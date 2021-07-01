import scipy
from scipy.cluster.hierarchy import fcluster
from scipy import stats
import scipy.cluster.hierarchy as hac
import statistics
from statistics import mode
from math import floor
import random
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import matplotlib
from cellNames import getCellName
import datetime
from numpy import genfromtxt

print('here')

dist = genfromtxt('muscle_dist2.csv', delimiter=',')
dist = dist.tolist()

print(dist)


Z = hac.linkage(dist,  method='ward')
np.savetxt('muscle_ward_distance.csv', Z, delimiter = ',')
exec(open('python/randomScripts/sendEmail.py').read())
