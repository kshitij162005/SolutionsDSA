n,k = list(map(int, input().split()))
nums = list(map(int, input().split()))

count = 0
i = 0

# here below len(nums) only woek but not n
while i < len(nums):
    found = False
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == k:
            count += 1
            nums.pop(j)
            nums.pop(i)
            found = True
            break
    if not found:
        i += 1

print(count)
