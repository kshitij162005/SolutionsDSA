# class Node:
#   def __init__(self, data):
#       self.data = data
#       self.next = None
#       self.prev = None

# class DoubleLinkedList:
#   def __init__(self):
#       self.head = None

#   def insert(self, data):
#       new_node = Node(data)
#       if self.head is None:
#           self.head = new_node
#       else:
#           curr = self.head
#           while curr.next is not None:
#               curr = curr.next
#           curr.next = new_node
#           new_node.prev = curr

#   def reverse(self):
#       curr, prev = self.head, None
#       while curr:
#           curr.next, curr.prev, prev, curr = prev, curr.next, curr, curr.next
#       self.head = prev

#   def display(self):
#       curr = self.head
#       if curr is None:
#           print(" ")
#       while curr is not None:
#           print(curr.data, end=" ")
#           curr = curr.next
#       print()

# N = int(input())
# if N <= 0:
#   print(" ")
# else:
#   ll = DoubleLinkedList()
#   nums = list(map(int, input().split()))

#   for i in nums:
#       ll.insert(i)
#   ll.reverse()
#   ll.display()


class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class LinkedList:
    def __init__(self):
       self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                 curr = curr.next
            curr.next = new_node
            new_node.prev = curr

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            curr.next, curr.prev, prev, curr = prev, curr.next, curr, curr.next
        self.head = prev

    def display(self):
        curr = self.head
        if curr is None:
            print(" ")
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


N = int(input())
nums = list(map(int, input().split()))

if N <= 0:
    print(" ")
else:
    ll = LinkedList()
    for i in nums:
        ll.insert(i)
    ll.reverse()
    ll.display()

        
      