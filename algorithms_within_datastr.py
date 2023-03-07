# Algorithms  within Data Structure

'''
In basic section we're going to cover:
- Linear search
- Binary search
- Bubble sort
- Insertion sort
'''

# Linear search
def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i;

arr = [2, 4, 5, 6, 10, 16, 22]
target = 22

print(search(arr, target))

# Binary search
def binary_search(arr1, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if arr1[mid] < target:
            start = mid + 1
        elif arr1[mid] > target:
            end = mid -1
        else:
            return mid

arr1 = [2, 4, 5, 6, 10, 16, 22]
target = 2

result = binary_search(arr1, 0, len(arr1) - 1, target)
# print(result)

if result != -1:
    print('Element is present at index %d' % result)
else:
    print('Element is not present in array')

# Bubble sort
# The bigger element to the top 
def bubbleSort(element):
    iterations = 0
    for i in range(len(element)):
        for j in range(len(element)-i-1):
            iterations += 1
            if element[j] > element[j+1]:
                element[j], element[j+1] = element[j], element[j+1]
    return element, iterations
element = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(bubbleSort(element))