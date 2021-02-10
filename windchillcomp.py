#!/usr/bin/python
# comment

from readdata import read_data

data = []  #list
#you can index into lists.. and strings
# column names and column indeces to read
columns = {'date':0, 'time':1, 'tempout':2, 'windspeed':7, 'windchill':12} #dictionary - position in data list

# Data types for each column ( only if non-string )
types = {'tempout': float, 'windspeed':float, 'windchill':float} # convert to a float ( float is a function ptr )

#data = {'date':[], 'time':[], 'tempout':[]} #initialize to lists with names # hardcode deprecated
#time = data['time']

# read data from file that has the method
data = read_data(columns, types=types )

# negative indexes start at the end instead of the beginning

# Compute the wind chill temperature

def compute_windchill(temp, windspeed):
    a = 35.74
    b = 0.6215
    c = 35.75
    d = 0.4275

    v16 = windspeed ** 0.16
    windchill = a + ( b * temp) - ( c * v16) + ( d * temp * v16 )

    return windchill




#print (data['tempout'])

windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(compute_windchill(temp,windspeed))

# for wc_data, wc_comp in zip (windchill, data['windchill']):
#     print(f'{wc_data:.5f} {wc_comp:.5f} {wc_data - wc_comp:.5f}')

print ('               ORIGINAL  COMPUTED')
print (' DATE    TIME WINDCHILL  WINDCHILL DIFFERENCE')
print ('------- ----- ---------- --------- ----------')
zip_data = zip(data['date'], data['time'], data['windchill'], windchill )
for date, time , wc_orig, wc_comp in zip_data:
    wc_diff = wc_orig - wc_comp
    #> right justified
    print (f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')



