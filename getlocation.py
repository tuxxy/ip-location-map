#!/usr/bin/env python
from pyipinfodb import pyipinfodb

ip_lookup = pyipinfodb.IPInfo('API_KEY_HERE')

coord_list = [] # List of tuples containing coordinates as (Longitude, Latitude)
with open('ips.txt','r') as ip_file:
    for ip in ip_file:
        print('Getting location for {}'.format(ip))
        ip_data=ip_lookup.get_city(ip)
        coord_list.append((ip_data['longitude'], ip_data['latitude']))

with open('geo.txt', 'w') as geo_file:
    for coordinates in coord_list:
        ip_longitude, ip_latitude = coordinates
        geo_file.write('{},{}\n'.format(ip_longitude, ip_latitude))
