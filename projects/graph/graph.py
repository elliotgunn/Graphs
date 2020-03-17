"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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
        # adding another row
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """

        # first, check if v1 is in the dictionary, then access the value and add to it
        # v2 also has to be available vertex
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("ERROR: vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """

        # very easy: just return the set!
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.

        O(n): touched every node, edge, connection once
        """
        queue = Queue()
        visited = set()

        # put our starting node in line
        queue.enqueue(starting_vertex)

        # if our queue's not empty, we have more people to visit!
        while queue.size() > 0:
            # get the next node out of line
            current_node = queue.dequeue()

            # check if it has been visited
            if current_node not in visited:
                # if not, mark as visited
                visited.add(current_node)
                print(current_node)
                # and get its neighbours
                edges = self.get_neighbors(current_node)
                # put them in line to be visited
                for edge in edges:
                    queue.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        O(n): touched every node, edge, connection once
        """

        stack = Stack()
        visited = set()

        # put our starting node on top of stack
        stack.push(starting_vertex)

        # if our stack's not empty, we have more people to visit!
        while stack.size() > 0:
            # get the next node on top of stack
            current_node = stack.pop()

            # check if it has been visited
            if current_node not in visited:
                # if not, mark as visited
                visited.add(current_node)
                print(current_node)
                # and get its neighbours
                edges = self.get_neighbors(current_node)
                # stack them on the stack to be visited
                for edge in edges:
                    stack.push(edge)

    def dft_recursive(self, vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        visited.add(vertex)

        edges = self.get_neighbors(vertex)

        if len(edges) == 0:
            return

        else:
            for edge in edges:
                # Check if the node has been visited
                if edge not in visited:
                # If not...
                    # Mark it as visited^^^
                    # Call dft_recursive on each neighbor
                    self.dft_recursive(edge, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # make a queue
        queue = Queue()

        # make a set for visited
        visited = set()

        # enqueue a path to the starting_vertex
        queue.enqueue([starting_vertex])

        # while the queue isn't empty:
        while queue.size() > 0:
            # dequeue the next path
            current_path = queue.dequeue()
            # current node is the last thing in the path
            current_node = current_path[-1]

            # current_node is the last thing in the path
            # check if it's the target, aka the destination_vertex
            # if so, return the path,
            if current_node == destination_vertex:
                return current_path

            else:
                if current_node not in visited:
                    # else, mark as visited
                    visited.add(current_node)
                    # get neighbors
                    edges = self.get_neighbors(current_node)

                    # copy the path, add the neighbor to the copy
                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        # for each one, add a path to it to our queue
                        queue.enqueue(path_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        stack = Stack()

        # make a set for visited
        visited = set()

        # put our starting node on top of stack
        stack.push([starting_vertex])

        # while the stack isn't empty:
        while stack.size() > 0:
            # get the next node on top of stack
            current_path = stack.pop()
            # current node is the last thing in the path
            current_node = current_path[-1]

            # current_node is the last thing in the path
            # check if it's the target, aka the destination_vertex
            # if so, return the path,
            if current_node == destination_vertex:
                return current_path

            else:
                if current_node not in visited:
                    # else, mark as visited
                    visited.add(current_node)
                    # get neighbors
                    edges = self.get_neighbors(current_node)

                    # copy the path, add the neighbor to the copy
                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        # stack them on the stack to be visited
                        stack.push(path_copy)

    def dfs_recursive(self, starting_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
            if starting_vertex == destination_vertex:
                return path_copy
            for neighbor in self.get_neighbors(starting_vertex):
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                if new_path is not None:
                    return new_path
        return None





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
