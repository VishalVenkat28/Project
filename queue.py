class Queue:

    def __init__(self):
        self.items = []
        self.marker = -1 

    def enqueue(self, data):
        self.items.append(data)
    
    def dequeue(self):
        if len(self.items) == 0:
            print('Queue is empty!')
            return
        self.items.pop(0)
    
    def printQueue(self):
        for ele in (self.items):
            print(ele, end=' ')
        print()
    
if __name__ == "__main__":
    ob = Queue()
    ob.enqueue(23)
    ob.enqueue(65)
    ob.enqueue('cat')
    ob.printQueue()
    ob.enqueue('hurah!')
    ob.dequeue()
    ob.printQueue()
