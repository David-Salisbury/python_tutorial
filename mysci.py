
# comment

filename = "data/wxobs20170821.txt"

#datafile = open (filename,"r")
#print (datafile.readline())
#print (datafile.readline())
#print (datafile.readline())
#print (datafile.readline())

#data = datafile.read() 
#datafile.close()

with open(filename,"r") as datafile: # a "context manager" # setting it to the name datafile.
    data = datafile.read()  # with - closes file, and 4 spaces needs to be consistent

# DEBUG

print(type(data))
