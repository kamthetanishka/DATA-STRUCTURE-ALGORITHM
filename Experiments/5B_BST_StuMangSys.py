class Node:
    def __init__(self, admission_no):
        self.data = admission_no
        self.left = None
        self.right = None
def insert(root, admission_no):
    if root == None:
        return Node(admission_no)
    if root.data > admission_no:
        root.left = insert(root.left, admission_no)
    else:
        root.right = insert(root.right, admission_no)
    return root
def create():
    root = None
    while True:
        admission_no = int(input("Enter Admission Number (-1 to stop): "))
        if admission_no == -1:
            break
        root = insert(root, admission_no)
    return root
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
class Queue:
    def __init__(self):
        self.R = -1
        self.F = -1
        self.QT = [0] * 5
    def insert(self, admission_node):
        if self.R == 4:
            print("Queue is overflow...")
            return
        self.R = self.R + 1
        self.QT[self.R] = admission_node
        if self.F == -1:
            self.F = 0
    def delete(self):
        if self.F == -1:
            print("Queue is underflow...")
            return
        else:
            admission_node = self.QT[self.F]
            if self.F == self.R:
                self.F = -1
                self.R = -1
            else:
                self.F = self.F + 1
            return admission_node
    def peek(self):
        if self.F == -1:
            print("Queue is empty...")
            return
        else:
            return self.QT[self.F]
    def display(self):
        if self.F == -1:
            print("Nothing to display...")
            return
        for i in range(self.F, self.R + 1):
            print(self.QT[i])
def level_wise(root):
    if root is None:
        return
    q = Queue()
    q.insert(root)
    while q.F != -1:
        admission_node = q.delete()
        print(admission_node.data, end=" ")

        if admission_node.left != None:
            q.insert(admission_node.left)

        if admission_node.right != None:
            q.insert(admission_node.right)
def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)

    return max(left_height, right_height) + 1
def leaf_nodes(root):
    if root is None:
        return

    if root.left == None and root.right == None:
        print(root.data)

    leaf_nodes(root.left)
    leaf_nodes(root.right)

# Student Admission Record Management
admission_root = create()

print("\nAdmission Numbers in Sorted Order:")
inorder(admission_root)

print("\nLevel-wise Admission Records:")
level_wise(admission_root)

print("\nHeight of Admission Tree:")
print(height(admission_root))

print("Leaf Admission Numbers:")
leaf_nodes(admission_root)