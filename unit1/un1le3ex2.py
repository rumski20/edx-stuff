# unit 1 | lecture 3 | exercise 2
# graph - student position problem

from handouts.lecture3Segment2 import *
import functools

# code from excercise
nodes = []
nodes.append(Node("ABC"))  # nodes[0]
nodes.append(Node("ACB"))  # nodes[1]
nodes.append(Node("BAC"))  # nodes[2]
nodes.append(Node("BCA"))  # nodes[3]
nodes.append(Node("CAB"))  # nodes[4]
nodes.append(Node("CBA"))  # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

# prompt: Add the appropriate edges to the graph.
# g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
# g.addEdge(Edge(g.getNode('ABC'), g.getNode('BAC')))
# g.addEdge(Edge(g.getNode('ACB'), g.getNode('CAB')))
# g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
# g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
# g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
# g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))
# g.addEdge(Edge(g.getNode('ABC'), g.getNode('ACB')))



# def swapfunc(x, y, z):
#     if "".join([x, y, z]) in nodestrings: return [x, y, z]

nodestrings = [n.getName() for n in nodes]

# ref: http://stackoverflow.com/a/25954716/6072959
def swap(s, i, j):
    return ''.join((s[:i], s[j], s[i + 1:j], s[i], s[j + 1:]))


swappable = []
for node in nodes:
    nodestr = node.getName()
    onetwoswap = swap(nodestr, 0, 1)
    if onetwoswap in nodestrings:
        swappable.append((nodestr, onetwoswap))
    twothreeswap = swap(nodestr, 1, 2)
    if twothreeswap in nodestrings:
        swappable.append((nodestr, twothreeswap))

# add edges
for e in swappable:
    g.addEdge(Edge(g.getNode(e[0]), g.getNode(e[1])))
        # g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
        # swappable = functools.reduce(swapfunc, list(node.getName()))

print(g)
