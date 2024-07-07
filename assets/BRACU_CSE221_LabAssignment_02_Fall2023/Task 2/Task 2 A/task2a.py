#Task 2 A

user_input = open("input2a.txt","r")
output = open("output2a.txt  ","w")

n = int(user_input.readline().strip())
line2 = user_input.readline().strip()
list1 = [int(i) for i in line2.split(" ")]
m = int(user_input.readline().strip())
line4 = user_input.readline().strip()
list2 = [int(i) for i in line4.split(" ")]


def mergelistnlogn(alice_list, bob_list):
    n = len(alice_list) + len(bob_list)
    merged_list = [0] * n  
    i, j, k = 0, 0, 0
    while i < len(alice_list) and j < len(bob_list):
        if alice_list[i] < bob_list[j]:
            merged_list[k] = alice_list[i]
            i += 1
        else:
            merged_list[k] = bob_list[j]
            j += 1
        k += 1
    while i < len(alice_list):
        merged_list[k] = alice_list[i]
        i += 1
        k += 1
    while j < len(bob_list):
        merged_list[k] = bob_list[j]
        j += 1
        k += 1
    return merged_list


new = mergelistnlogn(list1,list2)
new_str = ""
for i in range(len(new)):
  new_str+= (str(new[i])+" ")

output.write(new_str)
user_input.close()
output.close()
