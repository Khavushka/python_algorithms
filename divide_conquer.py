A = [ -5, -23, 5, 0, 23, -6, 23, 67]
C = []

while A:
    minimum = A[0]
    for x in A:
        if x < minimum:
            minimum = x
    C.append(minimum)
    A.remove(minimum)

print(C)


# second solution merge
def merging(left, right):
    C = []
    while min(len(left), len(right)) > 0:
        if left[0] > right[0]:
            insert = right.pop(0)
            C.append(insert)
        elif left[0] <= right[0]:
            insert = left.pop(0)
            C.append(insert)
    if len(left) > 0:
        for i in left:
            C.append(i)
    if len(right) > 0:
        for i in right:
            C.append(i)
        return C
left = [2, 5, 6, 10]
right = [3, 4, 12, 20]
print(merging(left, right))