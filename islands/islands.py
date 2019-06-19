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
        neighbours.append((square_index - 1, island_set_index))
    # get anything from the right
    if square_index != len(cur_island_set) - 1 and cur_island_set[square_index + 1] == 1:
        neighbours.append((square_index + 1, island_set_index))
    # get anything from below
    if island_set_index != len(islands) - 1 and islands[island_set_index + 1][square_index] == 1:
        neighbours.append((square_index, island_set_index + 1))
    # get anything from above
    if island_set_index != 0 and islands[island_set_index - 1][square_index] == 1:
        neighbours.append((square_index, island_set_index - 1))
    return neighbours

def island_counter(islands):
    g = Graph()
    for i in range(0, len(islands)):
        for j in range (0, len(islands[0])):
            if islands[j][i] == 1:
                g.add_vertex((i, j))
                
    for coordinates in g.vertices:
        neighbours = get_neighbours(coordinates[0], coordinates[1])
        for neighbour in neighbours:
            g.add_edge(coordinates, neighbour)

    return (g.vertices)



print(island_counter(islands)) # returns 4