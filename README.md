# ZoneTransfer
Quick and dirty zone transfer using dnspython

## Usage
```shell
python3 axfr.py -d TARGET_DOMAIN
```

## Syntax
```shell
python3 axfr.py -h                
usage: axfr.py [-h] [-d DOMAIN]

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Target Domain
```

## Setup
```shell
python3 -m pip install dnspython
```
