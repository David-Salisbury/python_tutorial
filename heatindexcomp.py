#!/usr/bin/python
# comment

from readdata import read_data

#you can index into lists.. and strings
# column names and column indeces to read
columns = {'date':0, 'time':1, 'tempout':2, 'humout':5, 'heatindex' : 13} #dictionary - position in data list

# Data types for each column ( only if non-string )
types = {'tempout': float, 'humout' : float, 'heatindex' : float} # convert to a float ( float is a function ptr )

data = {}
for column in columns:
    data[column] = []  # add a new key.  initialize the list so as to be able to append it.
    print (column)

# use [] tp get to an item no matter what it is,

filename = "data/wxobs20170821.txt"

#read data from file

data = read_data(columns, types=types)

# negative indexes start at the end instead of the beginning

# Compute heat index 

def compute_heatindex(temp, humidity):
    a = -42.379
    b = 2.04901523
    c = 10.14333127
    d = 0.22475541
    e = 0.00683783
    f = 0.05481717
    g = 0.00122874
    h = 0.00085282
    i = 0.00000199

    rh = humidity / 100

    heatindex = ( a + (b * temp ) + ( c * rh ) +
                 ( d * temp * rh ) +
                 ( e * temp ** 2 ) +
                 ( f * rh ** 2 ) + ( g * temp ** 2 * rh ) +
                 ( h * temp * rh ** 2 ) +
                 ( i * temp ** 2 * rh ** 2 ))

    return heatindex



#print (data['tempout'])

heatindex = []
for temp, humout in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp,humout))

# for wc_data, wc_comp in zip (windchill, data['windchill']):
#     print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

print ('               ORIGINAL  COMPUTED')
print (' DATE    TIME HEATINDEX HEATINDEX  DIFFERENCE')
print ('------- ----- ---------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex )
for date, time , hi_orig, hi_comp in zip_data:
    hi_diff = hi_orig - hi_comp
    #> right justified
    print (f'{date} {time:>6} {hi_orig:9.6f} {hi_comp:9.6f} {hi_diff:10.6f}')



