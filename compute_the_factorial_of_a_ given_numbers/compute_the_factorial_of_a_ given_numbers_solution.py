'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320


'''
############################################################################################################

from functools import reduce

def fact(num):

# Creating 2 empty lists

    subsequent_numbers_list = []
    factorial_list = []

# Checking that input from user is bigger than 0 , populating the subsequent_numbers_list and
# incrementing 1 from number each time

    while num > 0:
        subsequent_numbers_list.append(num)
        num = num - 1

# multiplying every items in list in themselves

    a = (reduce(lambda x, y: x * y, (subsequent_numbers_list)))
    print(a)

# Calling "fact" function with argument 8

fact(8)



############################################################################################################


# 2nd approach -  little bit more efficient

# Recuresivly calling the function and substracting 1 from x each time
def fact2(x):
    if x == 0:
        return 1
    return x * fact2(x - 1)

# Getting number from user

x=int(input("Enter a number:"))
print(fact2(x))













