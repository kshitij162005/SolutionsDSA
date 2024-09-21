a = int(input())
b = list(map(int, input().split()))
c = int(input())

d = 1
e = max(b)
while d < e:
    mid = (d + e) // 2
    if sum((j + mid - 1) // mid for j in b) > c:
        d = mid + 1
    else:
        e = mid
print(d)
