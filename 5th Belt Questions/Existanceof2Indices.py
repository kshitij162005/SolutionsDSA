a = int(input())
b = list(map(int, input().split()))
c = int(input())
d = 1

arr = []

for i in range(a):
    for j in range(i+1):
        if i != j and b[i] - b[j] == c:
            arr.append(1)

if d in arr:
    print("1")
else:
    print("0")
