import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("project2sheet - Sheet1.csv", delimiter=",", dtype=str)
# data should be an np array. Write a temporary line of code that
# prints the first row of the array to check that this worked.
print(data)

x = data[1:, 0].astype(np.float32) # I did this one for you.
y = data[1:,1].astype(np.float32)
y2 = data[1:,2].astype(np.float32)

print("y = ", y2)
print("x = ", x)


params, params_cov = scipy.optimize.curve_fit(linear, x, y2)
slope = params[0]
intercept = params[1]
print(slope)
print(intercept)

a = np.array([x])
b = np.array([y2])

#exercise 1
print_equation(slope,intercept,'weight(g)','height(mm)')
#The equation of the line is: y = -0.05800000000856739 height(mm/weight(g) x + 58.60000000334091 height(mm)

fig = plt.figure()
plt.scatter(a,b,label='data')
plt.plot(a, linear(a,slope,intercept), label='non-linear fit')
plt.legend(loc='best')
plt.xlabel("weight(g)")
plt.ylabel("height(mm)")
x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line,label="Best fit")


plt.show()
fig.savefig("dataplot.png")
