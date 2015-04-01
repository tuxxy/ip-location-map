from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 

ip_map = Basemap(projection='robin', lon_0=0, resolution='c')

with open('geo.txt','r') as f:
	for line in f.readlines():
		srclong, srclat = line.split(',')
		srclong=float(srclong)
		srclat=float(srclat)
		x, y = ip_map(srclong, srclat)
		plt.plot(x,y, 'o', color='#ff0000', ms=2.7, markeredgewidth=0.5)


ip_map.drawcountries(color='#ffffff')
ip_map.fillcontinents(color='#cccccc',lake_color='#ffffff')

plt.savefig('ip_map.png', dpi=600)
