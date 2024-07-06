#Task 1 B

user_input = open("22301001_CSE221_Lab02\Task 1\Task 1 B\input1b.txt","r")
output = open("22301001_CSE221_Lab02\Task 1\Task 1 B\output1b.txt","w")

line1 = user_input.readline().strip()
str1 = [int(i) for i in line1.split(" ")]

line2 = user_input.readline().strip()
str2 = [int(i) for i in line2.split(" ")]

i = 0
j = str1[0]-1
flag = "POSSIBLE"
try :
  while (i<j):
    if str2[i]+str2[j]<str1[1]:
      i+=1
    elif str2[i]+str2[j]>str1[1]:
      j-=1
    elif str2[i]+str2[j]==str1[1]:
      output.write(f"{i+1} {j+1}")
      break
except:
  flag = "IMPOSSIBLE"
  output.write(flag)


user_input.close()
output.close()