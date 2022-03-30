def sum(arg):
    '''
    Creates a variable called total, iterates over all the values in arg, 
    and adds them to total. 
    It then returns the result once the iterable has been exhausted.
    '''
    total = 0
    for val in arg:
        total += val
    return total