#TASK 3

def generateDFS(graph,start,visited=[]):
    print("Visited", visited)
    output.write(f"{start} ")
    visited += [start]
    print("Visited", visited)
    for neigh in graph[start]:
        if neigh not in visited:
            generateDFS(graph,neigh,visited)

user_input = open("input3.txt","r")
output = open("output3.txt","w")

N, M = map(int,user_input.readline().strip().split(" "))

graph = {i: [] for i in range(1, N + 1)}

for line in range(M):
    u, v = map(int,user_input.readline().strip().split(" "))
    graph[u].append(v)
    graph[v].append(u)

dora = generateDFS(graph, 1)

user_input.close()
output.close()