#Max Low
#9-1-17
#slope.py - calulator of the equation of a line given two points

x1 = int(input('x1'))
y1 = int(input('y1'))
x2 = int(input('x2'))
y2 = int(input('y2'))

slope = (y1-y2)/(x1-x2)

print('The slope is',slope)

b=(y1-(slope*x1))

print('The equation of the line is Y =',slope,'X+',b)
