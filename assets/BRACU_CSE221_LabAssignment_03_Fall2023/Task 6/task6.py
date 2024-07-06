def findTheValue(array, s_index, e_index, K):
  if s_index == K: 
    return array[s_index-1]
  else:
    partition_point = partition(array, s_index, e_index)
    if partition_point == K:
      return array[partition_point-1]
    elif partition_point<K:
      return findTheValue(array, s_index+1, e_index, K)
    else:
      return findTheValue(array, s_index, e_index-1, K)

def partition(list1, start, end):
  pivot = list1[end] 
  p_index = start     
  for i in range(start, end): 
    if list1[i] <= pivot: 
      list1[i], list1[p_index] = list1[p_index], list1[i] 
      p_index += 1 
  list1[end], list1[p_index] = list1[p_index], list1[end] 
  return p_index



user_input = open("input6.txt","r")
output = open("output6.txt","w")

line1 = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list1 = list(map(int,line2.split(" ")))
line3 = int(user_input.readline().strip())

for i in range(line3):
    K = int(user_input.readline().strip())
    number = findTheValue(list1, 0, line1-1, K)
      output.write(f"{number}\n")
user_input.close()
output.close()
