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
    d = []
    for i in range(1, n):
        if i == start:
            d += [0]
        elif i in distance:
            d += [distance[i]]
    return d


def find_meeting_point(graph, S, T):
    distance_alice = dijkstra(graph, S)
    distance_bob = dijkstra(graph, T)
    min_time = float('inf')
    meeting_point = -1
    d_alice = False
    d_bob = False

    for node in range(1,len(graph)-1):
        if distance_alice[node] != -1 and distance_bob[node] != -1 and max(distance_alice[node], distance_bob[node])<min_time:
            min_time = max(distance_alice[node], distance_bob[node])
            meeting_point = node+1

    return min_time, meeting_point



user_input = open("22301001_CSE221_Lab06\Task 2\input2.txt", "r")
output = open("22301001_CSE221_Lab06\Task 2\output2.txt", "w")



N, M = map(int, user_input.readline().split())
graph = {u: [] for u in range(1, N + 1)}
for _ in range(M):
    u, v, w = map(int, user_input.readline().split())
    graph[u].append((v, w))
S, T = map(int, user_input.readline().split())

time, node = find_meeting_point(graph, S, T)

if node == -1:
    output.write("IMPOSSIBLE")
else:
    output.write(f"Time: {time}\nNode: {node}")



user_input.close()
output.close()