#!/usr/bin/python
# comment

data = []  #list
data2 = {'date':[], 'time':[], 'tempout':[]} #initialize to lists with names

columns = {'date':0, 'time':1, 'tempout':2} #dictionary

types = {'tempout': float}
for column in columns:
    #data[column] = []  # initialize to be a list so as to be able to append it.
    print (column)
# use [] tp get to an item no matter what it is,

filename = "data/wxobs20170821.txt"

#datafile = open (filename,"r")
#print (datafile.readline())

#data = datafile.read() # read the whole file in 
#datafile.close()

# with - closes file, and 4 spaces needs to be consistent

# a "context manager" # setting it to the name datafile.

with open(filename,"r") as datafile: 
    #data = datafile.read()  
    for i in range(3): 
        datafile.readline()
    # read and parse the rest of the file
    for line in datafile:
        split_line = line.split()  # blank value means split on whitespace, default.
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data.append(value) 
        # datum is now a list of the split up string
        # data.append(datum) # adds another record to the data arrayist 
            data2['date'].append(split_line[0])

# negative indexes start at the end instead of the beginning


#print(data[8])
#print(data[8][4])
#print(data[8][4][0])
#print(data[8][::2]) # no start or end but always every other
#print(data[1:3])
#print(data[-1]) # last row
#for datum in data[:3]:  #[:4:2] - start at 0, do 4 by 2s
#   print(datum)

#print(type(data))







