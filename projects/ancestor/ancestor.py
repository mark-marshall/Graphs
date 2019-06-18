from graph import Graph
from util import Stack

# the nodes of the graph will be each member of the family
# the edges will be a list of parents for each node
family_member = 6
family = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [8,9], [11,8], [10,1]]

def getEarliestAncestor(family_member, family):
    g = Graph()

    # add all femily member vertices to the graph
    all_members = []
    for pair in family:
        for ind in pair:
            if ind not in all_members:
                all_members.append(ind)
                g.add_vertex(ind)

    # take the pairs and add all parents to each child vertice
    for pair in family:
        g.add_edge(pair[1], pair[0])
    
    return ancestor_search(family_member, g)
    # perform a search that starts at the child and keeps moving through parents until it gets to a vertex with no parents
    # it will finish with a path for that search showing all the nodes it took
    # the search will then return the final vertex in the longest path and if tied will return the vertex with smallest id

def ancestor_search(family_member, family_graph):
    # initialize a stack data structure and append starting_vertex
    s = Stack()
    s.push([family_member])
    # initialize an empty set of visited vertices
    visited_vs = set()
    # initialize a compete paths list
    complete_paths = []
    
    # while the stack is not empty, keep traversing
    while s.size():
        # pop the next path and store it as a variable
        p = s.pop()
        # grab the last vertex from the path
        v = p[len(p) - 1]
        # if the vertex has not already been visited
        if v not in visited_vs:
            if len(family_graph.vertices[v]) == 0:
                complete_paths.append(p)
            # add the vortex to the visited set
            visited_vs.add(v)
            # for each connected vertex in the vertex's set, add a copy of the current path with it appended on the end
            for next_vertex in family_graph.vertices[v]:
                # make a copy of the current path
                p_copy = p[:]
                # append the next_vertex to the path and push to the stack
                p_copy.append(next_vertex)
                s.push(p_copy)

    # find the longest path
    longest_path = complete_paths[0]
    for path in complete_paths
        # replace the cur longest_path if given paath is longer
        if len(path) > len(longest_path):
            longest_path = path
        # also replace the cur longest_path if given path is same lenght but final ID is smaller
        if (len(path) == len(longest_path)) and (path[-1] < longest_path[-1]):
            longest_path = path
    # return the final ancestor in tthe longest path
    return longest_path[-1]

print(getEarliestAncestor(family_member, family))