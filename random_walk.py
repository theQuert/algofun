#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 11:49:18 2019

@author: quert
"""

from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


# Define parameters for the walk
dims = 1
step_n = 10000
step_set = [-1, 0, 1]
origin = np.zeros((1, dims))

# Simulate steps in 1-D
step_shape = (step_n, dims)
steps = np.random.choice(a=step_set, size = step_shape)
path = np.concatenate([origin, steps]).cumsum(0)
start = path[:1]
stop = path[-1:]

# Plot the path
fig = plt.figure(figsize = (8, 4), dpi = 200)
ax = fig.add_subplot(111)
ax.scatter(np.arange(step_n+1), path, c = 'blue', alpha = 0.25, s = 0.05)