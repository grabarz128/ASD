import numpy as np
from copy import deepcopy

class Node():

    def __init__(self, input) -> None:
        self.key = input
    
    def __eq__(self, other):
        return self.key == other.key

    def __hash__(self):
        return hash(self.key)

class Edge():
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

class MatrixGraph():

    def __init__(self,input=None):
        self.graph = []
        self.node_list = []
        self.node_id = {}
        self.g_size = 0
        if input is not None:
            for el in input:
                self.insertEdge(el[0],el[1],el[2])


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
        self.graph[id2][id1] = 1 
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
            self.graph[id2][id1] = 0 #
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

    def getMatrix(self):
        return self.graph

def isomorphism(g, p, m):
    x = m @ np.transpose(m @ g)
    if (x == p).all():
        return True
    else:
        return False

def ullmann(g,p):
    M = np.zeros((p.shape[0], g.shape[0]))
    result_matrices = []
    columns = [False for _ in range(M.shape[1])]
    def ullman_rec(row,M,recursion = 0):
        recursion += 1
        if row == len(M):
            if isomorphism(g,p,M):
                result_matrices.append(M)
                return recursion
            else:
                return recursion
        for c in range(len(M[0])):
            if columns[c] == False:
                columns[c] = True
                M[row, :] = 0
                M[row, c] = 1
                recursion = ullman_rec(row+1,deepcopy(M),recursion)
                columns[c] = False
        return recursion
    rec = ullman_rec(0,M)
    # for i in result_matrices:
    #     print("\n",i)
    return len(result_matrices), rec


def ullmann2(g,p):
    M0 = np.zeros((p.shape[0], g.shape[0]))
    M = np.zeros((p.shape[0], g.shape[0]))
    
    for i in range(p.shape[0]):
        for j in range(g.shape[0]):
            if np.count_nonzero(p[i] == 1) <= np.count_nonzero(g[j] == 1):
                M0[i][j] = 1

    result_matrices = []
    columns = [False for _ in range(M.shape[1])]
    
    def ullman_rec2(row,M,M0,recursion = 0,columns = None):
        recursion += 1
        if row == len(M):
            if isomorphism(g,p,M):
                result_matrices.append(M)
                return recursion
            else:
                return recursion
        for c in range(len(M[0])):
            if columns[c] == False and M0[row][c] == 1:
                columns[c] = True
                M[row, :] = 0
                M[row, c] = 1
                recursion = ullman_rec2(row+1,deepcopy(M),M0,recursion,columns)
                columns[c] = False
        return recursion
    rec = ullman_rec2(0,M,M0,0,columns)
    return len(result_matrices), rec

def prune(g,p,m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m[i][j] == 1:
                neigh_p = []
                neigh_g = []
                for k in range(p.shape[0]):
                    if p[i][k] == 1:
                        neigh_p.append(k)
                for k in range(g.shape[0]):
                    if g[j][k] == 1:
                        neigh_g.append(k)
                
                for x in neigh_p:
                    db_break = True
                    for y in neigh_g:
                        if m[x][y] != 1:
                            db_break = False
                            break
                    if db_break:
                        break
                else:
                    m[i][j] = 0
    

                   


def ullmann3(g,p):
    M0 = np.zeros((p.shape[0], g.shape[0]))
    M = np.zeros((p.shape[0], g.shape[0]))
    
    for i in range(p.shape[0]):
        for j in range(g.shape[0]):
            if np.count_nonzero(p[i] == 1) <= np.count_nonzero(g[j] == 1):
                M0[i][j] = 1

    result_matrices = []
    columns = [False for _ in range(M.shape[1])]
    
    def ullman_rec3(row,M,M0,recursion = 0):
        recursion += 1
        if row == len(M):
            if isomorphism(g,p,M):
                result_matrices.append(M)
                return recursion
            else:
                return recursion
        pr_m = deepcopy(M)
        prune(g,p,pr_m)
        for c in range(len(M[0])):
            if columns[c] == False and M0[row][c] == 1:
                columns[c] = True
                pr_m[row, :] = 0
                pr_m[row, c] = 1
                recursion = ullman_rec3(row+1,deepcopy(pr_m),M0,recursion)
                columns[c] = False
        return recursion
    rec = ullman_rec3(0,M,M0)
    return len(result_matrices), rec




graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

ulmannG = MatrixGraph(graph_G)


ulmannP = MatrixGraph(graph_P)

G = np.array(ulmannG.getMatrix())
P = np.array(ulmannP.getMatrix())
print(ullmann(G,P))
print(ullmann2(G,P))
print(ullmann3(G,P))