n = int(input())
nums = list(map(int, input().split()))
target = int(input())
nums.sort()
closest_sum = float('inf')

for i in range(n-2):
    l,r = i+1, n-1 
    while l < r:
        current =  nums[i]+ nums[l] + nums[r]
        if abs(target- current) < abs(target - closest_sum):
            closest_sum = current
        if current > target:
             r -= 1
        else:
            l += 1
print(closest_sum)