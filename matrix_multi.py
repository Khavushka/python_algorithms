# Matrix multiplication
# naive method: Multiplying two matricies using netsed loops

# 2x2 matrix 'X'

# X = [[1,2],
#      [3,4]]

# #  2x2 matrix 'Y'
# Y = [[2,3],
#      [3,4]]

# # 2x2 matrix of '0', which added to our answer, gives the answer
# result = [[0,0],
#          [0,0]]

# # iterate through rows of X
# for i in range(len(X)):
#     # iterate through columns of Y
#     for j in range(len(Y[0])):
#         # iterate through rows of Y
#         for k in range(len(Y)):
#             result[i][j] += X[i][k] * Y[k][j]

# for end in result:
#     print(end)

'''
German matrix multiplication 
'''
print("-------------")

# # Strassen algorithms

# import numpy as np

# x = np.array([[1,2],[2,3]])
# y = np.array([[2,3],[3,4]])

# def strassen_ite(x,y):
    
#     #splitting the matrixs into quadrants
#     a,b,c,d =x[0,0], x[0,1], x[1,0], x[1,1]
#     e,f,g,h =y[0,0], y[0,1], y[1,0], y[1,1]

#     #computing the 7 products - this is where the magic happen
#     p1 = a * (f - h)
#     p2 = (a + b) * h
#     p3 = (c + d) * e
#     p4 = d * (g - e)
#     p5 = (a + d) * (e + h)
#     p6 = (b - d) * (g + h)
#     p7 = (a - c) * (e + f)

#     # computing the values of the 4 quadrants of the final matrix c
#     c1 = (p5 + p4 -p2 + p6)
#     c2 = (p1 + p2)
#     c3 = (p3 +p4)
#     c4 = (p1 + p5 - p3 -p7)

#     return np.array([[c1,c2],[c3,c4]])

# print(strassen_ite(x, y))
print("-------------------------")
# recursive solution

import numpy as np

x = np.array([[1,2],[2,3]])
y = np.array([[2,3],[3,4]])

def split(matrix):
    row, col = matrix.shape
    row2, col2 = row // 2, col // 2
    return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen_recur(x,y):
    #splitting the matrixs into quadrants
    a,b,c,d = split(x)
    e,f,g,h = split(y)

    #computing the 7 products, recursively (p1, p2, ..., p7)
    p1 = strassen_recur(a, f - h)
    p2 = strassen_recur(a + b, h)
    p3 = strassen_recur(c + d, e)
    p4 = strassen_recur(d, g - e)
    p5 = strassen_recur(a + d, e + h)
    p6 = strassen_recur(b - d, g + h)
    p7 = strassen_recur(a - c, e + f)

    # computing the values of the 4 quadrants of the final matrix c
    c1 = (p5 + p4 -p2 + p6)
    c2 = (p1 + p2)
    c3 = (p3 +p4)
    c4 = (p1 + p5 - p3 -p7)

    #combining the 4 quadrants into a single matrix by stacking horizontally and vertically
    c = np.vstack((np.hstack((c1, c2)), np.hstack((c3, c4))))

    return c

print(strassen_recur(x, y))