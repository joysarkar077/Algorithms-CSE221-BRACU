#TASK 1A

user_input = open("22301001_CSE221_Lab04\Task 1\Task 1 A\output1a.txt","r")
output = open("22301001_CSE221_Lab04\Task 1\Task 1 A\output1a.txt","w")

import numpy as np

N, M = map(int,user_input.readline().strip().split(" "))
matrix = np.zeros((N+1, N+1))

for i in range(int(M)):
  x,y,z = map(int,user_input.readline().strip().split(" "))
  matrix[x][y] = z

for i in range(N+1):
  for j in range((N+1)):
    if j != N:
      output.write(f"{int(matrix[i][j])} ")
    else:
      output.write(f"{int(matrix[i][j])}\n")

user_input.close()
output.close()
print(matrix)