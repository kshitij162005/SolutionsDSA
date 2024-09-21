# a = int(input())

# stack = []
# arr = []

# for i in range(a):
#     query = list(map(int, input().split()))

#     if query[0] == 1:
#         val = query[1]
#         stack.append(val)
#     elif query[0] == 2:
#         if stack:
#             popped = stack.pop()
#             arr.append(popped)
#         else:
#             arr.append(-1)

#     elif query[0] == 3: 
#         if stack:
#             arr.append(min(stack))
#         else:
#             arr.append(-1)

# print(*arr)



def Stack():
    stack=[]
    return stack

def push(stack, n):
    stack.append(int(n))

def pop(stack):
    if len(stack) == 0:
        return -1
    return stack.pop()

def getMin(stack):
    if len(stack)==0:
      return -1
        
    else:
        return min(stack)
def check(arr,stack):
  arr1=[]
  for i in arr:
    if i[0] == '1':
        push(stack, i[1])
    elif i[0] == '2':
        arr1.append(pop(stack))
    elif i[0] == '3':
        arr1.append(getMin(stack))
  return arr1

n = int(input())
stack = Stack()
arr=[]
for i in range(n):
    arr.append(input().split())
k=check(arr,stack)
print(*k)
