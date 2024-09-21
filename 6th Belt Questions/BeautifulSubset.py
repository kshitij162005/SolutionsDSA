n, k = map(int, input().split())
nums = list(map(int, input().split()))  

beautiful_count = 0

for mask in range(1, 1 << n):
    subset = []
    
    for i in range(n):
        if mask & (1 << i):
            subset.append(nums[i])
    
    is_beautiful = True
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if abs(subset[i] - subset[j]) == k:
                is_beautiful = False
                break
        if not is_beautiful:
            break
    
    if is_beautiful:
        beautiful_count += 1

print(beautiful_count)
