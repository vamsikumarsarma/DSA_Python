class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_beg(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def add_end(self,data):
        if self.head is None:
            print("LL is empty")
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
    def ll_length(self):
        if self.head is None:
            print("LL is empty")
        else:
            temp = self.head
            while temp:
                self.length += 1
                temp = temp.next
            print("Lenth of LL is: ", self.length)
    def display(self):
        if self.head is None:
            print("SLL is empty")
        else:
            temp_node = self.head
            while temp_node:
                print(temp_node.data)
                temp_node = temp_node.next
               
ll = Linkedlist()
ll.add_beg(40)
ll.add_beg(30)
ll.add_beg(20)
ll.add_end(50)
ll.ll_length()
ll.display()