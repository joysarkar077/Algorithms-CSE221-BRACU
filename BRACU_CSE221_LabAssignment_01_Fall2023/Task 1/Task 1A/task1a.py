#Openning user input and output file
user_input = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 1\Task 1A\input1a.txt","r")
output = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 1\Task 1A\output1a.txt","w")

num = int(user_input.readline())

#Reading the value in each line
#Checking if the value is even or odd
#Writing in the output file
for line in range(num):
  val = int(user_input.readline().strip())
  if int(val)%2==0:
    output.write(f"{val} is an Even number.\n")
  else:
    output.write(f"{val} is an Odd number.\n")
  