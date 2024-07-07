#TASK 1B


user_input = open("input1b.txt","r")
output = open("output1b.txt","w")

N, M = map(int,user_input.readline().strip().split(" "))
list1 = [0] * (N+1)

for i in range(int(M)):
  x,y,z = map(int,user_input.readline().strip().split(" "))

  if list1[x] != 0:
    list1[x].append((y,z))

  else:
    list1[x] = [(y,z)]

temp = ""
for i in range(len(list1)):
  if list1[i] == 0:
    output.write(f'{i} : \n')
  else:
    temp = ""
    for j in list1[i]:
      temp += str(j)+" "
    output.write(f'{i} : {temp}\n')

user_input.close()
output.close()