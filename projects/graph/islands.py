# nodes are 1s
# edges: NSEW, not diagonals
# connected component: islands
# cyclic as undirected


# iterate through the matrix
# if it's a 1, then run DFT/BFT to find islands
# mark things as visited so don't double count.
"""
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

island_counter(islands) # returns 4"""


# translate the problem into terminology you've learned this week

# build your graph

# traverse your graph

from util import Stack, Queue

def getNeighbors(matrix, node):
    row = node[0]
    col = node[1]

    neighbouring_islands = []

    stepNorth = stepSouth = stepWest = stepEast = False

    if row > 0:
        stepNorth = row - 1
    if col > 0:
        stepWest = col - 1
    if row < len(matrix) - 1:
        stepSouth = row + 1
    if col < len(matrix) - 1:
        stepEast = col + 1

    if stepNorth is not False and matrix[stepNorth][col] == 1:
        neighboring_islands.append((stepNorth, col))

    if stepSouth is not False and matrix[stepSouth][col] == 1:
        neighboring_islands.append((stepSouth, col))

    if stepWest is not False and matrix[row][stepWest] == 1:
        neighboring_islands.append((row, stepWest))

    if stepEast is not False and matrix[row][stepEast] == 1:
        neighboring_islands.append((row, stepEast))

    return neighboring_islands

def dft(matrix, node, visited):
    stack = Stack()

    stack.push(node)

    while stack.size() > 0:
        current_node = stack.pop()

        if node not in visited:
            visited.add(node)
            neighbors = getNeighbors(matrix, node)
            for neighbor in neighbors:
                stack.push(neighbor)

def islands_counter(matrix):

    total_islands = 0
    visited = set()

    # iterate through the matrix
    for row in range(len(matrix)):
        for col in range(leng(matrix)):
            node = (row, col) # x, y coordinates

            # if it's a 1, then run DFT/BFT
            if node not in visited and matrix[row][col] == 1:
                visited.add(node)
                dft(matrix, node, visited)
                total_islands += 1

    return total_islands

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]
           [0, 0, 0, 0, 0]]

print(islands_counter(islands))







"""
    # create an entirely separate matrix
    # that keeps track of visited
    visited = []
    for i in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    # [[False, False, False, False, False],
    #   [False, False, False, False, False],
    #   [False, False, False, False, False],
    #   [False, False, False, False, False],
    #   [False, False, False, False, False]]

    # for all nodes:
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            # if node is not visited
            if not visited[row][col]:
                # if we hit a 1:
                if matrix[row][col] == 1:
                    # mark visited
                    # traverse all connected nodes, marking as visited
                    visited = dft(row, col, matrix, visited)
                    # increment visited count
                    island_count += 1

    return island_count

    def dft(row, col, matrix, visited):




        # do a df traversal
        # return an updated visited matrix with all connected components marked as
"""
