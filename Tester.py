import math
matrix = [[0 for _ in range(0,10)]for y in range(1, 6)]
k = 0 #winkel
for i in range(0, 10):
    matrix[0][i] = i+1 #setzten der Radien
    
print(matrix[0])
print(matrix)

for i in range(0, 10):
    matrix[1][i] = math.cos(math.pi) * matrix[0][i]
print(matrix)
