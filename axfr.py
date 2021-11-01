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
    
    if args.d:
        print(f'[*] Target Domain: {args.d}')

    # Act
    nses = dns.resolver.resolve(args.d, 'NS')
    for n in nses:
        ns_record = dns.resolver.resolve(n.to_text(), 'A')
        print(f'[*] {n.to_text()} - {ns_record[0].address}\r\n\t----')
        try:
            z = dns.zone.from_xfr(dns.query.xfr(ns_record[0].address, args.d))
            for n in sorted(z.nodes.keys()):
                print(f'{z[n].to_text(n)}')
            print('\t----')
        except dns.xfr.TransferError as e:
            print(f'Transfer denied!\r\n\t----')


if __name__ == '__main__':
    main()
