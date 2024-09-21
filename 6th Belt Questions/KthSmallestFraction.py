import heapq

n, k = map(int, input().split())
arr = list(map(int, input().split()))

fractions = []
for i in range(n):
    for j in range(i + 1, n):
        fractions.append((arr[i] / arr[j], arr[i], arr[j]))

fractions.sort()
kth = fractions[k - 1]
print(f"{kth[1]} {kth[2]}")
