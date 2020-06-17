# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 22:34:08 2020

@author: Hister
"""
import random

def subfindpiPlot(n):
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
            x_inside.append(x)
            y_inside.append(y)
        else:
            p_outside += 1
            x_outside.append(x)
            y_outside.append(y)

    return [p_circle, p_outside, x_inside, y_inside, x_outside, y_outside]


def subfindpi(n):
    loading = 0
    percent = 0
    p_circle = 0
    p_outside = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if((x**2 + y**2) < 1):
            p_circle += 1
        else:
            p_outside += 1

    return [p_circle, p_outside, [], [], [], []]