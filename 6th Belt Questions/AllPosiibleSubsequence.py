a = int(input())
array = list(map(int, input().split()))

subsets = []
n = len(array)
for i in range(1 << n): 
    subset = []
    for j in range(n):
        if i & (1 << j):
            subset.append(array[j])
    if subset:
        subsets.append(subset)

subsets.sort()

for i in subsets:
    print(*i)
