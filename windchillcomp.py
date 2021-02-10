#!/usr/bin/python
# comment

from readdata import read_data
from  printing import print_comparison
from computation import compute_windchill


#you can index into lists.. and strings
data = []  #list

# column names and column indeces to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12} #dictionary - position in data list

# Data types for each column ( only if non-string )
types = {'tempout': float, 'windspeed':float, 'windchill':float} # convert to a float ( float is a function ptr )

# read data from file that has the method
data = read_data(columns, types=types )

# negative indexes start at the end instead of the beginning

# Compute the wind chill temperature

windchill = [computer_windchill(t,w) for t, w in zip(data['tempout'], data['windspeed'])]
#windchill = []
#for temp, windspeed in zip(data['tempout'], data['windspeed']):
#    windchill.append(compute_windchill(temp,windspeed))

# for wc_data, wc_comp in zip (windchill, data['windchill']):
#     print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

print_comparison('Windchill', data['date'], data['time'], data['windchill'], windchill )

