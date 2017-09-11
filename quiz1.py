#Max Low
#9-11-17
#quiz1.py - print name, enter numbers, do math and print, print a lucky number

from random import randint

print('Max Low')

num1 = float(Input('Enter a number: '))

num2 = float(Input('Enter an another number: '))

print('The sum is',num1+num2)
print('The product is',num1*num2)
print('Your lucky number is',randint(-10,10))

