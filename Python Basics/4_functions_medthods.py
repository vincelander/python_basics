"""
    FUNCTIONS
        function_name('value')
        e.g.
            print("Welcome!)                        -> returns a value
            input("What is your name?")             -> accepts a value
            print(input("What is your name?\n"))    -> wrap a function insid another function
            print(print("What is your name?\n"))    -> other cases the same function cannot wrap in the same function
"""
# methods -> functions of datatypes
print("name".upper())
print("name".lower())
print("name".capitalize())
print("name".replace('n', 'N'))

# new functions
print(abs(-10.5))
print(max(10,1))
print(min(1,10))
print(len("Hello"))

# pythagorian theorem
print("pply pythagorian theorem to calculate hypotenuse of a triange.")
first_number = int(input("Input first number:  "))
second_number = int(input("Input second number: "))
print(((first_number ** 2) + pow(second_number, 2)) ** 1/2)
print(((first_number ** 2) + pow(second_number, 2)) ** .5)
hypotenuse = ((first_number ** 2) + pow(second_number, 2)) ** (1/2)
print(hypotenuse)