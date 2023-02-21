def my_sparse(thelist):
    my_efficiant_list = []

    for i in range(len(thelist)):
        for j in range(len(thelist[i])):
            if (thelist[i][j] != 0):
                my_efficiant_list.append([i, j, thelist[i][j]])

    return(my_efficiant_list)


mylist = [
    [1.0, 0, 5.0, 0, 0, 0, 0, 0],
    [0, 3.0, 0, 0, 0, 0, 11.0, 0],
    [0, 0, 0, 0, 9.0, 0, 0, 0],
    [0, 0, 6.0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7.0, 0, 0, 0, 0],
    [2.0, 0, 0, 0, 0, 10.0, 0, 0],
    [0, 0, 0, 8.0, 0, 0, 0, 0],
    [0, 4.0, 0, 0, 0, 0, 0, 12.0]
]

print(my_sparse(mylist))