#Openning user input and output file
user_input = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 3\input3.txt","r")
output = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 3\output3.txt","w")

num = int(user_input.readline())
students = []

#Reading data from input.txt file
#Making a different list with both elements for sorting easily
str1 = user_input.readline().strip()
sid = [int(i) for i in str1.split(" ")]
str2 = user_input.readline().strip()
smark = [int(i) for i in str2.split(" ")]
for i in range(num):
  students.append([smark[i],sid[i]])

#Sorting students according to students marks and id
for i in range(num):
  max = i
  for j in range(i+1,num):
    if students[j][0] > students[max][0] or (students[j][0]==students[max][0] and students[j][1]<students[max][1]):
      max = j
  students[i],students[max]=students[max],students[i]

#Writing output in output.txt file
for i in range(num):
  output.write(f"ID: {students[i][1]} Mark: {students[i][0]}\n")