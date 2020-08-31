class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)
    
    def pop(self):
        if len(self.items) == 0:
            print('Stack is empty!')
            return
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def printStack(self):
        for elem in (self.items):
            print(elem, end =' ')
        print()


def isMatch(ch1, ch2):
    dict = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    return dict[ch1] == ch2

def isBalanced(expr):

    stack = Stack()
    for ch in expr:
        if ch == '(' or ch == '{' or ch == '[':
            stack.push(ch)

        if ch ==')' or ch =='}' or ch == ']':
            if stack.isEmpty():
                return False
            if not isMatch(ch, stack.pop()):
                return False
    return True

if __name__ == "__main__":
    
    expr = input('Enter the expression to check: ')
    print(isBalanced(expr))