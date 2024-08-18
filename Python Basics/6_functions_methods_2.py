# create function
def print_5_times(test_to_print = "Loop", loop_number = 5, end_message = "End of loop"):
    count = 0
    while count < loop_number:
        print(test_to_print, count + 1)
        count += 1
    return end_message

# uysing the function
test = print_5_times(end_message="The operation has ended.")
print(test)
# print_5_times()

def hypotenuse_calculator(side_a = 1, side_b = 1):
    hypotenuse = ((side_a ** 2) + pow(side_b, 2)) ** .5
    return round(hypotenuse, 4)

print("Apply pythagorian theorem to calculate hypotenuse of a triange.")
side_a = int(input("Input side A:   "))
side_b = int(input("Input side B:   "))

res = hypotenuse_calculator(side_a, side_b)
print("The hypotenuse of", side_a, "and", side_b, "is", res)

print("\n========== EXERCISE ==========\n")

def shouter(message, number = 5):
    if number > 10:
        print("You are too loud!")
    else:
        count = 0
        # while count <= number:      # -> can use for i in range(number) instead
        #     print(message.upper())
        #     count += 1
        for i in range(number):
            print(message.upper())
    return "done"

res = shouter("hello world!", 3)
print(res)