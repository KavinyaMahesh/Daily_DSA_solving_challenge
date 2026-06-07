def set_matrix_zeros(matrix):

    m=len(matrix)
    n=len(matrix[0]) 

    row=[0]*m
    col=[0]*n

    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1

    for i in range(m):
        for j in range(n):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0  

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9]
    ]
    set_matrix_zeros(matrix)
    print("Matrix after setting zeros:")
    for row in matrix:
        print(row)
        