''' Simple script to give an educated guess of how much you should pay based on
Zillow price history for a house given the previous sale. Self explanatory. '''

import numpy as np
import datetime 

#start_money = 138000
start_money = input('Input starting worth of house based on last sold price:\n')
#start_year = 2012
start_year = input('What year?\n')
#interest_rate = 2
interest_rate = input('Provide an interest rate (in %):\n')

# Recalc interest rate to be used for math
interest_rate = (float(interest_rate)/100)+1

#this_year = 2017
now = datetime.datetime.now()
this_year = now.year

num_years = this_year - int(start_year)

print('Year:\t Value:')
current_value = float(start_money)
current_year = int(start_year)
for i in range(num_years+1):
    print(str(current_year) + '\t' + '$ {:0.2f}'.format(current_value))
    current_value = current_value*interest_rate  
    current_year += 1
    i += 1

