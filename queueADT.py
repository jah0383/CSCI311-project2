class element:
    def __init__(self, data, key):
        self.data = data
        self.key = key
    
    def __lt__(self, other):
        return (self.key < other.key)

class PQueue():
    def __init__(self):
        self.queue = MinHeap()

    def enqueue(self, x):
        self.queue.insert(x)

    def dequeue(self):
        return self.queue.extractTop()

    def __str__(self):
        return str(self.queue)
        



class Heap():
    def __init__(self):
        self.heap = []
        self.size = -1
    
    def insert(self, p):
        self.size += 1
        self.heap.append(p)
        self.shiftUp(self.size)
        
    def extractTop(self):
        result = self.heap[0]
        if self.size != 0:
            self.heap[0] = self.heap.pop(self.size)
            self.size -= 1
            self.shiftDown(0)
        else: 
            self.heap = []
            self.size -= 1
        

        
        return result

    def remove(self, i):
        return 0
    
    def getMax(self):
        return 0

    def changePriority(self, i, p):
        pass

    def search(self, e):
        try:
            return [n[0] for n in self.heap].index(e)
        except Exception as e:
            return -1


    def parentIndex(self, i):
        return (i-1)//2
    def leftChildIndex(self, i):
        return (2*i)+1
    def rightChildIndex(self, i):
        return (2*i)+2

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def __str__(self):
        result = "["
        for x in self.heap:
            result += "data: {}, key: {}\n".format(str(x.data),str(x.key))
        result += "]"
        return result

class MaxHeap(Heap):
    def __init__(self):
        super.__init__()


    def shiftUp(self, i):
        """
        Private method which just shifts to maintain the max heap property
        """
        while(i > 0 and self.heap[self.parentIndex(i)][1] < self.heap[i][1]):
            self.swap(i, self.parentIndex(i))
            i = self.parentIndex(i)

    def shiftDown(self, i):
        """
        Private method which shifts the given indexed element down to 
        maintain the max heap property
        """
        maxIndex = i

        l = self.leftChildIndex(i)
        if (l <= self.size and self.heap[l] > self.heap[maxIndex]):
            maxIndex = l 

        r = self.rightChildIndex(i)
        if (r <= self.size and self.heap[r] > self.heap[maxIndex]):
            maxIndex = r

        if (i != maxIndex):
            self.swap(i, maxIndex)
            self.shiftDown(maxIndex)

class MinHeap(Heap):
    def __init__(self):
        super().__init__()

    # def heapify(self, i):
    #     if self.heap

    def shiftUp(self, i):
        """
        Private method which just shifts to maintain the max heap property
        """
        while(i > 0 and self.heap[(i-1)//2][1] > self.heap[i][1]):
            self.swap(i, self.parentIndex(i))
            i = self.parentIndex(i)

    def shiftDown(self, i):
        """
        Private method which shifts the given indexed element down to 
        maintain the max heap property
        """
        maxIndex = i

        l = self.leftChildIndex(i)
        if (l <= self.size and self.heap[l] < self.heap[maxIndex]):
            maxIndex = l 

        r = self.rightChildIndex(i)
        if (r <= self.size and self.heap[r] < self.heap[maxIndex]):
            maxIndex = r
        if (i != maxIndex):
            self.swap(i, maxIndex)
            self.shiftDown(maxIndex)
