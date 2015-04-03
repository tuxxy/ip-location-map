# ip-location-map

[[ ORIGINALLY AUTHORED BY: Joakim Algrøy (https://github.com/joakimalgroy) ]]

Here are some python scripts you can use to plot ip-addresses on a map

### API:

This branch uses the [freegeoip API](https://freegeoip.net), so you don't need an API Key to use it.
However, you are limited to 10,000 requests per hour.

### Dependencies:

* [matplotlib basemap](http://matplotlib.org/basemap/)

### Short usage guide:

* Put your IP-addresses in a file called **ips.txt**, with one IP on each line. (Note: only tested with IPv4)

* Run the **getlocation.py** script, like so: `python getlocation.py < ips.txt > geo.txt` It will create a file called **geo.txt**, which contains coordinates on each line.

* Finally, run the **generatemap.py** script, like so: `python generatemap.py < geo.txt` It will create an image file called map.png.

You can play around with the settings in **generatemap.py**, to use different map projections, different colors and so on.


I used this to plot refused SSH connections on my linux machine. I used the following command to fill ips.txt:

    grep "refused" /var/log/auth.log | awk '{ print $9 }' | sort | uniq > ips.txt

You can also run the whole process as a single pipeline:
    
    grep "refused" /var/log/auth.log | awk '{ print $9 }' | sort | uniq | python getlocation.py <API_KEY> | python generatemap.py

Note that I grep for lines with "refused". These are connections refused because of rules in /etc/hosts.deny and /etc/hosts.allow. You may need to change the command to suit your configuration.
