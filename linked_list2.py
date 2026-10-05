class Node:
    def __init__(self, data):  
        self.data = data
        self.left = None
        self.right = None

def create():
    n = int(input("Enter number of nodes: "))
    values = list(map(int, input("Enter values separated by space: ").split()))

    nodes = []
    for value in values:
        if value == -1:
            nodes.append(None)
        else:
            nodes.append(Node(value))

    for i in range(n):
        if nodes[i] is not None:
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n:
                nodes[i].left = nodes[left]
            if right < n:
                nodes[i].right = nodes[right]

    return nodes[0]

def preorder(temp):
    if temp is not None:
        print(temp.data, end=" ")
        preorder(temp.left)
        preorder(temp.right)

def inorder(temp):
    if temp is not None:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)

def postorder(temp):
    if temp is not None:
        postorder(temp.left)
        postorder(temp.right)
        print(temp.data, end=" ")


root = create()

print("\nPreorder Traversal:")
preorder(root)
print("\nInorder Traversal:")
inorder(root)
print("\nPostorder Traversal:")
postorder(root)

