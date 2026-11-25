class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, x):
    if root is None:
        return Node(x)
    if root.data > x:
        root.left = insert(root.left, x)
    elif root.data < x:
        root.right = insert(root.right, x)
    else:
        print("Duplicate element not allowed")
    return root
def create():
    root = None
    while True:
        x = int(input("Enter employee ID (-1 to stop): "))
        if x == -1:
            break
        root = insert(root, x)
    return root
class Queue:
    def __init__(self):
        self.R = -1
        self.F = -1
        self.QT = [0] * 100
    def insert(self, x):
        if self.R == 99:
            print("Queue is overflow...")
            return
        self.R = self.R + 1
        self.QT[self.R] = x
        if self.F == -1:
            self.F = 0
    def delete(self):
        if self.F == -1:
            print("Queue is underflow...")
            return None
        y = self.QT[self.F]
        if self.F == self.R:
            self.F = -1
            self.R = -1
        else:
            self.F = self.F + 1
        return y
# Level-wise traversal
def level_wise(root):
    if root is None:
        print("Tree is empty")
        return
    q = Queue()
    q.insert(root)
    while q.F != -1:
        r = q.delete()
        print(r.data, end=" ")
        if r.left is not None:
            q.insert(r.left)
        if r.right is not None:
            q.insert(r.right)
    print()
def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1
def leaf_nodes(root):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
    leaf_nodes(root.left)
    leaf_nodes(root.right)
print("Create Original BST")
r = create()
print("\nOriginal BST Level-wise:")
level_wise(r)
print("\nCreate New BST")
r1 = None
if r is not None:
    q = Queue()
    q.insert(r)
    while q.F != -1:
        temp = q.delete()
        r1 = insert(r1, temp.data)
        if temp.left is not None:
            q.insert(temp.left)
        if temp.right is not None:
            q.insert(temp.right)
print("\nNew BST Level-wise:")
level_wise(r1)
print("\nHeight of Original BST:")
print(height(r))
print("Leaf Nodes of Original BST:")
leaf_nodes(r)
print()
