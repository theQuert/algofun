# coding='utf-8'
__author__ = "the-Quert (github.com/the-quert)"

import os
import re
import pandas as pd
import numpy as np

sample_list = [1, 2, 3]
np.array(sample_list)
type(sample_list)

my_matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(my_matrix)

# 'np.arange': 含下不含上/ 累加
np.arange(0, 5)
np.arange(0, 13, 6)

# 
np.zeros(4)
np.ones(4)

# 'np.linspace'區間平分
np.linspace(0, 1, 10)

# 'np.eye'
np.eye(1)
np.eye(3)

# 'np.random'
# 產生隨機數
# np.random.randn() 從'正態分佈'return多個sample
# np.random.rand() 隨機樣本位於 [0, 1)
# np.random.rand(sample_size)
# np.random.randn(sample_size)
arr1 = np.random.randn(2, 4)
arr1
arr2 = np.random.rand(2, 4)
arr2
# np.randint(low, high, sample_size)
# [low, high)
arr3 = np.random.randint(2, 5, size=(2, 4))
arr3

# array.reshape(sample_size): reshape the dimension, but elements are remained
arr = np.array([0, 1, 2, 3, 4, 5])
arr.reshape(2, 3)
# array.shape: check current shape of Numpy array
arr = np.array([0, 2, 3, 4, 5, 6])
arr.shape
arr.reshape(2, 3)
arr.reshape(2, 3).shape

# find the maximum and the minimum value of a NumPy array
# np.max(sample_array)
# np.argmax(sample_array): find the index of maximum in sample_array
simple_array = [1, 2, 3, 4]
np.array(simple_array)
np.max(simple_array)
np.argmax(simple_array)
np.min(simple_array)
np.argmin(simple_array)

# attributes and methods of NumPy arrays
arr = np.arange(0, 4)
arr
2 + arr
arr1 = np.arange(0, 6)
arr1
6*arr1
arr1/2
np.sqrt(arr1)
np.exp(arr1)
np.cos(arr1)
np.sin(arr1)
np.log(arr1)

# NumPy Indexing and Assignment
arr = np.random.rand(5)
arr
# np.round(sample_type, decimal_places)
arr = np.round(arr, 2)
arr
# array[:]
arr = np.array([ 0.12, 0.94, 0.66, 0.73, 0.83 ])
arr[:]
arr[1:]
arr[1:4]
arr[:3]
# array()
arr = np.array([ 0.12, 0.94, 0.66, 0.73, 0.83 ])
arr[:]
arr[2] = 0.88
arr
arr[]

# Assignment
new_array = np.array([ 6, 7, 8, 9])
sec_array = new_array[0:2]
sec_array[1] = 4
sec_array
new_array

# 'copy'
array_to_copy = np.array([ 1, 2, 3])
copied_array = array_to_copy.copy()
copied_array[2] = 300
array_to_copy
copied_array

# matrix
mat = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
mat
mat[0]
mat[0][-1]
mat[1:][:2]

# for loop
dist_in_km = [3, 5, 10, 21.1, 42.195]
dist_in_mile = []
for i in dist_in_km:
    dist_in_mile.append(i * 0.62137)
print(dist_in_mile)

# list comprehension
dist_in_km = [3, 5, 10, 21.1, 42.195]
dist_in_miles = [d * 0.62147 for d in dist_in_km]
print(dist_in_miles)

# lambda expression and map()
dist_in_km = [3, 5, 10, 21.1, 42.195]
dist_in_miles = list(map(lambda d: d * 0.62137, dist_in_km))
print(dist_in_miles)

# ndarray
lst = [42.195, 'km', True]
for i in lst:
    print(type(i))
arr = np.array(lst)
for i in arr:
    print(type(i))
    
# tensor
my_tensor = np.arange(1, 25).reshape(2, 4, 3)
my_tensor















