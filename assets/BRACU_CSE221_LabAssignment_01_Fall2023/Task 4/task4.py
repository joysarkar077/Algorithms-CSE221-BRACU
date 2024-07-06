#Openning user input and output file
user_input = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 4\input4.txt","r")
output = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 4\output4.txt","w")

num = int(user_input.readline())
train = []

#Reading data from input.txt file
#Making a different data list with necessary element for sorting easily
for line in range(num):
  val = user_input.readline().strip()
  val2 = val.split(" ")
  name = val2[0]
  time = int(val2[6][0:2]+val2[6][3:5])
  time_str = val2[6]
  dept = val2[4]
  train.append([name,time,dept,time_str])

#Sorting the train data according to their name and time
for i in range(num):
  min = i
  for j in range(i+1,num):
    if train[j][0] < train[min][0] or (train[j][0]==train[min][0] and train[j][1]>train[min][1]):
      min = j
  train[i],train[min] = train[min],train[i]

#Writing output in output.txt file
for i in range(num):
  output.write(f"{train[i][0]} will departure for {train[i][2]} at {train[i][3]}\n")