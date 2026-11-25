class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
# Insert node into BST
def insert(root, x):
    if root is None:
        return Node(x)
    if root.data < x:
        root.right = insert(root.right, x)
    elif root.data > x:
        root.left = insert(root.left, x)
    else:
        print("Duplicate value not allowed")
    return root
# Create BST
def create():
    root = None
    while True:
        x = int(input("Enter roll number (0 to stop): "))
        if x == 0:
            break
        root = insert(root, x)
    return root

def inorder(root):
    stack = []
    current = root
    if root is None:
        print("Tree is empty")
        return
    print("Inorder Traversal:")
    while current is not None or len(stack) > 0:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.data, end=" ")
        current = current.right
    print()

def preorder(root):
    if root is None:
        print("Tree is empty")
        return
    stack = [root]
    print("Preorder Traversal:")
    while len(stack) > 0:
        current = stack.pop()
        print(current.data, end=" ")
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    print()

root = create()
inorder(root)
preorder(root)
