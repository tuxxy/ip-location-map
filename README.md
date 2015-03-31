# ip-location-map

Here are some python scripts you can use to plot ip-addresses on a map


### Dependencies:

* [matplotlib basemap](http://matplotlib.org/basemap/)
* [pyipinfodb](https://github.com/mossberg/pyipinfodb)


### Short usage guide:

* First, you need to get an API key for [ipinfodb](http://ipinfodb.com/), and insert it in getlocation.py

* Put your IP-addresses in a file called **ips.txt**, with one IP on each line. (Note: only tested with IPv4)

* Run the **getlocation.py** script. It will create a file called **geo.txt**, which contains coordinates on each line.

* Finally, run the **generatemap.py** script. It will create an image file called map.png.

You can play around with the settings in **generatemap.py**, to use different map projections, different colors and so on.


I used this to plot refused SSH connections on my linux machine. I used the following command to fill ips.txt:

    grep "refused" /var/log/auth.log | awk '{ print $9 }' | sort | uniq > ips.txt

Note that i grep for lines with "refused". These are connections refused because of rules in /etc/hosts.deny and /etc/hosts.allow. You may need to change the command to suit your configuration.
