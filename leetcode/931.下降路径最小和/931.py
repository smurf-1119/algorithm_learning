def minFallingPathSum(matrix) -> int:
    f = matrix.copy()

    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if j == 0:
                f[i][j] = min(f[i-1][j], f[i-1][j+1]) + f[i][j]
            elif j == len(matrix[0]) - 1:
                f[i][j] = min(f[i-1][j], f[i-1][j-1]) + f[i][j]
            else:
                f[i][j] = min(f[i-1][j], f[i-1][j-1], f[i-1][j+1]) + f[i][j]
    
    return min(f[-1])

matrix = [[-84,-36,2],[87,-79,10],[42,10,63]]
print(minFallingPathSum(matrix))