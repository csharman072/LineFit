import scipy as sp
import math as m
import numpy as np
from fitting_functions import linear
from fitting_functions import slope_units
from fitting_functions import print_equation

x = 1
m = 5
b = 2

x_units = 'seconds'
y_units = 'meters'

print('linear:',linear(m,x,b))
print('slope_units:',slope_units(x_units,y_units))
print_equation(m,b,x_units,y_units)



