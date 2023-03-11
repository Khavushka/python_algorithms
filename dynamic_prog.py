# Dynamic Programming

'''
Python  is strongly typed as the interpreter keeps
track of all variables types. Its's also very dymanic as it rarely
uses what it knows to limit variable usage
- breaking the problem down
- solving recursively (рекурсивно)
- optimal solutions to construct optimal solutions

In dynamic progaramming there are three basic methods:
- recursion
- top-down(w/memorization)
- bottom-up(w/tabulation)
'''

# Ugly-number
# Recursive function for successive divisions
def succesive_div(x, y):
    while x % y == 0:
        x = x // y
    return x

print(succesive_div(1,4))

# Function for checking if a number is ugly or not
def ugly_check(num):
    num = succesive_div(num, 2)
    num = succesive_div(num, 3)
    num = succesive_div(num, 5)
    if num == 1:
        return True
    else:
        return False
print(ugly_check(6))

# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15

# Function for finding the nth ugly number
def nth_ugly(n):
    i = 1
    # ugly number count
    counter = 1

    # Looping through all integers until ugly count becomes n
    while n > counter:
        i += 1
        if ugly_check(i):
            counter += 1
    return i
no = nth_ugly(15)
print("15th ugly number is:", no)