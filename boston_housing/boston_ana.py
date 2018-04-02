# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:40:32 2017

@author: Apolo
"""

# Import libraries necessary for this project
import numpy as np
import pandas as pd
import visuals as vs # Supplementary code
from sklearn.cross_validation import ShuffleSplit

# Pretty display for notebooks
#matplotlib inline

# Load the Boston housing dataset
#data = pd.read_csv('housing.csv')
#prices = data['MEDV']
#features = data.drop('MEDV', axis = 1)

#pedro = np.arange(0, 11, 1)
#print pedro
    
# Success
#print "Boston housing dataset has {} data points with {} variables each.".format(*data.shape)

#print np.std(prices)

sleep = [5,6,7,8,10]
scores = [65,51,75,75,86]

sleep_mean = sleep - np.mean(sleep)

print np.sum(np.square(sleep))


print sleep_mean