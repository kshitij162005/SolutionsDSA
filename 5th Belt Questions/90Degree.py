a, b = list(map(int, input().split()))
arr = []

for i in range(a):
    row = list(map(int, input().split()))
    arr.append(row)


for i in range(a):
    for j in range(i):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]  

for i in range(a):
    arr[i].reverse()

for i in range(a):
    for j in range(b):
        print(arr[i][j], end=" ")
    print()


