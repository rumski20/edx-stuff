# unit 1 | lecture 3 | exercise 4
# depth first search - student position problem

from handouts.lecture3segment3 import *


def build_student_graph(graphType):
    nodes = []
    nodes.append(Node("ABC"))  # nodes[0]
    nodes.append(Node("ACB"))  # nodes[1]
    nodes.append(Node("BAC"))  # nodes[2]
    nodes.append(Node("BCA"))  # nodes[3]
    nodes.append(Node("CAB"))  # nodes[4]
    nodes.append(Node("CBA"))  # nodes[5]

    g = graphType()
    for n in nodes:
        g.addNode(n)

    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[4]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[4], nodes[5]))
    return g


def shortest_path(source, destination):
    g = build_student_graph(Graph)
    sp = DFS(g, g.getNode(source), g.getNode(destination), [], None,
             toPrint=True)
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)


# print(build_student_graph(Digraph))
shortest_path('BCA', 'ACB')
