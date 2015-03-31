from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 

map = Basemap(projection='robin', lon_0=0, resolution='c')

f=open('geo.txt','r')
for line in f.readlines():
	srclong, srclat = line.split(',')
	srclong=float(srclong); srclat=float(srclat)
	x, y = map(srclong,srclat)
	plt.plot(x,y, 'o', color='#ff0000', ms=2.7, markeredgewidth=0.5)


map.drawcountries(color='#ffffff')
map.fillcontinents(color='#cccccc',lake_color='#ffffff')

plt.savefig('map.png', dpi=600)
