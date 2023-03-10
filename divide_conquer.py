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
def merging