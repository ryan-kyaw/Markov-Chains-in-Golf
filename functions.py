# -*- coding: utf-8 -*-

import random as r
import numpy as np 
import statistics as stat

# function to determine the initial state of our chain
def start(probmatrix, firststate, laststate):
    start = int(input("What is our initial state? "))
    if type(start) != int:
        start = r.randint(firststate, laststate)
    start_probs = probmatrix[start - 1, ]
    return start_probs, start

# fcn to determine the stopping condition of our chain
def stop():
    stop_condition = input("When do we stop this Markov Chain? After 'steps' or 'state'? ")
    if stop_condition == "steps":
        stop = int(input("How many steps? "))
    else: 
        stop = int(input("Which state do we stop at? "))
    return stop 

# fcn that goes through a Markov Chain and uses the start
# and stop conditions to print out the path of the random walk        
# Case 1: When the stopping condition is a state 

def path_state(probmatrix, startstate, finishstate):
    # Initialize the path_state array
    path_state = np.array([startstate])
    
    # While loop that goes through the array until the stopping condition is hit
    while path_state[-1] != finishstate:
        next_probs = probmatrix[path_state[-1] - 1, ]
        roll = r.random()
        current = 1
        while next_probs[current - 1] < roll:
            roll = roll - next_probs[current - 1]
            current = current + 1
        path_state = np.append(path_state, current)
    return path_state 
        
# Case 2: When the stopping condition is the number of steps we will
# be going through the chain
    
def path_steps(probmatrix, startstate, finishstate):  
    # Initialize the path_state array
    path_state = np.array([startstate])
    
    # While loop that goes through the array until the stopping condition is hit
    for i in range(0, finishstate):
        next_probs = probmatrix[path_state[-1] - 1, ]
        roll = r.random()
        current = 1
        while next_probs[current - 1] < roll:
            roll = roll - next_probs[current - 1]
            current = current + 1
        path_state = np.append(path_state, current)
    return path_state 

# Simulating the random walks as many times as you want and printing
# out the mean strokes after a certain amount of time 

def stats_state(probmatrix, startstate, finishstate, trials):
    length = []
    for i in range(0, trials):
        path = path_state(probmatrix, startstate, finishstate)
        length.append(len(path) - 1)
    mean_strokes = stat.mean(length)
    return mean_strokes
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


