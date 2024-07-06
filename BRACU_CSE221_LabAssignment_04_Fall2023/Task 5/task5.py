#TASK 5

def shortest_path(graph, start, end):
  queue = [(start, [start])]
  visited = set()
  while queue:
    current, path = queue.pop(0)
    visited.add(current)
    if current == end:
      return len(path) - 1, path
    for neighbor in graph[current]:
      if neighbor not in visited:
        queue.append((neighbor, path + [neighbor]))
  return float('inf'), []

user_input = open("input5.txt","r")
output = open("output5.txt","w")

N, M, D = map(int,user_input.readline().strip().split(" "))

graph = {i: [] for i in range(1, N + 1)}

for line in range(M):
  u, v = map(int,user_input.readline().strip().split(" "))
  graph[u].append(v)
  graph[v].append(u)

time, path = shortest_path(graph, 1, D)
output.write(f"Time: {time}\n")
output.write(f"Shortest Path: {' '.join(map(str, path))}")

user_input.close()
output.close()