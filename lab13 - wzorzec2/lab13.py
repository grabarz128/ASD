import time

def string_compare_rec(P,T,i,j):
    if i == 0:
        return j
    if j == 0:
        return i
    zamian = string_compare_rec(P,T,i-1,j-1) + (P[i] != T[j])
    wstawien = string_compare_rec(P,T,i,j-1) + 1
    usuniec = string_compare_rec(P,T,i-1,j) + 1

    return min([zamian,wstawien,usuniec])


def string_compare(P,T,i,j):
    P_size = len(P)
    T_size = len(T)
    D = [[0 for _ in range(T_size)] for i in range(P_size)]

    for i in range(T_size):
        D[0][i] = i
    
    for j in range(P_size):
        D[j][0] = j

    parent = [['X' for _ in range(T_size)] for i in range(P_size)]

    for i in range(T_size-1):
        parent[0][i+1] = 'I'
    
    for j in range(P_size-1):
        parent[j+1][0] = "D"

    signs = {'I':0,'S':0,'D':0}
    for i in range(P_size):
        for j in range(T_size):
            signs['S'] = D[i-1][j-1] + (P[i] != T[j])
            signs['I'] = D[i][j-1] + 1
            signs['D'] = D[i-1][j] + 1

            min_cost_key = min(signs, key = lambda k: signs[k])
            D[i][j] = signs[min_cost_key]
            parent[i][j] = min_cost_key
            if min_cost_key == 'S' and T[j] == P[i]:
                    parent[i][j] = 'M'
            

    return D[-1][-1]


def string_compare_path(P,T,i,j):
    P_size = len(P)
    T_size = len(T)
    D = [[0 for _ in range(T_size)] for i in range(P_size)]

    for i in range(T_size):
        D[0][i] = i
    
    for j in range(P_size):
        D[j][0] = j

    parent = [['X' for _ in range(T_size)] for i in range(P_size)]

    for i in range(T_size):
        parent[0][i] = 'I'
    
    for j in range(P_size):
        parent[j][0] = "D"
    
    signs = {'I':float('inf'),'S':float('inf'),'D':float('inf')}
    
    for i in range(1,P_size):
        for j in range(1,T_size):
            signs['S'] = D[i-1][j-1] + (P[i] != T[j])
            signs['I'] = D[i][j-1] + 1
            signs['D'] = D[i-1][j] + 1
            min_cost_key = min(signs, key = lambda k: signs[k])
            D[i][j] = signs[min_cost_key]
            parent[i][j] = min_cost_key
            if min_cost_key == 'S' and T[j] == P[i]:
                    parent[i][j] = 'M'
    
    parent[0][0] = 'X'

    row = len(parent) - 1
    col = len(parent[0]) - 1

    result = ''

    while row != 0 and col != 0:
        temp = parent[row][col]
        if temp == 'D':
            row -= 1
        elif temp == 'I':
            col -= 1
        else:
            row -= 1
            col -= 1
        result += temp
    
    temp = parent[row][col]
    result += temp

    return result[::-1]


def string_compare_match(P,T,i,j):
    P_size = len(P)
    T_size = len(T)
    D = [[0 for _ in range(T_size)] for i in range(P_size)]

    # I rzad na zero
    # for i in range(T_size):
    #     D[0][i] = i
    
    for j in range(P_size):
        D[j][0] = j

    parent = [['X' for _ in range(T_size)] for i in range(P_size)]

    # for i in range(T_size):
    #     parent[0][i] = 'I'
    
    for j in range(P_size):
        parent[j][0] = "D"
    
    parent[0][0] = 'X'
    
    signs = {'I':float('inf'),'S':float('inf'),'D':float('inf')}
    
    for i in range(1,P_size):
        for j in range(1,T_size):
            signs['S'] = D[i-1][j-1] + (P[i] != T[j])
            signs['I'] = D[i][j-1] + 1
            signs['D'] = D[i-1][j] + 1
            min_cost_key = min(signs, key = lambda k: signs[k])
            D[i][j] = signs[min_cost_key]
            parent[i][j] = min_cost_key
            if min_cost_key == 'S' and T[j] == P[i]:
                    parent[i][j] = 'M'
    
    parent[0][0] = 'X'

    end = D[-1].index(min(D[-1]))
    result = end - len(P.strip()) + 1

    return result


def string_compare_seq(P,T,i,j):
    P_size = len(P)
    T_size = len(T)
    D = [[0 for _ in range(T_size)] for i in range(P_size)]

    for i in range(T_size):
        D[0][i] = i
    
    for j in range(P_size):
        D[j][0] = j

    parent = [['X' for _ in range(T_size)] for i in range(P_size)]

    for i in range(T_size):
        parent[0][i] = 'I'
    
    for j in range(P_size):
        parent[j][0] = "D"
    
    signs = {'I':float('inf'),'S':float('inf'),'D':float('inf')}
    
    for i in range(1,P_size):
        for j in range(1,T_size):
            
            if P[i] == T[j]:
                signs['S'] = D[i-1][j-1] 
            else:   
                signs['S'] = D[i-1][j-1] + float('inf')

            signs['I'] = D[i][j-1] + 1
            signs['D'] = D[i-1][j] + 1
            min_cost_key = min(signs, key = lambda k: signs[k])
            D[i][j] = signs[min_cost_key]
            parent[i][j] = min_cost_key
            if min_cost_key == 'S' and T[j] == P[i]:
                    parent[i][j] = 'M'
    
    parent[0][0] = 'X'

    row = len(parent) - 1
    col = len(parent[0]) - 1

    result = ''

    while row != 0 and col != 0:
        temp = parent[row][col]
        if temp == 'D':
            row -= 1
        elif temp == 'I':
            col -= 1
        elif temp == "M":
            result += P[row]
            row -= 1
            col -= 1
        else:
            row -= 1
            col -= 1
    

    return result[::-1]


P = ' kot'
T = ' pies'

print(string_compare_rec(P, T, len(P) - 1, len(T) - 1))

P = ' biały autobus'
T = ' czarny autokar'

print(string_compare(P, T, len(P) - 1, len(T) - 1))

P = ' thou shalt not'
T = ' you should not'

print(string_compare_path(P, T, len(P) - 1, len(T) - 1))

P = ' ban'
T = ' mokeyssbanana'

print(string_compare_match(P, T, len(P) - 1, len(T) - 1))

P = ' democrat'
T = ' republican'

print(string_compare_seq(P, T, len(P) - 1, len(T) - 1))


T = ' 243517698'
P = ' '

to_sort = [] 
for el in T.strip():
    to_sort.append(int(el))
to_sort.sort()
for el in to_sort:
    P += str(el)

print(string_compare_seq(P, T, len(P) - 1, len(T) - 1))