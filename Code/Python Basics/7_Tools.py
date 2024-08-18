# string concatenation
first_name = "Bob"
last_name = "Marley"
age = 19

user_info = first_name + " " + last_name + " is " + str(age) + " years old."   # bad approach
print(user_info)

# f strings
user_info = f"{first_name} {last_name} is {age} years old."
print(user_info)


# single line ifs
if age <= 18:
    status = "Child"
else:
    status = "Adult"

print(f"{first_name} is {status}")

status = "Child" if age <= 18 else "Adult"
print(f"{first_name} is {status}")


# list comprehension
simple_list = []
for i in range(1,11,1):         # bad approach
# for i in range(10):             # bad approach
    simple_list.append(i)

print(simple_list)

simple_list = [i+1 for i in range(10)]
print(simple_list)

simple_list = [i for i in range(1,11,1)]
print(simple_list)

simple_list = [i * 2 for i in range(1,11,1)]
print(simple_list)

simple_list = [i * 2 for i in range(1,11,1) for j in ['a', 'b', 'c']]
print(simple_list)

simple_list = [f'{i}{j}' for i in range(1,11,1) for j in ['a', 'b', 'c']]
print(simple_list)

simple_list = [f'{i}{j}' for i in range(1,11,1) for j in ['a', 'b', 'c'] if j == 'a']
print(simple_list)


# dictionarry comprehension SERCH FOR IT.

# lambda function
def double_number(num):     # bad approach
    return num * 2

print(double_number(5))

double_value = lambda num = 5: num * 2
print(double_value())
print(double_value(5))

# some func wants a func as args
random_list_1 = [5,2,3,1,4]

sorted_list = sorted(random_list_1)
print(sorted_list)

random_list_2 = [('Bob',18),('Anna',20),('Marley',9)]

sorted_list = sorted(random_list_2)
print(sorted_list)

sorted_list = sorted(random_list_2, key=lambda i_tuple: i_tuple[1])
print(sorted_list)

print("\n========== EXERCISE ==========\n")

e_list = [f"{j+str(i) if (j+str(i))!='C3' else ''}" for i in range(1,6,1) for j in ['A','B','C','D','E']]
print(e_list)

e_list = [f"{j}{i}" for i in range(1,6,1) for j in ['A','B','C','D','E'] if f"{j}{i}" != 'C3']
print(e_list)       # correct