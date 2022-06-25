import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import matplotlib as mpl

def color_graph(z_in, z_out):
    # 0. show the standard color graph
    # found on: https://stackoverflow.com/questions/31940285/plot-a-polar-color-wheel-based-on-a-colormap-using-python-matplotlib
    fig = plt.figure()

    display_axes = fig.add_axes([0.1, 0.1, 0.8, 0.8], projection='polar')
    display_axes._direction = 2 * np.pi  ## This is a nasty hack - using the hidden field to
    ## multiply the values such that 1 become 2*pi
    ## this field is supposed to take values 1 or -1 only!!

    norm = mpl.colors.Normalize(0.0, 2 * np.pi)

    # Plot the colorbar onto the polar axis
    # note - use orientation horizontal so that the gradient goes around
    # the wheel rather than centre out
    quant_steps = 2056
    cb = mpl.colorbar.ColorbarBase(display_axes, cmap=cm.get_cmap('hsv', quant_steps),
                                   norm=norm,
                                   orientation='horizontal')

    # aesthetics - get rid of border and axis labels
    cb.outline.set_visible(False)
    display_axes.set_axis_off()
    plt.show()  # Replace with plt.savefig if you want to save a file

    # 1. possible case: the z_in and z_out are complex numbers

    # 2. possible case: the z_in/z_out are actually (x,y) tuples/ arrays
    return 0
