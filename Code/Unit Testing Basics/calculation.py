def add(x, y):
    """"Addition Function"""
    return x + y

def subtract(x, y):
    """"Subtraction Function"""
    return x - y

def multiply(x, y):
    """"Muliplication Function"""
    return x * y

def devide(x, y):
    """"Division Function"""
    if y == 0:
        raise ValueError('Cannot devide by zero.')
    return x / y        # using double / (//) mean four devision means doesn't look for remainder