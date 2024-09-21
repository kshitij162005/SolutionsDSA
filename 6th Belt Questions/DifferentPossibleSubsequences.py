N = int(input())  # Input size
nums = list(map(int, input().split()))
subsequences = set() 

def rec(idx, arr):
    if len(arr) > 1:
        subsequences.add(tuple(arr)) 
    
    for i in range(idx, N):
        if not arr or nums[i] >= arr[-1]: 
            rec(i + 1, arr + [nums[i]])

for i in range(N):
    rec(i + 1, [nums[i]])

sorted_subsequences = sorted(list(subsequences))

for subsequence in sorted_subsequences:
    print(' '.join(map(str, subsequence)))
