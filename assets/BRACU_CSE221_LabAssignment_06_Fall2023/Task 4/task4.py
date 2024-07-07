class lowestCost:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
        self.arr = []
        self.weight = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, w):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            if self.size[parent_x] < self.size[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]
            self.weight += w

    def findMinCost(self):
        self.arr.sort(key = lambda x:x[-1])

        for i in self.arr:
            x = i[0]
            y = i[1]
            weight = i[-1]
            self.union(x, y, weight)
        return self.weight



user_input = open("input4.txt", "r")
output = open("output4.txt", "w")



city, road = map(int, user_input.readline().split())
common = lowestCost(city)
for i in range(road):
    x, y, weight = map(int, user_input.readline().split())
    common.arr.append((x,y,weight))
result = common.findMinCost()
output.write(f"{result}")



user_input.close()
output.close()