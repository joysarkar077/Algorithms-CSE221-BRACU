#Openning user input and output file
user_input = open("input1b.txt","r")
output = open("output1b.txt","w")

num = int(user_input.readline())

#Reading the value in each line
#Checking the operator and complete the calculation
#Writing in the output file
for line in range(num):
  val = user_input.readline().strip()
  val2 = val.split(" ")
  if val2[2]=="+":
    output.write(f"The result of {val2[1]} + {val2[3]} is {int(val2[1])+int(val2[3])}\n")
  elif val2[2]=="-":
    output.write(f"The result of {val2[1]} - {val2[3]} is {int(val2[1])-int(val2[3])}\n")
  elif val2[2]=="*":
    output.write(f"The result of {val2[1]} * {val2[3]} is {int(val2[1])*int(val2[3])}\n")
  elif val2[2]=="/":
    output.write(f"The result of {val2[1]} / {val2[3]} is {int(val2[1])/int(val2[3])}\n")