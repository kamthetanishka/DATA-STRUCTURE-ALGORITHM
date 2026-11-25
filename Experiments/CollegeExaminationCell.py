class HeapSort:
    def read(self):
        self.n = int(input("Enter number of students: "))
        self.a = []
        print("Enter student marks:")
        for i in range(self.n):
            element = int(input())
            self.a.append(element)
        self.original = self.a.copy()
    def min_heapify(self, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.a[left] < self.a[smallest]:
            smallest = left
        if right < n and self.a[right] < self.a[smallest]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.min_heapify(n, smallest)
    def min_sort(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.min_heapify(self.n, i)
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.min_heapify(i, 0)
    def max_heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.a[left] > self.a[largest]:
            largest = left
        if right < n and self.a[right] > self.a[largest]:
            largest = right
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.max_heapify(n, largest)
    def max_sort(self):
        for i in range(self.n // 2 - 1, -1, -1):
            self.max_heapify(self.n, i)
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.max_heapify(i, 0)
    def display(self):
        print("\nOriginal Marks:", self.original)
        print("Sorted Marks:", self.a)
h = HeapSort()
h.read()
print("\n1. Min Heap (Descending Order)")
print("2. Max Heap (Ascending Order)")
choice = int(input("Enter your choice: "))
if choice == 1:
    h.min_sort()
    print("\nSorting using Min Heap")
    h.display()
elif choice == 2:
    h.max_sort()
    print("\nSorting using Max Heap")
    h.display()
else:
    print("Invalid choice!")
