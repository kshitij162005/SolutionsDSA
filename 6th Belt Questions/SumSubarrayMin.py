MOD = 10**9 + 7

n = int(input()) 
arr = list(map(int, input().split()))  

sum_min = 0
stack = []

prev_smaller = [0] * n
next_smaller = [0] * n

for i in range(n):
    while stack and arr[stack[-1]] >= arr[i]:
        stack.pop()
    prev_smaller[i] = i - stack[-1] if stack else i + 1
    stack.append(i)

stack = []

for i in range(n - 1, -1, -1):
    while stack and arr[stack[-1]] > arr[i]:
        stack.pop()
    next_smaller[i] = stack[-1] - i if stack else n - i
    stack.append(i)

for i in range(n):
    sum_min = (sum_min + arr[i] * prev_smaller[i] * next_smaller[i]) % MOD  
print(sum_min)
