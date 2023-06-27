class Node:
    def __init__(self, value=None):  # we write not the next  varibale becasue we dont want to the user to set the next value. we want to set it automatically.
        self.value = value # Assign value to node 
        self.next = None # Initialize next as null 


# create class for Singly Linked List
class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    ''' 
    __iter__ method to make our linked list iterable, so we can loop through it and print it out. we use the generator function to do that. 
    because we donot want to store the whole linked list in memory. we want to store one node at a time in memory. 
    '''

    def __iter__(self):
        node = self.head # we set the node to the head of the linked list
        while node: # while node is not null 

            '''
            yield: is used to return from a function without destroying the states of its local variable and when the function is called, the execution starts from the last yield statement.
            return: return statement terminates a function entirely. the yield statement pauses the function saving all its states and later continues from there on successive calls.
            '''

            yield node # yield the node so here the function stops here temporarily and then it will continue from here on the next iteration.
            node = node.next


    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traverse Singly Linked List
    
    def traverseList(self):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

 # Search for a node in Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The node does not exist in this SLL"
    # Delete a node from Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            return "The Singly Linked List does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(44,6)
print([node.value for node in singlyLinkedList]) 

# node1 = Node(1)
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2

singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
print([node.value for node in singlyLinkedList]) 
singlyLinkedList.insertSLL(5,3)
print([node.value for node in singlyLinkedList]) 

