class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    slow = fast = head

    # Move 'fast' by 2 steps and 'slow' by 1 step
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 'slow' will now be at the middle node
    return slow

# Helper function to create the linked list from the input list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Taking input
n = int(input())  # Number of elements in the linked list
elements = list(map(int, input().split()))  # List elements as a single input

# Create the linked list
head = createLinkedList(elements)

# Get the middle node
middle = middleNode(head)

# Output the value of the middle node
print(middle.data)
