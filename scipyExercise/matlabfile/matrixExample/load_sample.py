"""
load .mat file generated by genSample.m
"""

from scipy.io import loadmat

mat = loadmat('octave_a.mat')
a = mat['a']
print(a.shape)
