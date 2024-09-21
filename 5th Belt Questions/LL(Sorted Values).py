class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is  None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def sorting(self):
        curr = self.head
        while curr is not None:
            mini = curr
            next_node = curr.next
            while next_node is not None:
                if next_node.data < mini.data:
                    mini = next_node
                next_node = next_node.next
            curr.data, mini.data = mini.data, curr.data
            curr = curr.next

    def display(self):
        curr = self.head
        if curr is None:
            print(" ")
            return
        
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next
        print()

N = int(input())
if N == 0:
    print(" ")
else:
    ll = LinkedList()
    nums = list(map(int, input().split()))

    for i in nums:
        ll.insert(i)
    ll.sorting() 
    ll.display()
