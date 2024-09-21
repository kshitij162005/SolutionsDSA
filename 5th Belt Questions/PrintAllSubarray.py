a = int(input())
b = list(map(int, input().split()))
for i in range(a):
    for j in range(i+1, a+1):
        c = b[i:j]
        for num in c:
            print(num,end=" ")
        print()
