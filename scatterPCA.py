import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import datetime, os, glob, fnmatch, sys, itertools, netCDF4, pickle, time, warnings
from matplotlib.ticker import NullFormatter
from scipy.stats.stats import pearsonr, spearmanr
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText
import numpy as np
from scipy import linalg as LA


params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': 'xx-large',
         'axes.titlesize':'xx-large',
         'xtick.labelsize':'xx-large',
         'ytick.labelsize':'xx-large'}
pylab.rcParams.update(params)

def scatterplot(direc, x,xtitle,y,ytitle, xlim1=-25, xlim2=10, ylim1=-25, ylim2=10, binsx=10, binsy=10):
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
    axScatter.set_xlabel(xtitle+variable)
    axScatter.set_ylabel(ytitle+variable)
    axHistx.hist(x, bins=binsx)
    axHisty.hist(y, bins=binsy, orientation='horizontal')    
    axHistx.set_xlim(axScatter.get_xlim())
    axHisty.set_ylim(axScatter.get_ylim())
    pears=pearsonr(x,y)
    corrcoef=np.corrcoef(x,y)
    polyfit=np.polyfit(x,y,1)
    print(pears)
    print(polyfit) 
    print(corrcoef[0][1])
    c=np.linspace(xlim1,xlim2,360)
    d=polyfit[0]*c+polyfit[1]
    axScatter.plot(c,d, color='black', lw=3)
    axScatter.grid()
    fig.savefig(direc+"_"+xtitle+"_"+ytitle+'.png')
    #at = AnchoredText(('y='+str(pears[0])+'*x+'+str(pears[1])), prop=dict(size=10), frameon=True, loc=2 )
    #at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    #axScatter.add_artist(at)

    return fig, corrcoef[0][1]

direc='Figures/compare/P_Scat_'
''' Data from compareIsolde '''

variable = " Pressure [hPa]"
xtitle="Ulvebreen"
ytitle="Nordenskioldbreen"
y1=T_nomask[:,1]
y2=T_nomask[:,0]
fig2, s1 = scatterplot(direc, y1, xtitle, y2, ytitle, xlim1=np.min(y1) ,xlim2=np.max(y1) ,ylim1=np.min(y2) ,ylim2=np.max(y2), binsx=20, binsy=20)
plt.show()

xtitle="Ulvebreen"
ytitle="Lufthavn"
y1=T_nomask[:,1]
y2=T_nomask[:,2]
fig2, s2 = scatterplot(direc, y1, xtitle, y2, ytitle, xlim1=np.min(y1) ,xlim2=np.max(y1) ,ylim1=np.min(y2) ,ylim2=np.max(y2), binsx=20, binsy=20)
plt.show()

xtitle="Lufthavn"
ytitle="Nordenskioldbreen"
y1=T_nomask[:,2]
y2=T_nomask[:,0]
fig2, s3 = scatterplot(direc, y1, xtitle, y2, ytitle, xlim1=np.min(y1) ,xlim2=np.max(y1) ,ylim1=np.min(y2) ,ylim2=np.max(y2), binsx=20, binsy=20)
plt.show()

matrix = np.array([[1,s1,s2],
                   [s1,1,s3],
                   [s2,s3,1]])
print(matrix)
e_vals, e_vecs = LA.eig(matrix)
print("eigenvalues: ",e_vals)
print("Eigenvalue 1 = ", max(e_vals.real))
print("Eigenvalue 2 = ", np.median(e_vals.real))
print("Eigenvalue 3 = ", min(e_vals.real))
print("Variance of total data:")
print("Eigenvalue 1 = ", max(e_vals.real)/3*100)
print("Eigenvalue 2 = ", np.median(e_vals.real)/3*100)
print("Eigenvalue 3 = ", min(e_vals.real)/3*100)
print("eigenvectors: ")
print(e_vecs)
print("number 1:", e_vecs[0,0], e_vecs[1,0], e_vecs[2,0])
print("number 2:", e_vecs[0,1], e_vecs[1,1], e_vecs[2,1])
print("number 3:", e_vecs[0,2], e_vecs[1,2], e_vecs[2,2])




