from pyzfn import Pyzfn as op           # 'op' function to open the .zarr files
from pyzfn import utils                 # other various utilities
import numpy as np                      # working with vector data
from matplotlib import pyplot as plt    # plotting graphs
import cmocean                          # pretty colormaps
import ipywidgets                       # interactive widgets

def plot_2d_magnetization(path:str, dset:str):
    task = op(path) # Open the simulation data in python
    fig, axes = plt.subplots(3,1, figsize=(10, 5), sharex=True, sharey=True) # create empty figure
    for comp,ax in enumerate(axes): # loop over the 3 components of the magnetization
        im = ax.imshow( # plot the magnetization component
            task[dset][0,0,:,:,comp],  # `mag` is a numpy array
            cmap=cmocean.cm.balance,  # pretty colormap
            origin="lower", # put the origin at the bottom left
            extent=[0, task.Tx*1e9, 0, task.Ty*1e9], # set the x and y axis limits ( in nm )
            vmin=-1, # set the color scale limits ( reducded magnetization is from -1 to 1 )
            vmax=1 # set the color scale limits ( reducded magnetization is from -1 to 1 )
            )
        ax.grid(True) # show the grid
        cb = fig.colorbar(im, ax=ax) # add a colorbar
        cb.set_label(f"m_{['x','y','z'][comp]}") # set the colorbar label
        ax.set_ylabel("y (nm)") # set the y axis label
    axes[-1].set_xlabel("x (nm)") # set the x axis label
    plt.tight_layout() # make the plot pretty