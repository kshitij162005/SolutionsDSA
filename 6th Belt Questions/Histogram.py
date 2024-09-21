# Solved

n = int(input())  
heights = list(map(int, input().split()))  

stack = []
max_area = 0  
index = 0

while index < n:
    if not stack or heights[index] >= heights[stack[-1]]:
        stack.append(index)
        index += 1
    else:
        top_of_stack = stack.pop()
        area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
        max_area = max(max_area, area)

while stack:
    top_of_stack = stack.pop()
    area = heights[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
    max_area = max(max_area, area)
print(max_area)