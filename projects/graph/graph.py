"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        elif v1 in self.vertices:
            raise Exception(f"{v2} does not exist")
        elif v2 in self.vertices:
            raise Exception(f"{v1} does not exist")
        else:
            raise Exception(f"{v1} and {v2} do not exist")
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # initialise a queue data structure and append starting_vertex
        q = Queue()
        q.enqueue(starting_vertex)
        # initialise an empty set of visited vertices
        visited_vs = set()
        # while the queue is not empty, keep traversing
        while q.size():
            # dequeue the next vertex and store it in a variable
            v = q.dequeue()
            # if the vertex has not already been visited
            if v not in visited_vs:
                print(v)
                # add the vertex to the visited set
                visited_vs.add(v)
                # for each connected vertex in the vertex's set, add to the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # initialize a stack data structure and append starting_vertex
        s = Stack()
        s.push(starting_vertex)
        # initialize an empty set of visited vertices
        visited_vs = set()
        # while the stack is not empty, keep traversing
        while s.size():
            # pop the next vertex and store it as a variable
            v = s.pop()
            # if the vertex has not already been visited
            if v not in visited_vs:
                print(v)
                # add the vortex to the visited set
                visited_vs.add(v)
                # for each connected vertex in the vertex's set, add to the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # initialize a stack data structure and append starting_vertex
        stack = Stack()
        stack.push(starting_vertex)
        # initialize an empty set of visited vertices
        visited_vs = set()
        # nested recurse function has access to changing stack and visited set
        def recurse(stack, visited_vs):
            # pop the next vertex and store it as a variable
            v = stack.pop()
            # if the vertex has not already been visited
            if v not in visited_vs:
                print(v)
                # add the vortex to the visited set
                visited_vs.add(v)
                # for each connected node in the vertex's set, add to the stack
                for next_vertex in self.vertices[v]:
                    stack.push(next_vertex)
            if stack.size():
                recurse(stack, visited_vs)
        # invoke the recursive function with the stack and visited nodes
        recurse(stack, visited_vs)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # initialise a queue data structure and append starting_vertex as the first item in a list
        q = Queue()
        q.enqueue([starting_vertex])
        # initialise an empty set of visited vertices
        visited_vs = set()
        # while the queue is not empty, keep traversing
        while q.size():
            # dequeue the next path and store it in a variable
            p = q.dequeue()
            # grab the last vertex from the path
            v = p[len(p)  - 1]
            # if the vertex has not already been visited
            if v not in visited_vs:
                if v == destination_vertex:
                    return p
                # add the vertex to the visited set
                visited_vs.add(v)
                # for each connected vertex in the vertex's set, add a copy of the current path with it appended on the end
                for next_vertex in self.vertices[v]:
                    # make a copy of the current path
                    p_copy = p[:]
                    # append the next_vertex to the path and enqueue
                    p_copy.append(next_vertex)
                    q.enqueue(p_copy)
        # return False if the destination_vertex is not in  the graph
        return False
    
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # initialize a stack data structure and append starting_vertex
        s = Stack()
        s.push([starting_vertex])
        # initialize an empty set of visited vertices
        visited_vs = set()
        # while the stack is not empty, keep traversing
        while s.size():
            # pop the next path and store it as a variable
            p = s.pop()
            # grab the last vertex from the path
            v = p[len(p) - 1]
            # if the vertex has not already been visited
            if v not in visited_vs:
                if v == destination_vertex:
                    return p
                # add the vortex to the visited set
                visited_vs.add(v)
                # for each connected vertex in the vertex's set, add a copy of the current path with it appended on the end
                for next_vertex in self.vertices[v]:
                    # make a copy of the current path
                    p_copy = p[:]
                    # append the next_vertex to the path and push to the stack
                    p_copy.append(next_vertex)
                    s.push(p_copy)





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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
