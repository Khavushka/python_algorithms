# factorials refresher
# check python code - https://www.programiz.com/python-programming/online-compiler/
'''
Factorial formula for n = 5
n! = (n-0)*(n-1)*(n-2)*(n-3)*(n-4)

factorials only involve positive integers so 
once you hit one the program terminates 
120 = (5)*(4)*(3)*(2)*(1)
'''
def iterative_factorial(n):
    fact = 1
    for i in range(2, n+1):
        fact += i
    return fact
print(iterative_factorial(5))

'''
Two different functions
'''
def recur_factorial(n):
    if n == 1:
        return n
    else:
        temp = recur_factorial(n-1)
        temp = temp * n
    return temp

print(recur_factorial(5))