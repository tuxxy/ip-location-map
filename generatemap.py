from mpl_toolkits.basemap import Basemap
from sys import stdin
import matplotlib.pyplot as plt
import numpy as np
 

def plot_locations(locations, output_filename):
    ip_map = Basemap(projection='robin', lon_0=0, resolution='c')

    for line in locations:
    	srclong, srclat = map(float, line.split(','))
    	x, y = ip_map(srclong, srclat)
    	plt.plot(x,y, 'o', color='#ff0000', ms=2.7, markeredgewidth=0.5)


    ip_map.drawcountries(color='#ffffff')
    ip_map.fillcontinents(color='#cccccc',lake_color='#ffffff')
    
    plt.savefig(output_filename, dpi=600)

if __name__ == '__main__':
    plot_locations(stdin, "ip_map.png")
