
def read_data(columns, types={}, filename="daa/wxobs20170821.txt"):
    """
    Read data from CU data file
    Parameters:
       columns: A dictionary of column names to idices
       types: A dictionary o column names types to which to convert each column of data
       filename: a string
    """
    #initialize
    data = {} 
    for column in columns:
       data[column] = []

    with open(filename,"r") as datafile: 
        for i in range(3): 
            datafile.readline()

        # read and parse the rest of the file
        for line in datafile:
            split_line = line.split()  # blank value means split on whitespace, default.
            for column in columns:
                i = columns[column]
                t = types.get(column, str)
                value = t(split_line[i])
                data[column].append(value)
    return data






