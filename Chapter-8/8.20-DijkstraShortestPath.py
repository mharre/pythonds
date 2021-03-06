from pythonds.graphs import PriorityQueue, Graph, Vertex
from collections import defaultdict

def dijkstra(aGraph,start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                    + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newDist)

g = Graph()
g.addVertex(0) #U
g.addVertex(1) #V
g.addVertex(2) #W
g.addVertex(3) #X
g.addVertex(4) #Y
g.addVertex(5) #Z
g.addEdge(0, 1, 2)
g.addEdge(0, 2, 5)
g.addEdge(0, 3, 1)
g.addEdge(1, 0, 2)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(2, 1, 3)
g.addEdge(2, 0, 5)
g.addEdge(2, 3, 3)
g.addEdge(2, 4, 1)
g.addEdge(2, 5, 5)
g.addEdge(3, 0, 1)
g.addEdge(3, 1, 2)
g.addEdge(3, 2, 3)
g.addEdge(3, 4, 1)
g.addEdge(4, 3, 1)
g.addEdge(4, 2, 1)
g.addEdge(4, 5, 1)
g.addEdge(5, 2, 5)
g.addEdge(5, 4, 1)

for v in g:
    for w in v.getConnections():
        print(f'( {(v.getId())} , {(w.getId())} )')

# class Graph:
#     def __init__(self):
#         self.nodes = set()
#         self.edges = defaultdict(list)
#         self.distances = {}
    
#     def addNode(self,value):
#         self.nodes.add(value)
    
#     def addEdge(self, fromNode, toNode, distance):
#         self.edges[fromNode].append(toNode)
#         self.distances[(fromNode, toNode)] = distance


# def dijkstra(graph, initial):
#     visited = {initial : 0}
#     path = defaultdict(list)

#     nodes = set(graph.nodes)

#     while nodes:
#         minNode = None
#         for node in nodes:
#             if node in visited:
#                 if minNode is None:
#                     minNode = node
#                 elif visited[node] < visited[minNode]:
#                     minNode = node
#         if minNode is None:
#             break

#         nodes.remove(minNode)
#         currentWeight = visited[minNode]

#         for edge in graph.edges[minNode]:
#             weight = currentWeight + graph.distances[(minNode, edge)]
#             if edge not in visited or weight < visited[edge]:
#                 visited[edge] = weight
#                 path[edge].append(minNode)
    
#     return visited, path

# customGraph = Graph()
# customGraph.addNode("A")
# customGraph.addNode("B")
# customGraph.addNode("C")
# customGraph.addNode("D")
# customGraph.addNode("E")
# customGraph.addNode("F")
# customGraph.addNode("G")
# customGraph.addEdge("A", "B", 2)
# customGraph.addEdge("A", "C", 5)
# customGraph.addEdge("B", "C", 6)
# customGraph.addEdge("B", "D", 1)
# customGraph.addEdge("B", "E", 3)
# customGraph.addEdge("C", "F", 8)
# customGraph.addEdge("D", "E", 4)
# customGraph.addEdge("E", "G", 9)
# customGraph.addEdge("F", "G", 7)

# print(dijkstra(customGraph, "A"))

#({'A': 0, 'B': 2, 'C': 5, 'D': 3, 'E': 5, 'G': 14, 'F': 13},
# defaultdict(<class 'list'>, {'B': ['A'],
#                              'C': ['A'],
#                              'D': ['B'],
#                              'E': ['B'],
#                              'G': ['E'],
#                              'F': ['C']}))
# slightly more organized print statement, explanation:
#line 80, a --> b would be 2, a --> c would be 5, a --> e would be 5 etc
#81-86, a is starting point, shortested path to 'D' we would need A, B, D. Shortest path to 'G' we would need A, B, E, G etc