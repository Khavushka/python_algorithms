# Permutations (перестановка)
'''
Перестановка в Python - это расположение множества, в котором порядок имеет значение. 
Модуль Python itertools предоставляет встроенный метод permutation() для поиска перестановки.
Источник: https://pythonpip.ru/examples/perestanovka-i-kombinatsiya-v-python-primery
'''

# Permitation is when you take set of elements and find 
# all different variations

# * Remember strings are immutable

def permute(string, pocket = ""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together,letter + pocket)

print(permute("ABCD", ""))

# N Queens Promlem
# Real world example of permutations
