
import numpy as np

class Node():

    def __init__(self, input) -> None:
        self.key = input
    
    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

class Edge():
    def __init__(self, capacity, isResidual = False):
        self.capacity = capacity #pojemnosc
        self.isResidual = isResidual
        self.residual = capacity #przeplyw resztowy
        self.flow = 0 # poczatkowy przeplyw
    
    def __repr__(self):
            return str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)


class ListGraph():

    def __init__(self) -> None:
        self.graph = []
        self.node_list = []
        self.node_id = {}
        self.g_size = 0

    def isEmpty(self):
        if len(self.graph) == 0:
            return True
        else:
            return False        

    def insertVertex(self,vertex):
        self.node_list.append(vertex)
        self.node_id[vertex] = len(self.node_list)-1
        self.graph.append([])


    def insertEdge(self, vertex1, vertex2, egde: Edge):
        if vertex1 not in self.node_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.node_list:
            self.insertVertex(vertex2)

        id1 = self.getVertexIdx(vertex1)
        id2 = self.getVertexIdx(vertex2)
        self.graph[id1].append((id2,egde))
        self.graph[id2].append((id1,Edge(0,True))) #krawedz resiudalna
        self.g_size += 1 

    def normalize_dict(self):
        for i in range(len(self.node_list)):
            self.node_id[self.node_list[i]] = i

    def deleteVertex(self, vertex):
        idV = self.getVertexIdx(vertex)
        self.node_list.remove(vertex)
        self.node_id.pop(vertex)
        self.normalize_dict()
        self.graph.pop(idV)
        for rows in self.graph:
            if idV in rows:
                rows.remove(idV)
            for el in rows:
                if el > idV:
                    el -= 1

    def deleteEdge(self, vertex1, vertex2):
        id1 = self.getVertexIdx(vertex1)
        id2 = self.getVertexIdx(vertex2)
        self.graph[id1].remove(id2)
        self.g_size -= 1

    def getVertexIdx(self,vertex):
        return self.node_id[vertex]

    def getVertex(self,vertex_idx):
        for node, value in self.node_id.items():
                if value == vertex_idx:
                    return node

    def order(self):
        return len(self.graph) 

    def size(self):
        return self.g_size

    def edges(self):
        result = []
        for rows in range(len(self.graph)):
            for cols in self.graph[rows]:
                result.append((self.getVertex(rows).key, self.getVertex(cols).key))
                result.append((self.getVertex(rows).key, self.getVertex(cols).key))
        return result
    
    def neigboursIdx(self,vertex_id):
        result = []
        for i in range(len(self.graph)):
            for el in self.graph[i]:
                if el[0] == vertex_id:
                    result.append(i)
        return result
    
    def neighbours(self, v_idx):
        return self.graph[v_idx]
    
    def __str__(self):
        result =''
        for line in self.graph:
            result += str(line) + "\n"
        return result
                
    def bfs(self, start):
        visited = [start]
        parent = {start: None}
        while visited:
            w = visited.pop()
            for nei, edg in self.neighbours(w):
                if nei not in parent.keys() and edg.residual > 0:
                    visited.insert(0, nei)
                    parent[nei] = w
        return parent

    def count_min(self, start, end, parent: dict):
        min_flow = float('inf')
        vertex = end 
        if end not in parent.keys():
            return 0
        while vertex != start:
            par = parent[vertex]
            for el in self.graph[par]:
                if el[0] == vertex and el[1].isResidual is False:
                    if el[1].residual < min_flow:
                        min_flow = el[1].residual
                continue
            vertex = par
        return min_flow

    def augmentation(self,start, end, parent: dict, min_flow):
        vertex = end 
        if end not in parent.keys():
            return 0
        while vertex != start:
            par = parent[vertex]

            for el in self.graph[par]:
                if el[0] == vertex and el[1].isResidual is False:
                    el[1].flow +=min_flow
                    el[1].residual -= min_flow
                continue

            for el in self.graph[vertex]:
                if el[0] == par and el[1].isResidual is True:
                    el[1].residual += min_flow
                continue

            vertex = par

    def ford_fulkerson(self,start, end):
        result = 0
        parent = self.bfs(start)
        min_flow = self.count_min(start,end,parent)
        
        while min_flow > 0:
            self.augmentation(start, end, parent, min_flow)
            parent = self.bfs(start)
            min_flow = self.count_min(start, end, parent)
        
        for i in range(len(self.graph)):
            for el in self.graph[i]:
                if el[0] == end and el[1].isResidual is False:
                    result += el[1].flow
        return result

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v.key, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j).key, w, end=";") 
        print()
    print("-------------------")


graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
graf_3 = [('s', 'a', 8), ('s', 'd', 3), ('a', 'b', 9), ('b', 'd', 7), ('b', 't', 2), ('c', 't', 5), ('d', 'b', 7), ('d', 'c', 4)]

end_list = [2,4,6,4]
graphs = [graf_0,graf_1,graf_2,graf_3]

for i, el in enumerate(graphs):
    res = ListGraph()
    for elem in el:
        res.insertEdge(Node(elem[0]), Node(elem[1]), Edge(elem[2], False))
    print(res.ford_fulkerson(0,end_list[i]))
    printGraph(res)
    del res





