def maxConsecutiveOnes(nums, k):
    left = 0
    max_length = 0
    zero_count = 0

    # Iterate through the nums array
    for right in range(len(nums)):
        # If we encounter a 0, increase the zero_count
        if nums[right] == 0:
            zero_count += 1

        # If the zero_count exceeds k, shrink the window from the left
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update the maximum length of the window
        max_length = max(max_length, right - left + 1)

    return max_length

# Taking plain input from the user
n = int(input())  # Array size
nums = list(map(int, input().strip()))  # Binary array as a single string of numbers
k = int(input())  # Maximum number of flips

# Call the function and print the result
print(maxConsecutiveOnes(nums, k))
