#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 14:22:07 2020

@author: quert
"""

import numpy as np
from matplotlib import pyplot as plt

np.random.seed(7)

x = np.random.rand(100, 1)
y = 2 + 5 * x + .2 * np.random.randn(100, 1)

idx = np.arange(100)
np.random.shuffle(idx)

train_idx = idx[:80]
val_idx = idx[80:]

x_train, y_train = x[train_idx], y[train_idx]
x_val, y_val = x[val_idx], y[val_idx]

plt.scatter(x_train, y_train)
plt.show()



np.random.seed(7)
a = np.random.randn(1)

lr = 1e-1
num_epochs = 500

for epoch in range(num_epochs):
    yhat = a + b * x_train
    error = (y_train - yhat)
    loss = (error ** 2).mean()
    
    a_grad = -2 * error.mean()
    b_grad = -2 * (x_train * error).mean()
    
    a = a - lr * a_grad
    b = b - lr * b_grad
print(a, b)

