def quickSort(list1, start, end):
  if len(list1) == 1:
    return list1
  elif start < end:
    p = partition(list1, start, end)
    quickSort(list1,start, p-1) 
    quickSort(list1, p+1, end) 

def partition(list1, start, end):
  pivot = list1[end] 
  p_index = start     
  for i in range(start, end): 
    if list1[i] <= pivot: 
      list1[i], list1[p_index] = list1[p_index], list1[i] 
      p_index += 1 
  list1[end], list1[p_index] = list1[p_index], list1[end] 
  return p_index


user_input = open("input5.txt","r")
output = open("output5.txt","w")


line1 = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list1 = list(map(int,line2.split(" ")))


sorted = quickSort(list1,0,line1-1)

for i in sorted:
  output.write(f"{i} ")
user_input.close()
output.close()