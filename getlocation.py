#!/usr/bin/env python
from pyipinfodb import pyipinfodb
from sys import stdin, stderr
from functools import lru_cache

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
