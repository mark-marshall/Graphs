from graph import Graph

# the nodes of the graph will be each member of the family
# the edges will be a list of parents for each node

family_member = 6
family = [[1,3], [2,3], [3,6], [5,6], [5,7], [4,5], [4,8], [8,9], [11,8], [10,1]]

def getEarliestAncestor(family_member, family):
    g = Graph()
    # add all femily member vertices to the graph
    all_members = []
    for pair in family:
        if pair[0] not in all_members:
            all_members.append(pair[0])
    print(all_members)

getEarliestAncestor(family_member, family)