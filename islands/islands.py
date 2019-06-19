from graph import Graph
from util import Stack

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
#            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
#            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
#            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
#            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
#            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
#            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
#            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
#            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

def get_neighbours(island_set_index, square_index):
    neighbours = []
    cur_island_set = islands[island_set_index]
    # get anything from the left
    if square_index != 0 and cur_island_set[square_index - 1] == 1:
        neighbours.append((island_set_index, square_index - 1))
    # get anything from the right
    if square_index != len(cur_island_set) - 1 and cur_island_set[square_index + 1] == 1:
        neighbours.append((island_set_index, square_index + 1))
    # get anything from below
    if island_set_index != len(islands) - 1 and islands[island_set_index + 1][square_index] == 1:
        neighbours.append((island_set_index + 1, square_index))
    # get anything from above
    if island_set_index != 0 and islands[island_set_index - 1][square_index] == 1:
        neighbours.append((island_set_index - 1, square_index))
    return neighbours

def island_dft(g):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    # initialize a list of ilsnads
    islands = []
    # initialize an empty set of visited keys
    visited_keys = set()
    # loop over coordinate keys in the graph vertices
    for key in g.vertices:
        # check that the key has not already been traversed in a previous traversal
        if key not in visited_keys:
            # intiialize an empty set to hole the island coordinates
            island = set()
            # initialize a stack data structure and append starting_vertex
            s = Stack()
            s.push((key))
            # while the stack is not empty, keep traversing
            while s.size():
                # pop the next vertex and store it as a variable
                v = s.pop()
                # if the vertex has not already been visited
                if v not in island:
                    # add the vortex to the island and visited_keys set
                    visited_keys.add(v)
                    island.add(v)
                    # for each connected vertex in the vertex's set, add to the stack
                    for next_vertex in g.vertices[v]:
                        s.push(next_vertex)
            # when the while loop is finished add the contents of island to the islands array
            islands.append(island)
    # return the length of the islands array
    return len(islands)

def island_counter(islands):
    # instantiate a graph with vertices of legitemate coordinates (equal to 1)
    g = Graph()
    for i in range(0, len(islands)):
        for j in range (0, len(islands[0])):
            if islands[j][i] == 1:
                g.add_vertex((j, i))
    # add edges to the graph by getting all adjoining coordinates with a value of 1
    for coordinates in g.vertices:
        neighbours = get_neighbours(coordinates[0], coordinates[1])
        for neighbour in neighbours:
            g.add_edge(coordinates, neighbour)
    # run the depth first traversal, passing in the graph so that the keys can be mapped over
    return island_dft(g)


print(island_counter(islands)) # returns 4