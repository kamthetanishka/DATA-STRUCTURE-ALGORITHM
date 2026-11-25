class HashTable:
    # Initialize hash table
    def __init__(self):
        self.size = 10
        self.hash = [-1] * self.size
    # Insert key without replacement
    def insert(self, key):
        index = key % self.size
        start = index
        while self.hash[index] != -1:
            index = (index + 1) % self.size
            if index == start:
                print("Hash Table is Full!")
                return
        self.hash[index] = key
        print(key, "inserted at index", index)
    # Display hash table
    def display(self):
        print("\nIndex\tValue")
        for i in range(self.size):
            if self.hash[i] == -1:
                print(i, "\tEmpty")
            else:
                print(i, "\t", self.hash[i])
# Main program
h = HashTable()
n = int(input("Enter number of keys: "))
print("Enter keys:")
for i in range(n):
    key = int(input())
    h.insert(key)
h.display()

# Create a hash table and handle collisions using linear probing with replacement
class HashTable:
    # Initialize hash table
    def __init__(self):
        self.size = 10
        self.hash = [-1] * self.size
    # Insert key with replacement
    def insert(self, key):
        index = key % self.size
        # If position is empty
        if self.hash[index] == -1:
            self.hash[index] = key
            return
        # Check whether existing key belongs to a different hash address
        if self.hash[index] % self.size != index:
            temp = self.hash[index]

            # Replace existing key
            self.hash[index] = key
            print(temp, "is displaced from index", index)

            # Find next empty position
            i = (index + 1) % self.size
            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size
            if self.hash[i] == -1:
                self.hash[i] = temp
            else:
                print("Hash Table is Full!")
        else:
            # Normal linear probing
            i = (index + 1) % self.size
            while self.hash[i] != -1 and i != index:
                i = (i + 1) % self.size
            if self.hash[i] == -1:
                self.hash[i] = key
            else:
                print("Hash Table is Full!")
    # Display hash table
    def display(self):
        print("\nIndex\tValue")
        for i in range(self.size):
            if self.hash[i] == -1:
                print(i, "\tEmpty")
            else:
                print(i, "\t", self.hash[i])
# Main program
h = HashTable()
n = int(input("Enter number of keys: "))
print("Enter keys:")
for i in range(n):
    key = int(input())
    h.insert(key)
h.display()