class Plate:
    def __init__(self):
        self.top = -1
        self.ST = [0]*20
        self.categories = {}
    def insert(self,x):
        if self.top == 19:
            print("Stack of plates is Full,No new plate can be added...")
            return        
        if x in self.ST[:self.top+1]:
            print("Duplicate plate cannot be added...")
            return
        category = input("Enter plate category (Steel/Ceramic): ")
        if category not in ["Steel", "Ceramic"]:
            print("Invalid category. Only Steel or Ceramic allowed.")
            return
        self.top = self.top + 1
        self.ST[self.top] = x
        self.categories[x] = category
    def category(self):
        if self.top == -1:
            print("Stack is empty")
            return
        return self.categories.get(self.ST[self.top], "Unknown category")
    def remove(self,y):
        if self.top == -1:
            print("Stack of plates is Empty,No plate can be removed...")
            return
        else:    
            y = self.ST[self.top]
            if y in self.categories:
                del self.categories[y]
            self.top = self.top - 1
        return y
    def peek(self):
        if self.top == -1:
            print("Stack of plates is Empty,No plate can be peeked...")
            return
        return self.ST[self.top]
    def display(self):
        if self.top == -1:
            print("Stack of plates is Empty,No plate can be displayed...")
            return
        for i in range(self.top,-1,-1):
            print(self.ST[i])
p = Plate()
while True:
    print("1. Insert a plate","\n2. Category of plate:","\n3. Remove a plate","\n4. Peek the top plate","\n5. Display all plates","\n6. Exit")
    c = int(input("Enter your choice:"))
    if c == 1:
        x = input("Enter the plate_ID to be inserted:")
        p.insert(x)
    elif c == 2:
        print("Category of plate is:",p.category())
    elif c == 3:
        y = input("Enter the plate_ID to be removed:")
        p.remove(y)
    elif c == 4:
        print("Top plate is:",p.peek())
    elif c == 5:
        print("Plates in the stack are:")
        p.display()
    elif c == 6:
        break
        