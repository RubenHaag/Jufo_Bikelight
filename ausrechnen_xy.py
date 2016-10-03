import math
matrix = [[0 for _ in range(0,10)]for y in range(1, 6)]
k = math.pi/2 #winkel
for i in range(0, 10):
    matrix[0][i] = i+1 #setzten der Radien
    


for i in range(0, 10):
    matrix[1][i] = round(math.cos(k) * matrix[0][i], 1) 
    matrix[2][i] = round(math.sin(k) * matrix[0][i], 1)
    
print(matrix[0])
print(matrix[1])
print(matrix[2])


