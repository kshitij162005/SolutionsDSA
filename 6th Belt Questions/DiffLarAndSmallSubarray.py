n = int(input())  
nums = list(map(int, input().split())) 

total = 0

for i in range(n):
    for j in range(i, n):
        subarray = nums[i:j+1]
        diff = max(subarray) - min(subarray)
        total += diff

print(total)
