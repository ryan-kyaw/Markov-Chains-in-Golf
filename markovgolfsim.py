# -*- coding: utf-8 -*-

# Proposed Markov Chain Model 
# Each number generated corresponds to a shot and where it goes 

import random as r
import numpy as np 
import pandas as pd
import statistics as stat

# Need to establish the Markov Chains

# 100-150 yard par 3 Chain

P = np.array([[0, 0.15, 0.15, 0.25, 0.25, 0.15, 0.05, 0],
              [0, 0, 0.05, 0.15, 0.2, 0.4, 0.2, 0],
              [0, 0, 0, 0, 0, 0.05, 0.85, 0.1],
              [0, 0, 0, 0, 0, 0, 0.7, 0.3],
              [0, 0, 0, 0, 0, 0, 0.4, 0.6],
              [0, 0, 0, 0, 0, 0, 0.25, 0.75],
              [0, 0, 0, 0, 0, 0, 0.05, 0.95],
              [0, 0, 0, 0, 0, 0, 0, 1]])

from functions import * 

avg = stats_state(P, 1, 8, 50)

print(avg)
    

     
            
    
        
 






