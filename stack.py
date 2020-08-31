class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if len(self.items) == 0:
            print('Stack is empty!')
            return
        self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def printStack(self):
        for elem in (self.items):
            print(elem, end =' ')
        print()

if __name__ == "__main__":
    ob = Stack()
    ob.push(65)
    ob.push(45)
    ob.push(33)
    ob.pop()
    # ob.pop()
    # ob.pop()
    ob.printStack()
    ob.pop()
    ob.push(66)
    ob.push('cat')
    ob.push('yay!')
    print(ob.top())
    ob.pop()
    ob.printStack()
    print(ob.isEmpty())

