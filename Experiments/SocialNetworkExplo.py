class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.G = []
    def create(self):
        self.v = int(input("Enter no of users: "))
        self.e = int(input("Enter no of friendship connections: "))
        self.G = [[] for i in range(self.v)]
        for i in range(self.e):
            print("Enter connection", i + 1)
            u = int(input("Enter start vertex: "))
            v = int(input("Enter end vertex: "))
            if u < 0 or u >= self.v or v < 0 or v >= self.v:
                print("Invalid vertex! Enter valid vertices.")
                continue
            self.G[u].append(v)
            self.G[v].append(u)
    def display(self):
        print("Adjacency List:")
        for i in range(self.v):
            print(i, ":", self.G[i])
class Queue:
    def __init__(self):
        self.Q = []
        self.F = -1
        self.R = -1
    def insert(self, x):
        self.Q.append(x)
        self.R += 1
        if self.F == -1:
            self.F = 0
    def delete(self):
        if self.F == -1:
            return None
        x = self.Q[self.F]
        if self.F == self.R:
            self.F = -1
            self.R = -1
            self.Q = []
        else:
            self.F += 1
        return x
def bfs(obj, start):
    visited = [False] * obj.v
    q = Queue()
    q.insert(start)
    visited[start] = True
    print("BFS Traversal:")
    while q.F != -1:
        u = q.delete()
        print(u, end=" ")
        for v in obj.G[u]:
            if visited[v] == False:
                q.insert(v)
                visited[v] = True
    print()
    if False in visited:
        print("Unreachable vertices:", end=" ")
        for i in range(obj.v):
            if visited[i] == False:
                print(i, end=" ")
        print()
obj = Graph()
obj.create()
obj.display()

start = int(input("Enter starting user vertex: "))

if start < 0 or start >= obj.v:
    print("Invalid starting vertex!")
else:
    bfs(obj, start)
