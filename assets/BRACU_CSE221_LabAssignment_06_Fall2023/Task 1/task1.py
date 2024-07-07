def dijkstra(graph, start):
    n = len(graph)
    distance = {}
    priority_queue = [(0, start)]

    while priority_queue:
        w1, N = priority_queue.pop(0)

        if N in distance:
            continue

        distance[N] = w1

        for n2, w2 in graph[N]:
            if n2 not in distance:
                priority_queue+=[(w1 + w2, n2)]
                priority_queue.sort()
    for i in range(n+1):
        if i not in distance:
            distance[i] = -1
    return distance



user_input = open("input1.txt", "r")
output = open("output1.txt", "w")



N, M = map(int, user_input.readline().split())
graph = {u: [] for u in range(1, N + 1)}
for _ in range(M):
    u, v, w = map(int, user_input.readline().split())
    graph[u].append((v, w))

source = int(user_input.readline())

distance = dijkstra(graph, source)

for i in range(1, N + 1):
    if i == source:
        output.write(f"0 ")
    elif i in distance:
        output.write(f"{distance[i]} ")



user_input.close()
output.close()