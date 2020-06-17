# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 21:54:44 2020

@author: Hister
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:03:44 2020

@author: Hister
"""

import random
import matplotlib.pyplot as plt
from multiprocessing import Pool

def findpi(n):
    p_circle = 0
    p_outside = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
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
            
    return 4*(p_circle/(p_outside + p_circle))
    #plt.scatter(x_inside, y_inside, color = 'red')
    #plt.scatter(x_outside, y_outside, color = 'blue')
    #plt.title('Find Pi')
    #plt.show()






import random
import matplotlib.pyplot as plt
import time
import multiprocessing 

class Points:
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

def subfindpi(n, q):
    p = Points()
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            p.x_inside.insert(0, x)
            p.y_inside.insert(0, y)
        else:   
            p.x_outside.insert(0, x)
            p.y_outside.insert(0, y)
            
        q.put(['hello'])

def findpi_2(n):
    starttime = time.time()
    q = multiprocessing.SimpleQueue()
    
    process1 = multiprocessing.Process(target=subfindpi, args=(n, q))
    process1.start()
    process1.join()

    print(q.get())
    q.close()
    print('That took {} seconds'.format(time.time() - starttime))
    
    #print(4*(len(p.x_inside)/(len(p.x_outside) + len(p.x_inside))))
    #plt.scatter(p.x_inside, p.y_inside, color = 'red')
    #plt.scatter(p.x_outside, p.y_outside, color = 'blue')
    #plt.title('Find Pi')
    #plt.show()









if __name__ == '__main__':
    starttime = time.time()
    
    processes = []
    
    p = multiprocessing.Process(target=subfindpi, args=(10, ))
    p.start()
    p.join()

    data = return_dict.values()
    print(return_dict)
        
    print('That took {} seconds'.format(time.time() - starttime))







import random
import matplotlib.pyplot as plt
import time
import multiprocessing 

class Points:
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

def subfindpi(n):
    p = Points()
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            p.x_inside.insert(0, x)
            p.y_inside.insert(0, y)
        else:   
            p.x_outside.insert(0, x)
            p.y_outside.insert(0, y)

    return 3

def foo(n):
    return n+1

def findpi_3(num):
    starttime = time.time()
    
    process = multiprocessing.Pool(processes=2)
    data = process.map(subfindpi, [num])
    process.close()
    print(data)
    
    print('That took {} seconds'.format(time.time() - starttime))
    
    #print(4*(len(p.x_inside)/(len(p.x_outside) + len(p.x_inside))))
    #plt.scatter(p.x_inside, p.y_inside, color = 'red')
    #plt.scatter(p.x_outside, p.y_outside, color = 'blue')
    #plt.title('Find Pi')
    #plt.show()
    
if __name__ == '__main__':
    starttime = time.time()
    
    process = multiprocessing.Pool(processes=2)
    data = process.map(foo, [10])
    process.close()
    print(data)
    
    print('That took {} seconds'.format(time.time() - starttime))