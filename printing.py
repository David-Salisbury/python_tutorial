def print_comparison(name, dates, times, original_data, coputed_data ):
    """
    Print a comparison
    Parameters:
    name: string name of data being compared no more than 9 characters
    dates: list of strings
    times: list of strings
    original_data list of original data floats
    computed_data: list of computed data
    """

    print ('      Stuff')
    print(f' DATE   TIME {name.upper():>9}')
    print ('------- ----')
    zip_datai = zip(dates, times, original_data, computed_data)
    for date, time, orig, comp in zip_data:
        diff = orig - comp
        print(f'{data} {time:>6} comp:9.6f} {diff:10.6f}' )

