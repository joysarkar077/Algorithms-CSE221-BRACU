stack = []
def dfs1(graph, node):
    visited[node] = 1
    for neighbor in graph[node]:
        if visited[neighbor] == 0:
            dfs1(graph, neighbor)
    stack.append(node)

result = []
def dfs2(graph, node):
  if visited[node] == 0:
      result.append(node)
      visited[node] = 1
      for neighbor in graph[node]:
          if visited[neighbor] == 0:
              dfs2(graph, neighbor)


user_input = open("22301001_CSE221_Lab05\Task 3\input3.txt", "r")
output = open("22301001_CSE221_Lab05\Task 3\output3.txt", "w")


N, M = map(int, user_input.readline().strip().split())
graph = {i: [] for i in range(1, N + 1)}
trans_graph = {i: [] for i in range(1, N + 1)}

for i in range(M):
    u, v = map(int, user_input.readline().strip().split())
    graph[u].append(v)
    trans_graph[v].append(u)

visited = [0] * (N+1)
for i in range(1,len(visited)):
  if visited[i] == 0:
    dfs1(graph, i)
visited = [0] * (N+1)
while stack:
  dfs2(trans_graph, stack.pop())
  if result != []:
    for i in result:
      output.write(f'{i} ')
    output.write("\n")
  result = []


user_input.close()
output.close()