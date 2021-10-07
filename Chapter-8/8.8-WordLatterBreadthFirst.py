# from pythonds.graphs import Graph, Vertex
# from pythonds.basic import Queue

# def buildGraph(wordFile):
#     d = {}
#     g = Graph()
#     wfile = open(wordFile,'r')
#     # create buckets of words that differ by one letter
#     for line in wfile:
#         word = line[:-1]
#         for i in range(len(word)):
#             bucket = word[:i] + '_' + word[i+1:]
#             if bucket in d:
#                 d[bucket].append(word)
#             else:
#                 d[bucket] = [word]
#     # add vertices and edges for words in the same bucket
#     for bucket in d.keys():
#         for word1 in d[bucket]:
#             for word2 in d[bucket]:
#                 if word1 != word2:
#                     g.addEdge(word1,word2)
#     return g



# def bfs(g,start):
#     start.setDistance(0)
#     start.setPred(None)
#     vertQueue = Queue()
#     vertQueue.enqueue(start)
#     while (vertQueue.size() > 0):
#         currentVert = vertQueue.dequeue()
#         for nbr in currentVert.getConnections():
#             if (nbr.getColor() == 'white'):
#                 nbr.setColor('gray')
#                 nbr.setDistance(currentVert.getDistance() + 1)
#                 nbr.setPred(currentVert)
#                 vertQueue.enqueue(nbr)
#         currentVert.setColor('black')

# def traverse(y):
#     x = y
#     while (x.getPred()):
#         print(x.getId())
#         x = x.getPred()
#     print(x.getId())

# traverse(g.getVertex('sage'))

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue: #this means, while queue is not empty
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    # def dfs(self, vertex):
    #     visited = [vertex]
    #     stack = [vertex]
    #     while stack:
    #         popVertex = stack.pop()
    #         print(popVertex)
    #         for adjacentVertex in self.gdict[popVertex]:
    #             if adjacentVertex not in visited:
    #                 visited.append(adjacentVertex)
    #                 stack.append(adjacentVertex)
    



customDict = { "a" : ["b","c"],
            "b" : ["a", "d", "e"],
            "c" : ["a", "e"],
            "d" : ["b", "e", "f"],
            "e" : ["d", "f", "c"],
            "f" : ["d", "e"]
               }



g = Graph(customDict)
g.bfs("a")