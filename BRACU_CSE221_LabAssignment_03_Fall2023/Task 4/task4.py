#Task 4

def calculateSum(left, right):
    ith_max = max(left)
    jth_max = max(map(abs, right))
    return int(ith_max + jth_max ** 2)

def findMax(elem):
    if len(elem) == 2:
        return elem[0] + elem[1] ** 2
    elif len(elem) < 2:
        return 0
    mid = len(elem) // 2
    left_r = findMax(elem[:mid])
    right_r = findMax(elem[mid:])
    sum = calculateSum(elem[:mid], elem[mid:])
    return max(left_r, right_r, sum)




user_input = open("22301001_CSE221_Lab03\Task 4\input4.txt","r")
output = open("22301001_CSE221_Lab03\Task 4\output4.txt","w")


line1 = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list1 = list(map(int,line2.split(" ")))


max = findMax(list1)


output.write(f"{max}")
user_input.close()
output.close()