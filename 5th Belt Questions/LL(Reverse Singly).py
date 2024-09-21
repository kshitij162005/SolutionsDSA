class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

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

  def reverse(self):
        prev, curr = None, self.head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        self.head = prev

  def display(self):
        curr = self.head
        if curr is None:
            print(" ")
            return
        
        while curr != None:
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
    ll.reverse() 
    ll.display()





