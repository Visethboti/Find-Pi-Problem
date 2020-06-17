# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 22:33:28 2020

@author: Hister
"""

import worker_subfindpi
import multiprocessing
import time
import datetime
import math
import matplotlib.pyplot as plt
from csv import writer

def findpi(n, numWorkerProcess, numInputList, plot, note):
    
    # Avoid memory crash, Exit program when plot is 1 and too large n
    if(plot == 1 and n > 100000000):
        print("Too large, will result in memory crash! Exit Program...")
        exit()
    
    if(plot == 1):
        plotSTR = "Yes"
    else:
        plotSTR = "No"
        
    # Divide up n into a list for input process pool
    ninput = math.ceil(n/numInputList)
    inputList = []
    for _ in range(numInputList):
        inputList.append(ninput)
    
    print("Process started with: \n   n:", n,"| Work Process:", numWorkerProcess,"| List:", numInputList, "| Plot:", plotSTR)
    starttime = time.time()
    pool = multiprocessing.Pool(numWorkerProcess)
    print("Processing...")
    
    # Use subfindpiPlot or subfindpi (without plot)
    if(plot == 1):
        results = pool.map(worker_subfindpi.subfindpiPlot, inputList)
    else:
        results = pool.map(worker_subfindpi.subfindpi, inputList)
    
    pool.close()
    pool.join()
    print("Process finished")
    
    process_time = time.time() - starttime
    print('---------------||Result||---------------')
    print('  That took {} seconds.'.format(process_time))
    
    # Variable to get output
    total_inside = 0;
    total_outside = 0;
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    
    # Assign output from result to each variables
    for result in results:
        total_inside += result[0]
        total_outside += result[1]
        x_inside.append(result[2])
        y_inside.append(result[3])
        x_outside.append(result[4])
        y_outside.append(result[5])
    
    # Calculate and print pi
    pi_result = (4*(total_inside/(total_outside + total_inside)))
    print('  pi =',pi_result)
    print('----------------------------------------')
    
    # Plot
    if(plot == 1):
        starttime = time.time()
        print('Start Plotting...')
        plt.scatter(x_inside, y_inside, color = 'red')
        plt.scatter(x_outside, y_outside, color = 'blue')
        plt.title('Find Pi')
        plt.show()
        plot_time = time.time() - starttime
        print('Finished Plotting')
        print('That took {} seconds to plot'.format(plot_time))
    else:
        plot_time = None
        
    current_date = datetime.datetime.today().strftime('%d-%m-%Y')
    current_time = datetime.datetime.today().strftime('%H:%M:%S')
    
    with open('Find_pi_Report.csv', 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        #note = "testing without plot"
        print('Saving to Find_pi_Report.csv...')
        list_of_elem = [current_date, current_time, n, numWorkerProcess, numInputList, plotSTR, plot_time ,process_time , pi_result, note]
        csv_writer.writerow(list_of_elem)
        print('Save successful')
    print('Findpi(',n,',',numWorkerProcess,',',numInputList,',',plot ,') Finished!')



# input here
if __name__ == '__main__':
    findpi(10000, 1, 1, 0, 'Loading test')


