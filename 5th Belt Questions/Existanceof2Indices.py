a = int(input())
b = list(map(int, input().split()))
c = int(input())

if a == 0 or len(b) == 0:
    print(-1)
else:
    found = False
    for i in range(a-1):
        for j in range(i+1):
            if b[i] + b[j] == c:
                print(j,i)
                found = True
                break
        if found:
            break
    if not found:
        print(-1)
