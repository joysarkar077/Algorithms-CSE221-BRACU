#Task-1 A

user_input = open("input1a.txt","r")
output = open("output1a.txt","w")

line1 = user_input.readline().strip()
str1 = [int(i) for i in line1.split(" ")]

line2 = user_input.readline().strip()
str2 = [int(i) for i in line2.split(" ")]

count = 0

for i in range(str1[0]):
  for j in range(i+1,str1[0]):
    if str2[i]+str2[j]==str1[1] and count==0:
      output.write(f"{i+1} {j+1}")
      count=1

user_input.close()
output.close()