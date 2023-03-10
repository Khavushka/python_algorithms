# Matrix multiplication
# naive method: Multiplying two matricies using netsed loops

# 2x2 matrix 'X'

X = [[1,2],
     [3,4]]

#  2x2 matrix 'Y'
Y = [[2,3],
     [3,4]]

# 2x2 matrix of '0', which added to our answer, gives the answer
result = [[0,0],
         [0,0]]

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

for end in result:
    print(end)

'''
German matrix multiplication 
'''
