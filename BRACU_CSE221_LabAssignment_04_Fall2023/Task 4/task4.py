#TASK 4

def has_cycle(graph, vertex, visited, stack):
  visited[vertex] = True
  stack[vertex] = True
  for neighbor in graph[vertex]:
    if not visited[neighbor]:
      if has_cycle(graph, neighbor, visited, stack):
        return True
    elif stack[neighbor]:
      return True
  stack[vertex] = False
  return False

def contains_cycle(n, edges):
  graph = {i: [] for i in range(1, n + 1)}
  for edge in edges:
    u, v = edge
    graph[u].append(v)
  visited = {i: False for i in range(1, n + 1)}
  stack = {i: False for i in range(1, n + 1)}
  for vertex in range(1, n + 1):
    if not visited[vertex]:
      if has_cycle(graph, vertex, visited, stack):
        return "YES"
  return "NO"


user_input = open("input4.txt","r")
output = open("output4.txt","w")

N, M = map(int,user_input.readline().strip().split(" "))

edges = []
for line in range(M):
    u, v = map(int,user_input.readline().strip().split(" "))
    edges.append((u, v))

result = contains_cycle(N, edges)
output.write(result)

user_input.close()
output.close()