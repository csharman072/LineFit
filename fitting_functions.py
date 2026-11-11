import scipy as sp
import math as m
import numpy as np


def linear(m,x,b):
    return (m*x)+b

def slope_units(x_units,y_units):
    return y_units.rstrip('s')+'/'+x_units.rstrip('s')

#(c) print_equation takes in 4 parameters: m and b (which are numbers),
#y_units and x_units. It should print a string in this format:
#"The equation of the line is: y =  4 in/sec x + 9.9 in"
#It should calculate the slope units by calling the previous function. 

def print_equation(m,b,x_units,y_units):
    print('The equation of the line is: y =',m,slope_units(x_units,y_units),'x +',b,(y_units))

    
