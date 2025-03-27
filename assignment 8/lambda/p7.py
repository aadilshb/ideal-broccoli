def sort_matrix(matrix):
    return sorted(matrix,key=lambda row:sum(row))

matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

s_matrix1 = sort_matrix(matrix1)
s_matrix2 = sort_matrix(matrix2)

print("Original Matrix:", matrix1)
print("Sorted Matrix:", s_matrix1)

print("\nOriginal Matrix:", matrix2)
print("Sorted Matrix:", s_matrix2)
