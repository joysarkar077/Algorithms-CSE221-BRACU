#Task 3

def merge(a, b):
  merged = []
  swapping = 0
  i = j = 0
  while i < len(a) and j < len(b):
    if a[i] <= b[j]:
      merged.append(a[i])
      i += 1
    else:
      merged.append(b[j])
      j += 1
      swapping += len(a) - i

  merged.extend(a[i:])
  merged.extend(b[j:])
  return merged, swapping

def counter(arr):
  if len(arr) <= 1:
      return arr, 0
  mid = len(arr) // 2
  l, li = counter(arr[:mid])
  r, ri = counter(arr[mid:])
  merged, split = merge(l, r)

  total_inversions = li + ri + split
  return merged, total_inversions



user_input = open("input3.txt","r")
output = open("output3.txt","w")


line1 = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list1 = list(map(int,line2.split(" ")))


sorted, count = counter(list1)


output.write(f"{count}")
user_input.close()
output.close()