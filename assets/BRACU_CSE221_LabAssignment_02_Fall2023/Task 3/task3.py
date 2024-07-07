#Task 3

user_input = open("input3.txt","r")
output = open("output3.txt","w")

n = int(user_input.readline().strip())

list1 = []

for j in range(n):
  list2 = [int(i) for i in user_input.readline().strip().split(" ")]
  list1.extend([list2])

for i in range(n):
  min = i
  for j in range(i+1,n):
    if list1[j][1] < list1[min][1]:
      min = j
  list1[i],list1[min] = list1[min],list1[i]

task = []
t = 0
for i in range(n):
  if len(task) == 0:
    task.append(list1[i])
  elif len(task)>0 and task[t][1]<=list1[i][0]:
    task.append(list1[i])
    t+=1

output.write(f"{len(task)}\n")
for i in range(len(task)):
  output.write(f"{task[i][0]} {task[i][1]}\n")
user_input.close()
output.close()
