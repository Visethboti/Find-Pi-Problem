from multiprocessing import Process
import random
import time

def subfindpi(n):
    inside = 0;
    outside = 0;
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            inside += 1
        else:   
            outside +=1

    print(4*inside/(inside+outside));

def findpi(num):
    starttime = time.time()
    
    process1 = Process(target=subfindpi, args=(num/6,))
    process2 = Process(target=subfindpi, args=(num/6,))
    process3 = Process(target=subfindpi, args=(num/6,))
    process4 = Process(target=subfindpi, args=(num/6,))
    process5 = Process(target=subfindpi, args=(num/6,))
    process6 = Process(target=subfindpi, args=(num/6,))
    
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    
    print('That took {} seconds'.format(time.time() - starttime))
    
    
    
from multiprocessing import Pool

if __name__ == '__main__':
    starttime = time.time()
    num = 1000000
    
    p = Pool(processes=20)
    data = p.map(subfindpi, [100])
    p.close()
    print(data)
    
    
    print('That took {} seconds'.format(time.time() - starttime))










from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    p = Pool(5)
    print(p.map(f, [1, 2, 3]))