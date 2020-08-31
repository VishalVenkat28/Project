class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LinkedList:

    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def insertAtEnd(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next 
        itr.next = Node(data, None)

    def getLength(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        return count

    def insertAtIndex(self, index, data):
        if index < 0 or index > self.getLength():
            print('Index is not valid!')
            return

        if index == 0:
            self.insertAtBeginning(data)
        
        count = 0
        itr = self.head
        while itr:
            if  count == index - 1:
                newNode = Node(data, None)
                newNode.next = itr.next
                itr.next = newNode
                break

            itr = itr.next
            count += 1


    def removeFromIndex(self, index):
        if index < 0 or index > self.getLength():
            print('Index is not valid!')

        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def printList(self):
        if self.head is None:
            print('List is empty!')
            return
        
        itr = self.head
        llstr= ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        llstr += 'None'
        print(llstr)

if __name__ == "__main__":
    ob = LinkedList()
    ob.insertAtBeginning(65)
    ob.insertAtBeginning(5)
    ob.insertAtBeginning(97)
    ob.insertAtEnd(69)
    ob.insertAtEnd(22)
    ob.insertAtEnd(666)
    ob.printList()
    print('Length of linked list', ob.getLength())
    ob.removeFromIndex(2)
    ob.removeFromIndex(2)
    ob.insertAtIndex(2, 'cat')
    ob.insertAtIndex(5, 'yay!')
    ob.printList()