# 5. A sparse matrix is a matrix in which most of the elements have zero value. Write a program 
# to read a sparse matrix from a file and transform it into efficient dictionary representation 
# where the key is a tuple (row, col) and the value is the data. Write a function 
# get_val(matrix, row, col) that returns the value if it exists, or 0 if it doesn't.  
# Input:   
# [[0, 0, 0, 1, 0], 
# [0, 0, 0, 0, 0], 
# [0, 2, 0, 0, 0], 
# [0, 0, 0, 0, 0], 
# [0, 0, 0, 3, 0]] 
# Output:  {(0, 3): 1, (2, 1): 2, (4, 3): 3}


x=[[0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0], 
[0, 2, 0, 0, 0], 
[0, 0, 0, 0, 0], 
[0, 0, 0, 3, 0]] 

def sparse_matrix(matrix):
    y={}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]!=0:
                y[(i,j)]=matrix[i][j]
    return y
 
sparse_representation = sparse_matrix(x)
print("Sparse Matrix Representation:", sparse_representation)