#!/usr/bin/python
# comment

data = []  #list

filename = "data/wxobs20170821.txt"

#datafile = open (filename,"r")
#print (datafile.readline())

#data = datafile.read() 
#datafile.close()

# with - closes file, and 4 spaces needs to be consistent

# a "context manager" # setting it to the name datafile.

with open(filename,"r") as datafile: 
    #data = datafile.read()  
    for i in range(3):
        datafile.readline()
    # read and parse the rest of the file
        for line in datafile:
            datum = line.split()  # blank value means split on whitespace, default.
            # datum is not a list of the split up string
            data.append(datum) # adds another record to the data arrayist 

    data2 = {'date':[], 'time':[], 'tempout':[]}

    for line in datafile:
        split_line = line.split()
        data2['data'].append(split_line[0])
        data2['time'].append(split_line[1])
        data2['tempout'].append(float(split_line[2])) # integer only on floats

# DEBUG
#print(data[8])
#print(data[8][4])
#print(data[8][4][0])
#print (data[8][::2]) # no start or end but always every other
#print (data2['tempout']
#print(data[1:3])
#print(data[-1]) # last row
#for datum in data[:3]:  #[:4:2] - start at 0, do 4 by 2s
#   print(datum)

#print(type(data))







