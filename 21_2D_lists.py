# used to create matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print('\n', matrix[0][1])

# modify
matrix[0][1] = 20
print('\nModified: ', matrix[0][1])

# iterate through all the items

print('\n-----------ITERATE THROUGH ITEMS IN MATRIX------------------')
for row in matrix:
    for item in row:
        print(item)
print('-----------------------------')
