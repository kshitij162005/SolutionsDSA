# Solved

from collections import deque

size = int(input()) 
nums = list(map(int, input().split())) 
k = int(input())  

dq = deque()
for i in range(size):
    if dq and dq[0] == i - k:  
        dq.popleft()
    while dq and nums[dq[-1]] < nums[i]: 
        dq.pop()
    dq.append(i)
    if i >= k - 1:  
        print(nums[dq[0]], end="")