def dfs(graph, vertex, visited, order, cycle_detection):
    visited[vertex] = True
    cycle_detection[vertex] = True  # Mark the current node as part of the current DFS path
    if vertex in graph:
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                if dfs(graph, neighbor, visited, order, cycle_detection):
                    return True
            elif cycle_detection[neighbor]:
                # If the neighbor is part of the current DFS path, there is a cycle
                return True
    
    cycle_detection[vertex] = False  # Mark the current node as no longer part of the current DFS path
    order.append(vertex)
    return False

def course_order_dfs(N, preReq):
    graph = {}
    for i in preReq:
        if i[0] not in graph:
            graph[i[0]] = []
        graph[i[0]].append(i[1])

    visited = [False] * (N + 1)
    order = []
    cycle_detection = [False] * (N + 1)

    for course in range(1, N + 1):
        if not visited[course]:
            if dfs(graph, course, visited, order, cycle_detection):
                return "IMPOSSIBLE"
    return order[::-1]


user_input = open("22301001_CSE221_Lab05\Task 1\Task 1 A\input1a.txt", "r")
output = open("22301001_CSE221_Lab05\Task 1\Task 1 A\output1a.txt", "w")


N, M = map(int,user_input.readline().strip().split(" "))
array = []
for i in range(M):
    array += [user_input.readline().strip()]
preReq =[tuple(map(int, i.split())) for i in array]
result = course_order_dfs(N, preReq)
if result == "IMPOSSIBLE":
    output.write(f"{result}")
else:
    for i in result:
        output.write(f"{i} ")


user_input.close()
output.close()