# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:03:44 2020

@author: Hister
"""

import time
import random
import matplotlib.pyplot as plt

def findpi(n):
    p_circle = 0
    p_outside = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    
    starttime = time.time()
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            p_circle += 1
            x_inside.insert(0, x)
            y_inside.insert(0, y)
        else:
            p_outside += 1
            x_outside.insert(0, x)
            y_outside.insert(0, y)
            
    print(4*(p_circle/(p_outside + p_circle)))
    print('That took {} seconds'.format(time.time() - starttime))
    plt.scatter(x_inside, y_inside, color = 'red')
    plt.scatter(x_outside, y_outside, color = 'blue')
    plt.title('Find Pi')
    plt.show()
    
    
    
    
    
    
    
    
    
    
    

#with loading bar

import time
import random
import matplotlib.pyplot as plt
import math

def findpi(n):
    loading = 0;
    percent = 0;
    p_circle = 0
    p_outside = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    
    starttime = time.time()
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            p_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            p_outside += 1
            x_outside.append(x)
            y_outside.append(y)
        if(loading <= i):
            print(percent, "% complete.")
            loading += math.floor(n/100)
            percent += 1
    
    print("=======|Completed|========")
            
    print(4*(p_circle/(p_outside + p_circle)))
    print('That took {} seconds to calculate'.format(time.time() - starttime))
    
    starttime = time.time()
    plt.scatter(x_inside, y_inside, color = 'red')
    plt.scatter(x_outside, y_outside, color = 'blue')
    plt.title('Find Pi')
    plt.show()
    print('That took {} seconds to plot'.format(time.time() - starttime))
    










#with loading bar and on/off plot

import time
import random
import matplotlib.pyplot as plt
import math

def findpi(n, plot):
    loading = 0;
    percent = 0;
    p_circle = 0
    p_outside = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    
    starttime = time.time()
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            p_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            p_outside += 1
            x_outside.append(x)
            y_outside.append(y)
        if(loading <= i):
            print(percent, "% complete. Pi is: ", (4*(p_circle/(p_outside + p_circle))))
            loading += math.floor(n/100)
            percent += 1
    
    print("=======|Completed|========")
            
    print(4*(p_circle/(p_outside + p_circle)))
    print('That took {} seconds to calculate'.format(time.time() - starttime))
    
    if(plot == 1):
        starttime = time.time()
        plt.scatter(x_inside, y_inside, color = 'red')
        plt.scatter(x_outside, y_outside, color = 'blue')
        plt.title('Find Pi')
        plt.show()
        print('That took {} seconds to plot'.format(time.time() - starttime))

    print("Findpi() finished.")