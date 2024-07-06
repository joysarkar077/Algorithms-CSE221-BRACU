#TASK 2

def generateBFS(graph,start):
    colors = {vertex: 0 for vertex in graph}
    print("Colors", colors)
    visited = []
    colors[start] = 1
    visited.append(start)
    while visited:
        
        vertex = visited.pop(0)
        output.write(f"{vertex} ")
        print("Vertex", vertex,"While visited is",visited)
        for neigh in graph[vertex]:
            print("Vertex", vertex)
            if colors[neigh] == 0:
                colors[neigh] = 1
                visited.append(neigh)
    print("Colors", colors)
    print("Visited", visited)


user_input = open("22301001_CSE221_Lab04\Task 2\input2.txt","r")
output = open("22301001_CSE221_Lab04\Task 2\output2.txt","w")

N, M = map(int,user_input.readline().strip().split(" "))

graph = {i: [] for i in range(1, N + 1)}
print(graph)

for line in range(M):
    u, v = map(int,user_input.readline().strip().split(" "))
    graph[u].append(v)
    graph[v].append(u)

print(graph)
dora = generateBFS(graph, 1)


user_input.close()
output.close()