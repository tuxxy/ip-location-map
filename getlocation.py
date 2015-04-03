#!/usr/bin/env python
from __future__ import print_function
from argparse import ArgumentParser
from contextlib import contextmanager
from sys import stdin, stdout, stderr
import json
try:
    import urllib2
except ImportError:
    import urllib.request as urllib2


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
def get_location(ip):
    print('Getting location for', ip, file=stderr)
    url = "https://freegeoip.net/json/{}".format(ip)
    ip_lookup = urllib2.urlopen(url)
    ip_data = json.loads(ip_lookup.read().decode('utf-8'))
    yield ip_data['longitude'], ip_data['latitude']


@contextmanager
def smart_open(file_or_filename, *args, **kwargs):
    try:
        f = open(file_or_filename, *args, **kwargs)
    except TypeError:
        yield file_or_filename
    else:
        with f:
            yield f


def main():
    parser = ArgumentParser()
    parser.add_argument('--input', '-i', default=stdin)
    parser.add_argument('--output', '-o', default=stdout)
    args = parser.parse_args()
    
    with smart_open(args.input) as istr:
        with smart_open(args.output, 'w') as ostr:
            for ip in istr:
                print(*get_location(ip), sep=",", file=ostr)

if __name__ == '__main__':
    main()
