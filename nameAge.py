#Max Low
#8-31-17
#nameAge.py - identifies the amount of charactures

Name = input('What is your name?(first and last)')
Age = int(input('What is your age?'))

Name1,Name2 = Name.split()

print('Your first name has', len(Name1) ,'letters')

print('Your last name has', len(Name2) ,'letters')

print('You will be', Age+1 ,'years old next year')