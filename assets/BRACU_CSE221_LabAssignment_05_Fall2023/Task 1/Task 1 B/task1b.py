def course_order_bfs(N, preReq):
    graph = {}
    in_degree = [0] * (N + 1)

    for i in preReq:
        if i[0] not in graph:
            graph[i[0]] = []
        graph[i[0]].append(i[1])
        in_degree[i[1]] += 1

    queue = []
    for course in range(1, N + 1):
        if in_degree[course] == 0:
            queue.append(course)

    order = []
    while queue:
        current_course = queue.pop(0)
        order.append(current_course)

        if current_course in graph:
            for neighbor in graph[current_course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    if len(order) == N:
        return order
    else:
        return "IMPOSSIBLE"


user_input = open("input1b.txt", "r")
output = open("output1b.txt", "w")


N, M = map(int,user_input.readline().strip().split(" "))
array = []
for i in range(M):
    array += [user_input.readline().strip()]
prereq =[tuple(map(int, i.split())) for i in array]
result= course_order_bfs(N, prereq)
if result == "IMPOSSIBLE":
    output.write(f"{result}")
else:
    for i in result:
        output.write(f"{i} ")


user_input.close()
output.close()