#!/usr/bin/env python
from __future__ import print_function
from pyipinfodb import pyipinfodb
from sys import stdin, stderr
from functools import lru_cache

#TODO: move this to main, get api key from a CLI argument
ip_lookup = pyipinfodb.IPInfo('API_KEY_HERE')

@lru_cache(maxsize=None)
def get_location(ip):
    print('Getting location for', ip, file=stderr)
    ip_data = ip_lookup.get_city(ip)
    yield ip_data['longitude'], ip_data['latitude']

def main():
    for ip in stdin:
        print(*get_location(ip), sep=',')

if __name__ == '__main__':
    main()
