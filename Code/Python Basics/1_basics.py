# EXECUTION ORDER
print("line 1") # string after this pound sign is ignored
print("line 2")
print("line 3")

# DATATYPES
print('words')  # string
print("words")
print(123)      # integer / int
print(-10)
print(1.25)     # floating point value / float

# OPERATIONS
print(3 + 3)    # to duplicate this line press alt + shift + down
print(3 - 3)
print(3 + 3)
print(3 / 3)
print(3 + 3.1230)
print(3 * "Hello World")    # integer + string not valid but multiplication is valid
print(10 - 5 * 2 + 3)       # order of operation runs automatically
print(10 - 5 * (2 + 3))     # add parenthesis to manipulate order

"""
    VARIABLES
    - Mandatory
        - only letters A-z. 0-9, _
        - cannot start with number
        - case sensitive
        - cannot use inbuilt function names

    - Beneficial
        - Be clear
        - use snake case (e.g. test_value)

"""
test = 123      # created a variable by asigning value using = sign
print(test)     # print varibale to see
test = test + 2 # to update test using the same + a number
print(test)
print(test + 2) # shorter and better approach

# INPUTS
user_name = input("What is your name?\n")
print("Hello ", user_name, " have a nice day!")
print("Hello", user_name,"have a nice day!")    # pytho automatically adds a space in concatenation when using comma
