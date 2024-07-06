#Task 2 B

user_input = open("22301001_CSE221_Lab02\Task 2\Task 2 B\input2b.txt","r")
output = open("22301001_CSE221_Lab02\Task 2\Task 2 B\output2b.txt","w")

n = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list1 = [int(i) for i in line2.split(" ")]
m = int(user_input.readline().strip())
line4 = user_input.readline().strip()
list2 = [int(i) for i in line4.split(" ")]

def mergeSorted(list1, list2):
  new = []
  left=0
  right=0
  for i in range(len(list1)+len(list2)):
    if left<len(list1) and right<len(list2):
        if list1[left]<list2[right]:
          new.append(list1[left])
          left+=1
        else:
          new.append(list2[right])
          right+=1
    else:
        if left < len(list1):
            new.append(list1[left])
            left+=1
        else:
            new.append(list2[right])
            right+=1
  return new


new = mergeSorted(list1,list2)
new_str = ""
for i in range(len(new)):
  new_str+= (str(new[i])+" ")

output.write(new_str)
user_input.close()
output.close()