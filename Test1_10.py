matrix_one = [[1, 2, 3, 4, 5, 6, 7, 8],
              [1, 2, 3, 4, 5, 6, 7, 8],
              [1, 2, 3, 4, 5, 6, 7, 8]]


def transpose(mtrx):
    inner_list = [0]*len(mtrx)
    full_list = [inner_list[:] for i in range(len(mtrx[0]))]
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            full_list[j][i] = mtrx[i][j]
    return full_list


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="\t")
        print("")


print_matrix(transpose(matrix_one))
