class HeapSort:
    # Read array elements
    def read(self):
        self.n = int(input("Enter number of elements: "))
        self.a = []
        print("Enter elements:")
        for i in range(self.n):
            element = int(input())
            self.a.append(element)
    # Maintain Min Heap
    def heapify(self, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.a[left] < self.a[smallest]:
            smallest = left
        if right < n and self.a[right] < self.a[smallest]:
            smallest = right
        if smallest != i:
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            self.heapify(n, smallest)
    # Heap Sort using Min Heap
    def sort(self):
        # Build Min Heap
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)
        # Extract minimum element
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heapify(i, 0)
    # Display sorted array
    def display(self):
        print("\nSorted elements in Descending Order:")
        for i in range(self.n):
            print(self.a[i], end=" ")
        print()
# Main program
h = HeapSort()
h.read()
h.sort()
h.display()

class HeapSort:
    # Read array elements
    def read(self):
        self.n = int(input("Enter number of elements: "))
        self.a = []
        print("Enter elements:")
        for i in range(self.n):
            element = int(input())
            self.a.append(element)
    # Maintain Max Heap
    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.a[left] > self.a[largest]:
            largest = left
        if right < n and self.a[right] > self.a[largest]:
            largest = right
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.heapify(n, largest)
    # Heap Sort using Max Heap
    def sort(self):
        # Build Max Heap
        for i in range(self.n // 2 - 1, -1, -1):
            self.heapify(self.n, i)
        # Extract maximum element
        for i in range(self.n - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heapify(i, 0)
    # Display sorted array
    def display(self):
        print("\nSorted elements in Ascending Order:")
        for i in range(self.n):
            print(self.a[i], end=" ")
        print()
# Main program
h = HeapSort()
h.read()
h.sort()
h.display()