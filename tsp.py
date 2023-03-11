# Traveling salesman problem
'''
Course of action:
- City 1: starting and ending point
- (n - 1)! Permitations
- Calculate cost of every permutation
- Return min cost
'''

from itertools import permutations
V = 4

def travel_salseman_problem(graph, s):
    #store all vertices
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = []
    next_permatation = permutations(vertex)

    for i in next_permatation:
        current_pathweight = 0

        k = s
        for j in i:
            current_pathweight += graph[k][j]
            #print(j, i, current_pathweight, graph[k][j])
            k = j
        current_pathweight += graph[k][s]
        min_path.append(current_pathweight)
        x = sorted(min_path)
    return x[0]

if __name__ == "__main__":
    #matrix representation of graph
    graph = [[0, 10, 15, 20],
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]
s = 0
print(travel_salseman_problem(graph, s))