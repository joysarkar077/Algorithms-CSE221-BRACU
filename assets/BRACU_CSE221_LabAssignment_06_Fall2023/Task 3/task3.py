class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            if self.size[parent_x] < self.size[parent_y]:
                parent_x, parent_y = parent_y, parent_x
            self.parent[parent_y] = parent_x
            self.size[parent_x] += self.size[parent_y]

def friendCircleSize(N, queries):
    uf = UnionFind(N)
    result = []

    for query in queries:
        a, b = query
        uf.union(a - 1, b - 1)
        result.append(uf.size[uf.find(a - 1)])

    return result



user_input = open("input3.txt", "r")
output = open("output3.txt", "w")



N, M = map(int, user_input.readline().split())
array = []
for i in range(M):
    array += [user_input.readline()]

queries =[tuple(map(int, i.split())) for i in array]

output1 = friendCircleSize(N, queries)
for size in output1:
    output.write(f"{size}\n")
    
    

user_input.close()
output.close()