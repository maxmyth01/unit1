#Max Low
#9-1-17
#PythagoreanDemo.py -- finding the hypotenuse of a right triangle

from math import sqrt

a = float(input('enter leg one'))
b = float(input('enter leg two'))

c= sqrt((a**2)+(b**2))

print('The hypotenuse is',c)