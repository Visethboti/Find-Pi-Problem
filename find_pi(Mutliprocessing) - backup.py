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
    
    
    
from multiprocessing import Process
    
def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()



from multiprocessing import Pool

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(findpi, [100, 100, 100]))
    






import random
import matplotlib.pyplot as plt

class P:
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

def subfindpi(n):
    p = P()
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            p.x_inside.insert(0, x)
            p.y_inside.insert(0, y)
        else:
            p.x_outside.insert(0, x)
            p.y_outside.insert(0, y)
            
    return p

def findpi_2(n):
    p = subfindpi(n)
    
    print(4*(len(p.x_inside)/(len(p.x_outside) + len(p.x_inside))))
    plt.scatter(p.x_inside, p.y_inside, color = 'red')
    plt.scatter(p.x_outside, p.y_outside, color = 'blue')
    plt.title('Find Pi')
    plt.show()