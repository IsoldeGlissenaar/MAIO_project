import numpy as np
import matplotlib.pyplot as plt
import datetime, os, glob, fnmatch, sys, itertools, netCDF4, pickle, time, warnings
from matplotlib.ticker import NullFormatter
from scipy.stats.stats import pearsonr, spearmanr
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

def scatterplot(title, x,xtitle,y,ytitle, xlim1, xlim2, ylim1, ylim2, binsx=10, binsy=10):
    nullfmt = NullFormatter()         # no labels    
    # definitions for the axes
    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width + 0.02   
    rect_scatter = [left, bottom, width, height]
    rect_histx = [left, bottom_h, width, 0.2]
    rect_histy = [left_h, bottom, 0.2, height]
    # start with a rectangular Figure
    fig = plt.figure(1, figsize=(8, 8))
    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)
    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)
    # the scatter plot:
    axScatter.scatter(x, y)
    # now determine nice limits by hand:
    binwidth = 0.25
    xymax = np.max([np.max(np.fabs(x)), np.max(np.fabs(y))])
    lim = (int(xymax/binwidth) + 1) * binwidth    
    axScatter.set_xlim((xlim1, xlim2))
    axScatter.set_ylim((ylim1, ylim2))
    axScatter.set_xlabel(xtitle)
    axScatter.set_ylabel(ytitle)
    axHistx.hist(x, bins=binsx)
    axHisty.hist(y, bins=binsy, orientation='horizontal')    
    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())
    pears=pearsonr(x,y)
    #pears=spearmanr(x,y)
    c=np.linspace(-lim,lim,360)
    d=pears[0]*c+pears[1]
    axScatter.plot(c,d, color='black', lw=3)
    print(c,d)
    at = AnchoredText(('y='+str(pears[0])+'*x+'+str(pears[1])),
                      prop=dict(size=10), frameon=True, loc=2 )
    at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    axScatter.add_artist(at)

    return fig
    
city1="ulvebreen"
city2="nordenskioldbreen"
### Create data
x1=T_ulve_c 
y1=T_norden_c

### Plot data
fig=plt.figure('Average Daily Precipitation per Month', figsize=(10,5))
plt.plot(x1, y1, label=city1)
plt.scatter(x1, y1, s=20, color='red', marker=u'o') 
plt.plot(x2, y2, label=city2)
plt.scatter(x2, y2, s=20, color='red', marker=u'o') 
plt.legend()
plt.title('Average Daily Precipitation per Month') # Title at top of plot
plt.xlabel('time [years]') # label along x-axes
plt.ylabel('Total Precipitation [mm of water]') # label along x-axes
plt.grid(True); plt.show() # show plot on screen

title="test"
xtitle=city1
ytitle=city2
fig2 = scatterplot(title, y1, xtitle, y2, ytitle, xlim1=-20 ,xlim2=20 ,ylim1=-20 ,ylim2=20, binsx=20, binsy=20)
plt.show()
