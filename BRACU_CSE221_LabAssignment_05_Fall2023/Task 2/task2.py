def smallestOrder(N, preReq):
    graph = {}
    in_degree = [0] * (N + 1)

    for each in preReq:
        if each[0] not in graph:
            graph[each[0]] = []
        graph[each[0]].append(each[1])
        in_degree[each[1]] += 1

    queue = []
    result_order = []
    for course in range(1, N + 1):
        if in_degree[course] == 0:
            queue.append(course)

    while queue:
        current_course = min(queue)  # Choose the lexicographically smallest course
        queue.remove(current_course)
        result_order.append(current_course)
        if current_course in graph:
            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
    if len(result_order) == N:
        return result_order
    else:
        return "IMPOSSIBLE"


user_input = open("22301001_CSE221_Lab05\Task 2\input2.txt", "r")
output = open("22301001_CSE221_Lab05\Task 2\output2.txt", "w")


N, M = map(int, user_input.readline().strip().split())
array = []
for i in range(M):
    array += [user_input.readline().strip()]
prereq =[tuple(map(int, i.split())) for i in array]
result= smallestOrder(N, prereq)
if result == "IMPOSSIBLE":
    output.write(f"{result}")
else:
    for i in result:
        output.write(f"{i} ")


user_input.close()
output.close()