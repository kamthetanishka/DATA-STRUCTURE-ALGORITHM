class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = []
    def create(self):
        self.v = int(input("Enter no of intersections: "))
        self.e = int(input("Enter no of roads: "))
        self.G = [[0 for i in range(self.v)] for j in range(self.v)]
        for i in range(self.e):
            print("Enter road", i + 1)
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            if u < 0 or u >= self.v or v < 0 or v >= self.v:
                print("Invalid vertex! Enter valid vertices.")
                continue
            self.G[u][v] = 1
            self.G[v][u] = 1
    def display(self):
        print("Adjacency Matrix:")
        for i in range(self.v):
            for j in range(self.v):
                print(self.G[i][j], end=" ")
            print()
class Stack:
    def __init__(self):
        self.st = []
        self.TOP = -1
    def push(self, x):
        self.st.append(x)
        self.TOP += 1
    def pop(self):
        if self.TOP == -1:
            return None
        x = self.st[self.TOP]
        self.TOP -= 1
        return x
def dfs(obj, start):
    visited = [False] * obj.v
    s = Stack()
    s.push(start)
    print("DFS Traversal:")
    while s.TOP != -1:
        u = s.pop()
        if visited[u] == False:
            print(u, end=" ")
            visited[u] = True
            for v in range(obj.v - 1, -1, -1):
                if obj.G[u][v] != 0 and visited[v] == False:
                    s.push(v)
    print()
    if False in visited:
        print("Disconnected vertices:", end=" ")
        for i in range(obj.v):
            if visited[i] == False:
                print(i, end=" ")
        print()
obj = Graph()
obj.create()
obj.display()
start = int(input("Enter starting intersection: "))
if start < 0 or start >= obj.v:
    print("Invalid starting vertex!")
else:
    dfs(obj, start)
