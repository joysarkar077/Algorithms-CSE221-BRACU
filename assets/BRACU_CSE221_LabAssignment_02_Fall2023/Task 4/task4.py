#Task 4

user_input = open("22301001_CSE221_Lab02\Task 4\input4.txt","r")
output = open("22301001_CSE221_Lab02\Task 4\output4.txt","w")

line1 = [int(i) for i in user_input.readline().strip().split(" ")]
n,m = line1[0],line1[1]

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

task = {}
man = 0
t = 0
val = []
for i in range(n):
  keys = list(task.keys())
  
  if (list1[i][0] not in task) and (man<m):
    task[list1[i][0]]=[list1[i]]
    val.append(list1[i])
    man+=1
    t+=1
  for j in keys:
    if (task[j][len(task[j])-1][1]<=list1[i][0]):
      task[j].append(list1[i])
      t+=1

output.write(f"{t}")
user_input.close()
output.close()