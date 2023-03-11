# Palindromic Matrix Paths

def paths(m, n):
    row = [1] * n
    print(row)
    for i in range(m-1):
        newRow = [1] * n
        for j in range(n - 2, -1 -1):
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
        print(row)
    return row[0]
print(paths(3, 3))

print("\n================================")

import itertools
a = [['a', 'a', 'a'],
     ['b', 'b', 'b'],
     ['a', 'b', 'a']]
x = list(itertools.product(*a))
# print(x)

p_1 = []
for i in x:
    y = "".join(i)
    p_1.append(y)
# print(p_1)
# print(set(p_1))

def isPalin_2(p_1):
    p_2 = []
    for x in set(p_1):
        if x == x[::-1]:
            p_2.append(x)
    return p_2
print(isPalin_2(p_1))

print("\n================================")

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
def palindromic_path(string, a, i, j, m, n):
    if j < m -1 or i < n - 1:
        if i < n - 1:
            palindromic_path(string + a[i][j], a, i + 1, j, m, n)
        if j < m -1:
            palindromic_path(string + a[i][j], a, i, j + 1, m, n)
    else:
        string = string + a[n - 1][m - 1]
        if is_palindrome(string):
            print(string)
str = ""
print(palindromic_path(str, a, 0, 0, 3, 3))
    