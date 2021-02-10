#!/usr/bin/python
# comment

from readdata import read_data
from printing import print_comparison
from computation import compute_heatindex

#you can index into lists.. and strings
# column names and column indeces to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex' : 13} #dictionary - position in data list

# Data types for each column ( only if non-string )
types = {'tempout': float, 'humout' : float, 'heatindex' : float} # convert to a float ( float is a function ptr )

# use [] tp get to an item no matter what it is,

filename = "data/wxobs20170821.txt"

#read data from file

data = read_data(columns, types=types)

# negative indexes start at the end instead of the beginning

# Compute heat index 

#print (data['tempout'])
heatindex = [compute_heatindex(t,h) for t, h in zip(data['tempout'], data['humout'])]


#heatindex = []
#for temp, humout in zip(data['tempout'], data['humout']):
#    heatindex.append(compute_heatindex(temp,humout))

# for wc_data, wc_comp in zip (windchill, data['windchill']):
#     print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

print_comparison('heatindex', data['date'], data['time'], data['heatindex'], heatindex )



