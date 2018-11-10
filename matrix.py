#matrix operations
#defining a matrix
A = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

#we have now created a matix of size 3x4
#each list in a represents a row and all 1st elements in it represents the 1st column
#to get the element Anm i.e nth row,mth coloumn -  Anm = A[n-1][m-1]
firstrow = A[0]


#To get first column
column = []
for row in A:
	column.append(row[0])
print(column)


#additon of matrices
B = [[12,11,10,9],[8,7,6,5],[4,3,2,1]]
result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(0,len(A)):
	for j in range(0,len(A[0])):
		result[i][j] = A[i][j] + B[i][j]
print(result)


#multiplication of matrices
for i in range(len(A)):
   for j in range(len(B[0])):
       for k in range(len(B)):
           result[i][j] += A[i][k] * B[k][j]
print(result)


#transpose
C= [[12,7],[4 ,5],[3 ,8]]
transpose = [[0,0,0],[0,0,0]]
for i in range(len(C)):
   for j in range(len(C[0])):
       transpose[j][i] = C[i][j]
print(transpose)


#slicing of matrices
A = [[1, 4, 5, 12, 14], 
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21]]

print(A[:2, :4])  # two rows, four columns

#Output:[[ 1  4  5 12][-5  8  9  0]]

print(A[:1,])  # first row, all columns

#Output:[[ 1  4  5 12 14]]

print(A[:,2])  # all rows, second column

#Output:[ 5  9 11]

print(A[:, 2:5])  # all rows, third to fifth column
#Output:[[ 5 12 14][ 9  0 17][11 19 21]]
