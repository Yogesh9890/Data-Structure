class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def get_length(self):
        count = 0
        n = self.head
        while n:
            count+=1
            n = n.next    


    def print_ll(self):
        if self.head is None:
            print("Linked List is empty!!")
        else:
            n = self.head
            llstr = ''
            while n is not None:
                llstr += str(n.data)+' --> ' if n.next else str(n.data)
                n = n.next
            print(llstr)


    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head= node
            return
        
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = node   
 

    def insert_at(self, index, data):
        if index<0:
            raise Exception("Invalide index!!")

        if index == 0:
            self.insert_at_begining(data)
            return 

        n = self.head
        count = 0
        while n:
            if count == index -1:
                node = Node(data, n.next)
                n.next = node
                break
            n = n.next
            count += 1  

    def remove_at(self, index):
        if index<0:
            raise Exception("Invalide index!!")
        n = self.head
        if index == 0:
            n = self.next
            return
        count = 0
        while n:
            if count == index - 1:
                n.next = n.next.next
                break
            n = n.next
            count += 1   


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



ll = LinkedList()
ll.insert_at_begining(50)
ll.insert_at_end(31)
ll.insert_at_begining(21)
ll.insert_at(1, 100)
ll.print_ll()

ll1 = LinkedList()
ll1.insert_values(["banana","mango","grapes","orange"])
ll1.insert_at(1,"blueberry")
ll1.remove_at(2)
ll1.print_ll()

ll1.insert_values([45,7,12,567,99])
ll1.insert_at_end(67)
ll1.print_ll()