#TASK 6

def isValid(grid, visited, row, col):
  rows, cols = len(grid), len(grid[0])
  return 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#' and not visited[row][col]

def floodFill(grid, visited, row, col):
  rows, cols = len(grid), len(grid[0])
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  if not isValid(grid, visited, row, col):
    return 0
  visited[row][col] = True
  diamonds = 1 if grid[row][col] == 'D' else 0
  for dr, dc in directions:
    nrow, ncol = row + dr, col + dc
    if isValid(grid, visited, nrow, ncol):
      diamonds += floodFill(grid, visited, nrow, ncol)
  return diamonds

user_input = open("input6.txt","r")
output = open("output6.txt","w")

R, H = map(int,user_input.readline().strip().split(" "))

data_into_list = user_input.readlines()
grid = [list(line.strip()) for line in data_into_list[0:R+1]]
max_diamonds = 0
visited = [[False for _ in range(H)] for _ in range(R)]
for i in range(R):
    for j in range(H):
        if grid[i][j] != '#' and not visited[i][j]:
            max_diamonds = max(max_diamonds, floodFill(grid, visited, i, j))

output.write(str(max_diamonds))

user_input.close()
output.close()