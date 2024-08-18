# if statements
print(5 == 5)

if 5 > 4:
    print("5 is greater tha 4")

if 3 > 4:
    print("5 is greater tha 4")

print("run without checking if condition if true")

if 5 > 4:
    print("5 is greater tha 4")
else:
    print("5 is NOT greater tha 4")

if 3 > 4:
    print("5 is greater tha 4")
else:
    print("5 is NOT greater tha 4")

if 3 > 4:
    print("5 is greater tha 4")
elif 4 == 4:
    print("4 is equal to 4")
else:
    print("5 is NOT greater tha 4")

if 3 > 4:
    print("5 is greater tha 4")
elif 4 == 4:
    print("4 is equal to 4")
    if len([1,2,3]) > 2:
        print("length of list is greater than 2")
else:
    print("5 is NOT greater tha 4")

# whle loop
count = 0
while count <= 10:
    print("Count is", count)
    count += 1

print("end of first while loop")

while True:
    print("Count is", count)
    count += 1
    if count > 20:
        break
print("end of second while loop")

# for loop -> works for all containers
test_list = [1,2,3,4,5,6,7,8,9,"Test"]
for i in test_list:
    print(i)

test_dict = {
    'Name' : 'Bob',
    'Age' : 20,
    'Address' : ['123 Street','Manila','Philippines']
}
for i in test_dict: # -> default is dict.keys()
    print(i)

for i in test_dict.values():
    print(i)

for i in test_dict.items(): # -> returns key value pair in a tuple type
    print(i)

for k,v in test_dict.items(): # -> returns key vand value together separately
    print(k)
    print(v)

# truthy and falsy
if 0:
    print("python falsy approach supposedly not to run")

if 1:
    print("python truthy approach")

test = ""

if test:
    print("python truthy approach")
else:
    print("python falsy approach") # -> falsy run when 0 or containers are empty or variablle has no strings

if []:
    print("python truthy approach")
else:
    print("python falsy approach") # -> falsy run when 0 or containers are empty or variablle has no strings

if ['sample value']:
    print("python truthy approach")
else:
    print("python falsy approach") # -> falsy run when 0 or containers are empty or variablle has no strings

print("\n========== EXERCISE ==========\n")

e_list = [1,2,3,4,5]
for i in e_list:
    if i == 2:
        print("the value is 2")
    elif i == 5:
        test_val = 1
        count = 0
        while test_val:     # we can also run the while loop outside the fow since we're checking the last item
            print("last item", count + 1)
            count += 1
            if count == 6:
                test_val = 0
    else:
        print("the value is NOT 2")
