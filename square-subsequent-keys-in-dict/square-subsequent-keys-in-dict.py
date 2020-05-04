'''
Question:

With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that
is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

'''



# _____________________________________________________________________________________________________


def squaredict(num):

# Creating Empty dictionary
    dict = {}
#  iterate the following range and updating empty dicttionary with key:value

    for i in range(1,num+1):
        dict.update({i:i*i})
# print the result
    print(dict)

# Getting integer from user, then calling the function with the var as argument

userinput = int(input("Please Enter a number:"))
squaredict(userinput)

# _____________________________________________________________________________________________________



# Alternative solution - using dictionary comprehension

def squareindict(number):

    d = {i:i*i for i in range(1,number+1)}
    print(d)

# Getting integer from user, then calling the function with the var as argument

userinput2 = int(input("Please Enter a number:"))
squareindict(userinput2)

# _____________________________________________________________________________________________________


