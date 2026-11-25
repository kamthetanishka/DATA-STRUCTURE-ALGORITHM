class HashTable:
    def __init__(self):
        self.size = 10
        self.hash = [-1] * self.size
    def insert_without_replacement(self, key):
        index = key % self.size
        if self.hash[index] == -1:
            self.hash[index] = key
            return
        i = (index + 1) % self.size
        while self.hash[i] != -1 and i != index:
            i = (i + 1) % self.size
        if self.hash[i] == -1:
            self.hash[i] = key
        else:
            print("Hash Table is Full!")
    def insert_with_replacement(self, key):
        index = key % self.size
        if self.hash[index] == -1:
            self.hash[index] = key
            return
        if self.hash[index] % self.size != index:
            temp = self.hash[index]
            self.hash[index] = key
            print(temp, "is displaced from index", index)
            i = (index + 1) % self.size
            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size
            if self.hash[i] == -1:
                self.hash[i] = temp
            else:
                print("Hash Table is Full!")
        else:
            i = (index + 1) % self.size
            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size
            if self.hash[i] == -1:
                self.hash[i] = key
            else:
                print("Hash Table is Full!")
    def search(self, key):
        index = key % self.size
        i = index
        while self.hash[i] != -1:
            if self.hash[i] == key:
                print(key, "found at index", i)
                return
            i = (i + 1) % self.size
            if i == index:
                break
        print(key, "not found")
    def display(self):
        print("\nIndex\tValue")
        for i in range(self.size):
            if self.hash[i] == -1:
                print(i, "\tEmpty")
            else:
                print(i, "\t", self.hash[i])
# Main Program
print("1. Linear Probing Without Replacement")
print("2. Linear Probing With Replacement")
choice = int(input("Enter your choice: "))
h = HashTable()
n = int(input("Enter number of application numbers: "))
print("Enter application numbers:")
for i in range(n):
    key = int(input())
    if choice == 1:
        h.insert_without_replacement(key)
    elif choice == 2:
        h.insert_with_replacement(key)
    else:
        print("Invalid choice!")
        break
h.display()
key = int(input("\nEnter application number to search: "))
h.search(key)
