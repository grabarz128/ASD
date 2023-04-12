class create_matrix:
    
    #declaration of matrix depending on given arguments
    def __init__(self, dimension, number = 0):
        if isinstance(dimension,tuple):
            self.__matrix = []
            line = [number for _ in range(0,dimension[1])]
            for i in range(0,dimension[0]):
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
        

def count_det(matrix):
    if(matrix.size() == (2,2)):
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    else:
        return "matrix is not (2,2) sqare"


def chio(matrix,coeff):

    mat_size = matrix.size()[0]
    if mat_size == 2:
        return count_det(matrix)*coeff

    if matrix[0][0] == 0:
        first_el = [matrix[i][0] for i in range(mat_size)]
        indexes = [i for i, x in enumerate(first_el) if x != 0]
        for k in range(mat_size):
            matrix[0][k], matrix[indexes[0]][k] = matrix[indexes[0]][k], matrix[0][k]
        coeff *= -1

    a1 = matrix[0][0]
    next_coeff = coeff*(1/(a1**(mat_size-2)))
    
    det_list = []
    for i in range(mat_size-1):
        temp = []
        for j in range(mat_size-1):
            temp.append(count_det(create_matrix([[matrix[0][0],matrix[0][j+1]], [matrix[i+1][0],matrix[i+1][j+1]]])))
        det_list.append(temp)
    
    return chio(create_matrix(det_list),next_coeff)


def main():
    
    m1 = create_matrix([

    [5 , 1 , 1 , 2 , 3],

    [4 , 2 , 1 , 7 , 3],

    [2 , 1 , 2 , 4 , 7],

    [9 , 1 , 0 , 7 , 0],

    [1 , 4 , 7 , 2 , 2]

    ])

    m2 = create_matrix([
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])

    print(chio(m1,1))
    print(chio(m2,1))

 
if __name__ == '__main__':
    main()