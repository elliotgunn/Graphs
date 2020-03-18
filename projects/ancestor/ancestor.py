# 3 step approach

# nodes: parents & children
# algorithm: bft, farthest path
#

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):

        # for example:
        # self.vertices = {"A": set("B"), "B": set()
        #                  "C": set(), "D": set()}
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # this will ensure not overwriting
        if vertex_id not in self.vertices:
            # adding another row
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph (because it's parent-child).
        """

        # first, check if v1 is in the dictionary, then access the value and add to it
        # v2 also has to be available vertex
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: vertex does not exist")

# ancestors:
## [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):

    # build our graph
    graph = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)

        # add directed edge between parent, child
        graph.add_edge(child, parent)

    # BFS
    queue = Queue()
    queue.enqueue([starting_node])

    longest_path_length = 1
    earliest_ancestor = -1

    ## while queue isn't empty, dequeue the next path
    while queue.size() > 0:
        path = queue.dequeue()

        # current node is last thing in path
        current_node = path[-1]


        # case of 8, where you have two parents equidistant
        if len(path) >= longest_path_length:
            # arbitrarily decide the earliest ancestor is the smaller one
            if current_node < earliest_ancestor:
                longest_path_length = len(path)
                earliest_ancestor = current_node

        # update length of path so far
        # update earliest ancestor so far
        if len(path) > longest_path_length:
            longest_path_length = len(path)
            earliest_ancestor = current_node

        # get neighbours
        neighbors = graph.vertices[current_node]
        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            queue.enqueue(path_copy)
    print(path)
    return earliest_ancestor
