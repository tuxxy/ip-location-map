#!/usr/bin/env python
from __future__ import print_function
from argparse import ArgumentParser
from contextlib import contextmanager
from pyipinfodb import pyipinfodb
from sys import stdin, stdout, stderr

def memoize(func):
    '''
    Decorator for a function which caches results. Based on
    http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
    '''
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = func(*key)
            return ret
        def __call__(self, *args):
            return self[args]
    
    return memodict()

@memoize
def get_location(ip_lookup, ip):
    print('Getting location for', ip, file=stderr)
    ip_data = ip_lookup.get_city(ip)
    yield ip_data['longitude'], ip_data['latitude']


@contextmanager
def smart_open(file_or_filename, *args, **kwargs):
    if isinstance(file_or_filename, (int, str, bytes)):
        with open(file_or_filename, *args, **kwargs) as f:
            yield f
    else:
        yield file_or_filename

def main():
    parser = ArgumentParser()
    parser.add_argument('--input', '-i', default=stdin)
    parser.add_argument('--output', '-o', default=stdout)
    parser.add_argument('API_KEY')
    args = parser.parse_args()
    
    ip_lookup = pyipinfodb.IPInfo(args.API_KEY)
    
    with smart_open(args.input) as istr:
        with smart_open(args.output, 'w') as ostr:
            for ip in istr:
                print(*get_location(ip_lookup, ip), sep=",", file=ostr)

if __name__ == '__main__':
    main()
