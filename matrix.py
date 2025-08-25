matrix=[
    [1,2,3,4],
    [5,6,7,8],

]
print(matrix[0][2])
print(matrix[1][3])
for row in matrix:
    print(row)
# ---------------------------------------input matrix--------------------------------
matrix=[]
row=int(input("given row size:"))
col=int(input("given col size"))
for i in range(row):
    val=[]
    for j in range(col):
        val.append(input())
    matrix.append(val)
print(matrix)

