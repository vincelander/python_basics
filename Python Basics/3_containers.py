"""
    CONTINERS
        Tuples 
            Example: my_tuple = ('Name', 123, 'Liza', [another List], (another Tuple))
            - defined by using parenthesis
            - can store different datatypes
            - values separated by comma
            - immutable or canot be changed
        List
            Example: my_tuple = ['Name', 123, 'Liza', [another List], (another Tuple)]
            - defined by using square brackets
            - can store different datatypes
            - values separated by comma
            - mutable or can be changed
        Set
            Example: my_tuple = {'Name', 123, 'Liza', [another List], (another Tuple)}
            - defined by using curly brackets
            - can store different datatypes
            - values separated by comma
            - mutable or can be changed
            - any duplicated values will be removed, must be unique
        Dictionary
            Example: my_tuple = {'key' : 'value', 123 : 'test', 'Liza' : [another List]}
            - defined by using curly brackets
            - can store different datatypes with some minor limitations
            - values separated by comma
            - mutable or can be changed
            - used to organize data
"""
user_tuple = ('Bob', 20, ['123 Street','Manila','Philippines'])
user_list = ['Bob', 20, ['123 Street','Manila','Philippines']]
user_set = {'Bob', 20, ('123 Street','Manila','Philippines'), 20}
user_dict = {
    'Name' : 'Bob',
    'Age' : 20,
    'Address' : ['123 Street','Manila','Philippines']
}
print(len(user_tuple), len(user_list), len(user_set), len(user_dict))
print(user_tuple,'\n',user_list,'\n',user_set,'\n',user_dict)

user_list.append('male')
user_list.append('employed')
user_list.append('True')
print(user_list)
print(len(user_list))

user_dict['Gender'] = 'male'
print(user_dict)
print(len(user_dict))

# slicing
print(user_tuple[0])
print(user_list[0])
print(user_list[0:3])       # returns from index 0 to 2
print(user_list[0:6:2])     # returns from index 0 to 5 with interval of 2
print(user_list[-1])        # returns from the last element
print(user_list[1:])
print(user_list[:4])

print(user_dict['Name'])

# print(len(user_list))
# print(user_list)

# user_list = ['Bob', 20, 20]
# print(user_list)
# print(set(user_list))

# exercise
print("========== EXERCISE ==========")
e_ist = [1,2,3,4,5,6,7,8,9,10]
print(e_ist)
print(e_ist[7:2:-2])