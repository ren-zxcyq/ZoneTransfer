#!/usr/bin/env python3

import argparse
import dns.query
import dns.resolver
import dns.zone


def main():
    # Parse Args
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help='Target Domain', type=str)
    args = parser.parse_args()

    # Act
    try:
        nses = dns.resolver.resolve(args.domain, 'NS')
        for n in nses:
            ns_record = dns.resolver.resolve(n.to_text(), 'A')
            print(f'[*] {n.to_text()} - {ns_record[0].address}\r\n\t----')
            try:
                z = dns.zone.from_xfr(dns.query.xfr(ns_record[0].address, args.domain))
                for n in sorted(z.nodes.keys()):
                    print(f'{z[n].to_text(n)}')
                print('\t----')
            except dns.xfr.TransferError as e:
                print(f'Transfer denied!\r\n\t----')
            except Exception as e:
                print(f'Something went wrong while attempting to perform a zone transfer\r\n{str(e)}\r\n')
    except Exception as e:
        print(f'Something went wrong during the DNS resolving process!\r\n{str(e)}')


if __name__ == '__main__':
    main()
