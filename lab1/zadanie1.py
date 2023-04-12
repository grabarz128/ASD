class create_matrix:
    
    #declaration of matrix depending on given arguments
    def __init__(self, dimension, number = 0):
        if isinstance(dimension,tuple):
            self.__matrix = []
            for i in range(0,dimension[0]):
                line = [number for _ in range(0,dimension[1])]
                self.__matrix.append(line)
        else:
            self.__matrix = dimension

    def __init__(self, matrix, value=0):
        if isinstance(matrix, tuple):
            self.__matrix = [[value] * matrix[1] for _ in range(matrix[0])]
        else:
            self.__matrix = matrix

    #return rows of matrix as below when type print(object)
    #| 1  0  2 |
    #|-1  3  1 |
    def __str__(self):    
        result = ''
        for x in self.__matrix:
            result += '|'
            for y in x:
                if len(str(y))==2:
                    result += f'{y} ' 
                else:
                    result += f' {y} '
            result += '|\n'
        return result
    

    def __add__(self, matrix2):
        result = []
        
        if self.size() != matrix2.size():
            return "Matrices have bad dimensions"
        
        for i in range(0,self.size()[0]): 
            temp = []
            for j in range(0,self.size()[1]): 
                temp.append(self.__matrix[i][j]+matrix2[i][j])
            result.append(temp)
        return create_matrix(result)


    def __mul__(self, matrix2):
        result = []
    
        if self.size()[1] != matrix2.size()[0]:
            return "Matrices have bad dimensions"
        
        for i in range(0,self.size()[0]): 
            li = []
            for j in range(0,self.size()[0]):
                sum = 0 
                for y in range(0,self.size()[1]):
                    sum +=(self.__matrix[i][y]*matrix2[y][j])
                li.append(sum)
            result.append(li)
            
        return create_matrix(result)



    #return size of matrix as tuple(row,column)
    def size(self):
        return len(self.__matrix), len(self.__matrix[0])
    
    def __getitem__(self, coord):
        return self.__matrix[coord] 
    
    def __setitem__(self, key, value):
        self.__matrix[key] = value
        

def transpose_m(matrix):
    n_mat = create_matrix((matrix.size()[1],matrix.size()[0]))
    for i in range(matrix.size()[0]):  ## wiersz
        for j in range(matrix.size()[1]): ## kolumna
            n_mat[j][i] = matrix[i][j]
    return n_mat   


def main():
    
    m1 = create_matrix([[1, 0, 2],
        [-1, 3, 1] ])

    m2 = create_matrix((2,3),1) #kolumna, wiersz

    m3 = create_matrix(
    [ [3, 1],
    [2, 1],
    [1, 0]])
 
    print(transpose_m(m1))
    print(m1+m2)
    print(m1*m3)
   
 

if __name__ == '__main__':
    main()