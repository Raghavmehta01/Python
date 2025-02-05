
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
print(n)

def transpose(matrix):
    trans = [[0 for _ in range(n)] for _ in range(n)]
    print(trans)
    for i in range(n):
        for j in range(n):
            trans[i][j] = matrix[j][i]
        
    return trans

print(transpose(matrix))