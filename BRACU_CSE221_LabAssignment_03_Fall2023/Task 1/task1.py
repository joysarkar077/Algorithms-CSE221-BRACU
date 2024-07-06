#Task-1

def merge(a, b):
  merged = []
  l = 0
  r = 0
  while l< len(a) and r< len(b):
    if a[l] <= b[r]:
      merged.append(str(a[l]))
      l += 1
    else:
      merged.append(str(b[r]))
      r += 1
  merged.extend(map(str, a[l:]))
  merged.extend(map(str, b[r:]))
  return merged

# write your code here
# Here a and b are two sorted list
# merge function will return a sorted list after merging a and b

def mergeSort(arr):
  if len(arr) <= 1:
    return arr
  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[:mid]) # write the parameter
    a2 = mergeSort(arr[mid:]) # write the parameter
    return merge(a1, a2) # complete the merge function above`


user_input = open("22301001_CSE221_Lab03\Task 1\input1.txt","r")
output = open("22301001_CSE221_Lab03\Task 1\output1.txt","w")

line1 = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list2 = list(map(int,line2.split(" ")))


merge_sort = mergeSort(list2)
for i in merge_sort:
  output.write(f"{i} ")
user_input.close()
output.close()