#Max Low
#8-31-17
#tipCalculator.py

meal= float(input('Price of Meal(in dollars)'))
tip = float(input('% to tip'))

print('You should tip', round(meal*(tip*0.01),2) ,'dollars')
