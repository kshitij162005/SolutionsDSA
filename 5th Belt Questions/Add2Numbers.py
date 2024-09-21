class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def display(self):
        curr = self.head
        if curr is None:
            print(" ")
            return
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print()


def reverse_linked_list(linked_list):
    prev = None
    curr = linked_list.head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    linked_list.head = prev


def addtwoLists(first, second):
    result = LinkedList()
    carry = 0

    reverse_linked_list(first)
    reverse_linked_list(second)

    first_curr = first.head
    second_curr = second.head


    while first_curr is not None or second_curr is not None or carry != 0:
        first_data = first_curr.data if first_curr else 0
        second_data = second_curr.data if second_curr else 0

        total = first_data + second_data + carry
        carry = total // 10
        result.insert(total % 10)

        if first_curr != None:
            first_curr = first_curr.next
        if second_curr != None:
            second_curr = second_curr.next

    reverse_linked_list(result)
    return result


# Input handling
n = int(input())
arr1 = list(map(int, input().split())) 
m = int(input())  
arr2 = list(map(int, input().split()))  

first_list = LinkedList()
for num in arr1:
    first_list.insert(num)

second_list = LinkedList()
for num in arr2:
    second_list.insert(num)

result_list = addtwoLists(first_list, second_list)

result_list.display()
