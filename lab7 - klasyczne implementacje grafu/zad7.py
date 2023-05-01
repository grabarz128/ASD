import polska

class Node():

    def __init__(self, input) -> None:
        self.data1 = input[0]
        self.data2 = input[1]
        self.key = input[2]
    
    def __eq__(self, other):
        self.key == other.key

    def __hash__(self):
        return hash(self.key)

class Edge():
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

class MatrixGraph():

    def __init__(self):
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

        if self.isEmpty():
            self.graph.append([0])
        else:
            for row in self.graph:
                row.append(0)
            self.graph.append([0 for _ in range(len(self.graph[0]))])

    def insertEdge(self, vertex1, vertex2, egde = 1):
        if vertex1 not in self.node_list:
            self.insertVertex(vertex1)
        if vertex2 not in self.node_list:
            self.insertVertex(vertex2)

        id1 = self.getVertexIdx(vertex1)
        id2 = self.getVertexIdx(vertex2)

        self.graph[id1][id2] = 1 #tu można wstawić wage krawędzi
        #self.graph[id2][id1] = 1  bo nie bierzemy kierunuków pod uwage
        self.g_size +=1

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
            rows.pop(idV)
        
    def deleteEdge(self, vertex1, vertex2):
        if vertex1 in self.node_list and vertex2 in self.node_list:
            id1 = self.getVertexIdx(vertex1)
            id2 = self.getVertexIdx(vertex2)
            self.graph[id1][id2] = 0 #tu można wstawić wage krawędzi
            self.graph[id2][id1] = 0 # bo nie bierzemy kierunuków pod uwage
            self.g_size -=1
        else:
            raise ValueError()

    def getVertexIdx(self, vertex):
        return self.node_id[vertex]

    def getVertex(self,vertex_idx):
        for node, value in self.node_id.items():
            if value == vertex_idx:
                return node

    def order(self):
        return len(self.graph[0]) 

    def size(self):
        return self.g_size

    def edges(self):
        result = []
        for rows in range(len(self.graph)):
            for cols in range(len(self.graph)):
                if self.graph[rows][cols] == 1:
                    result.append((self.getVertex(rows).key, self.getVertex(cols).key))
        return result

    def __str__(self):
        result =''
        for line in self.graph:
            result += str(line) + "\n"
        return result
        
    def neighboursIdx(self,vertex_idx):
        result = []
        for cols in self.graph:
            if self.graph[vertex_idx][cols] == 1:
                result.append(cols)
        return result



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
        self.graph[id1].append(id2)
        #self.graph[id1].append(id2) nie bierzemy kierunkow pod uwage
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
        return len(self.graph[0]) 

    def size(self):
        return self.g_size

    def edges(self):
        result = []
        for rows in range(len(self.graph)):
            for cols in self.graph[rows]:
                result.append((self.getVertex(rows).key, self.getVertex(cols).key))
        return result
    
    def neigboursIdx(self,vertex_id):
        result = []
        for i in range(len(self.graph)):
            for el in self.graph[i]:
                if el == vertex_id:
                    result.append(i)
        return result

    def __str__(self):
        result =''
        for line in self.graph:
            result += str(line) + "\n"
        return result


#test 1
graph1 = MatrixGraph()
polska_nodes = {}
for el in polska.polska:
    polska_nodes[el[2]] = Node(el)
for key1, key2 in polska.graf:
    graph1.insertEdge(polska_nodes[key1], polska_nodes[key2], 1)

graph1.deleteVertex(polska_nodes['K'])
graph1.deleteEdge(polska_nodes['E'], polska_nodes['W'])

polska.draw_map(graph1.edges())

#test 2
graph2 = ListGraph()


for key1, key2 in polska.graf:
    graph2.insertEdge(polska_nodes[key1], polska_nodes[key2], 1)

graph2.deleteVertex(polska_nodes['K'])
graph2.deleteEdge(polska_nodes['E'], polska_nodes['W'])
graph2.deleteEdge(polska_nodes['W'], polska_nodes['E'])

polska.draw_map(graph2.edges())