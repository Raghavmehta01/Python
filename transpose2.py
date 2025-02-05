
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
def transpose(matrix):
    
    nums = [[0 for _ in range(n)]for _ in range(n)]
    print(f"List before transpose : \n{nums}")
    for i in range(n):
        for j in range(n):
            nums[j][i] = matrix[i][j]
    print(f"List after transpose :")        
    for x in matrix:
        print(x)

print(transpose(matrix))