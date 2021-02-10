#!/usr/bin/python
# comment

data = []  #list
data = {}  #dictionary
#you can index into lists.. and strings
# column names and column indeces to read
columns = {'date':0, 'time':1, 'tempout':2} #dictionary

# Data types for each column ( only if non-string )
types = {'tempout': float} # convert to a float ( float is a function ptr )

#data = {'date':[], 'time':[], 'tempout':[]} #initialize to lists with names # hardcode deprecated
#time = data['time']
for column in columns:
    data[column] = []  # add a new key.  initialize the list so as to be able to append it.
    print (column)

# use [] tp get to an item no matter what it is,

filename = "data/wxobs20170821.txt"

for column in columns: # loop through each of the keys in our dictionary 
    data[column] = [] # data[date], data[time]..

# a "context manager" # setting it to the name datafile.

with open(filename,"r") as datafile:  # closes the file too 
    #data = datafile.read()  
    for i in range(3): 
        datafile.readline()
    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()  # blank value means split on whitespace, default.
        # instead of the below we do the following for loop
        #data['date'].append(split_line[0])
        #data['time'].append(split_line[1])
        #data['tempout'].append(float(split_line[2]))
        for column in columns:   # make our new data dictionary
            i = columns[column]  # i shorthand for index  i will be 0, 1 or 2
            t = types.get(column,str)
            print(t)
            value = t(split_line[i])
            data[column].append(value) 

# negative indexes start at the end instead of the beginning

#print (data['tempout'])




