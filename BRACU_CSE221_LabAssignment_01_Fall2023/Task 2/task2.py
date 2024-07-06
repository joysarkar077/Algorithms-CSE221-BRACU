#Openning user input and output file
user_input = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 2\input2.txt","r")
output = open("C:\VS_Contents\22301001_CSE221_Lab01\Task 2\output2.txt","w")

#Reading the inputs and making a list for sorting it in ascending order
num = int(user_input.readline())
str1 = user_input.readline().strip()
str2 = [int(i) for i in str1.split(" ")]

#Taking finding the minimum and miximum value from the list
min = str2[0]
max = str2[0]
for i in str2:
  if i<min:
    min=i
  if i>max:
    max=i

#Sorting list by increasing value from minimum to maximum
sorted = ""
for i in range(min,max+1):
  if i in str2:
    sorted+= str(i)+" "

#Writing the output in txt files
output.write(sorted)

#Let's analyze the time complexity for each operations
#T(n) = O(1) [Openning files] + O(n) [Reading the inputs] + O(n) [Finding the minimum and maximum value] + O(n) [Sorting the list] + O(n) [Writing the output]
#T(n) = O(1) + O(n) + O(n) + O(n) + O(n)
#T(n) = O(1) + 4 x O(n)
#T(n) = O(n)

#Here, Time complexity for all the senario will be O(n). So in the best case senario for this code time complexity will be O(n).
#This is how the code will achieve O(n) for the best case senario.