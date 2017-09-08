#Max Low
#9-7-17
#Binary.py - binary to base 10 converter

binary = int(input('Input and 8 digit binary number'))

runningTotal = (binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2**(1*(binary%10))
binary = (binary//10)

runningTotal = runningTotal+ 2**(2*(binary%10))
binary = (binary//10)

runningTotal = runningTotal+ 2**(3*(binary%10))
binary = (binary//10)

runningTotal = runningTotal+ 2**(4*(binary%10))
binary = (binary//10)

runningTotal = runningTotal+ 2**(5*(binary%10))
binary = (binary//10)

runningTotal = runningTotal+ 2**(6*(binary%10))
binary = (binary//10)

runningTotal = runningTotal+ 2**(7*(binary%10))
binary = (binary//10)

print('That is',runningTotal)