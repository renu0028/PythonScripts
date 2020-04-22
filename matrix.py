n=input("Enter 2 nos.: ")
l=[]
l=n.split(',')
row=int(l[0])
col=int(l[1])
matrix=[[0 for j in range(col)] for i in range(row)]
for i in range(row):
 for j in range(col):
  matrix[i][j]=i*j
print(matrix)
