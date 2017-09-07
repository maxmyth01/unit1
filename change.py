#Max Low
#9-7-17
#change.py - enter an amount of cents and converts into coins

change = float(input('Enter an amount of change')) 
change = change*100
quarter = change//25
change = change - 25*quarter
dime = change//10
change = change - 10*dime
nickle =change//5
change = change - 5*nickle
pennie = change
print('That is',quarter ,'Quarters', dime ,'Dimes', nickle ,'Nickles',pennie,'Pennies')