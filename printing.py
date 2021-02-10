
def print_comparison(name, dates, times, original_data, computed_data ):
    """
    Print a comparison
    Parameters: a string and a list of floats
    name: A string name of data being compared no more than 9 characters
    dates: A list of strings
    times: A list of strings
    original_data List of original data floats
    computed_data: List of computed data
    """

    print ('      Stuff')
    print(f' DATE   TIME {name.upper():>9} {name.upper():>9} DIFFERENCE')
    print ('------- ---- --------- --------- ---------')
    zip_data = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        diff = orig - 1
        print(f'{date} {time:>6} {orig:9.6f} {comp:9.6f} {diff:10.6f}' )

