import numpy as np
import graf_mst
class Node():

    def __init__(self, input) -> None:
        #self.data1 = input[0]
        #self.data2 = input[1]
        self.key = input
    
    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

class Edge():
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2


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


    def insertEdge(self, vertex1, vertex2, egde = 1):
        if vertex1 not in self.node_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.node_list:
            self.insertVertex(vertex2)

        id1 = self.getVertexIdx(vertex1)
        id2 = self.getVertexIdx(vertex2)
        self.graph[id1].append((id2,egde))
        #self.graph[id2].append((id1,egde)) #nie bierzemy kierunkow pod uwage
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

    def primMST(self):
        intree = [0 for _ in range(len(self.graph))] #czy wierzchołek jest w drzewie
        distance = [float('inf') for _ in range(len(self.graph))] # minimalna waga krawędzi dla danego wierzchołka
        parent = [-1 for _i in range(len(self.graph))] #poprzedni wierzchołek w drzewie (do opisu krawędzi)

        result = ListGraph()
        for x in self.node_list:
            result.insertVertex(x)

        ver = 0
        while intree[ver] == 0:
          
            intree[ver] = 1
            for vertex, wage in self.neighbours(ver):
                if intree[vertex] == 0:
                   
                    if distance[vertex] > wage:
                       
                        parent[vertex] = ver
                        distance[vertex] = wage
       
            try:
                not_in_mst = [i for i, e in enumerate(intree) if e == 0]
                min_list = []
                for index,value in enumerate(distance):
                    if value != float('inf') and index in not_in_mst:
                        min_list.append(value)
                min_distance = min(min_list)
            except:
                min_distance = min(distance)
    
            for x in not_in_mst:
                if distance[x] == min_distance:
                    result.insertEdge(self.getVertex(parent[x]), self.getVertex(x), distance[x])
                    #result.insertEdge(self.getVertex(x),self.getVertex(parent[x]), distance[x],)
                    ver = x
                    break
        return result
                
            

def printGraph(g):
    n = g.order()
    print("------GRAPH------",n)
    for i in range(n):
        v = g.getVertex(i)
        print(v.key, end = " -> ")
        nbrs = g.neighbours(i)
        for (j, w) in nbrs:
            print(g.getVertex(j).key, w, end=";") #g.get_vertex(j).key j.key
        print()
    print("-------------------")


mst = ListGraph()

for el in graf_mst.graf:
    mst.insertEdge(Node(el[0]), Node(el[1]), el[2])
    mst.insertEdge(Node(el[1]), Node(el[0]), el[2])
m = mst.primMST()
printGraph(m)
