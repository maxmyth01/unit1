#Max Low
#9-7-17
#Binary.py - binary to base 10 converter

binary = int(input('Input and 8 digit binary number'))

runningTotal = (binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2*(binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2*2*(binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2*2*2*(binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2*2*2*2*(binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2*2*2*2*2*(binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2*2*2*2*2*2*(binary%10)
binary = (binary//10)

runningTotal = runningTotal+ 2*2*2*2*2*2*2*(binary%10)
binary = (binary//10)

print('That is',runningTotal)