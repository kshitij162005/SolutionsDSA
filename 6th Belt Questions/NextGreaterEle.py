
n1 = int(input())  
nums1 = list(map(int, input().split()))  

n2 = int(input())  
nums2 = list(map(int, input().split()))

next_greater = {}
stack = []

for num in reversed(nums2):

    while stack and stack[-1] <= num:
        stack.pop()
    

    if stack:
        next_greater[num] = stack[-1]
    else:
        next_greater[num] = -1
    
    stack.append(num)

result = [next_greater[num] for num in nums1]
print(" ".join(map(str, result)))
