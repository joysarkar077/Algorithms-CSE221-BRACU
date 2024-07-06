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
    elatI = list1[i]
    elatP = list1[p_index]
    if elatI <= pivot: 
      elatI, elatP = elatP, elatI 
      p_index += 1 
  list1[end], elatP = elatP, list1[end] 
  return p_index





line1 = 6
list1 = [8, 1, 4, 2, 1, 3]


sorted = quickSort(list1,0,line1-1)
print(sorted)