class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sortList(head):
    count = [0, 0, 0]  
    
    current = head
    
    while current:
        count[current.data] += 1
        current = current.next
    
    current = head
    i = 0
    while current:
        if count[i] == 0:
            i += 1
        else:
            current.data = i
            count[i] -= 1
            current = current.next

    return head

def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for val in arr[1:]:
        current.next = Node(val)
        current = current.next
    return head

def printList(head):
    current = head
    while current:
        print(current.data, end='')
        current = current.next
    print()

n = int(input())  
elements = list(map(int, input().split()))  

head = createLinkedList(elements)

sorted_head = sortList(head)

printList(sorted_head)
