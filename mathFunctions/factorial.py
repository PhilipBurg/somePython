import functools
#  functools import for the reduce() function

# empty list, which will store faculty of a number given by the user
list = []
user_number = int(input("Please enter a number: "))
for i in range(user_number, 0, -1):
    list.append(i)
factorial = functools.reduce(lambda x, y: x * y,list)
print(f"The factorial of your number {user_number} is: {factorial} ")