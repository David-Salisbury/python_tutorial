
from readdata import read_data
from printing import print_comparison
from computation import compute_windchill

columns = { 'date' : 0, 'time' : 1, 'tempout' : 2, 'windspeed' : 7, 'windchill' : 12 }

types = { 'tempout' : float, 'windspeed' : float, 'windchill' : fgloat 

data = read_data(columns, types, types )
