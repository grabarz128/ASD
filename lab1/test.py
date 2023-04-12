import zadanie1
m1 = zadanie1.create_matrix([

    [0 , 1 , 1 , 2 , 3],

    [0 , 2 , 1 , 7 , 3],

    [1 , 1 , 2 , 4 , 7],

    [9 , 1 , 0 , 7 , 0],

    [1 , 4 , 7 , 2 , 2]

    ])

non_zero = [m1[i][0] for i in range(m1.size()[0])]
# for i in range(m1.size()[0]):
#     non_zero.append(m1[i][0])

indexes = [i for i, x in enumerate(non_zero) if x != 0]

print(indexes)