#Task 2
def isMax(a, b):
  if a>b:
    return a
  else:
    return b

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid])
    a2 = mergeSort(arr[mid:])
    return isMax(a1, a2)


user_input = open("22301001_CSE221_Lab03\Task 2\input2.txt","r")
output = open("22301001_CSE221_Lab03\Task 2\output2.txt","w")


line1 = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list1 = list(map(int,line2.split(" ")))


max = mergeSort(list1)


output.write(f"{max[0]}")
user_input.close()
output.close()