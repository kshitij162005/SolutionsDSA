# Solved


n = int(input())
heights = list(map(int, input().split()))  


left = 0
right = len(heights) - 1
left_max = heights[left]
right_max = heights[right]
water = 0


while left < right:
    if left_max < right_max:
        left += 1
        left_max = max(left_max, heights[left])
        water += left_max - heights[left]
    else:
        right -= 1
        right_max = max(right_max, heights[right])
        water += right_max - heights[right]


print(water) 