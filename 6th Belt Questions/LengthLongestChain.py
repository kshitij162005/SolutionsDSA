n = int(input())
pairs = []

for i in range(n): 
    pair = list(map(int, input().split()))
    pairs.append(pair)

pairs.sort()
last = pairs[0]
cnt = 1

for i in range(1, len(pairs)):
    if last[-1] < pairs[i][0]:
        last = pairs[i]
        cnt += 1
    elif last[-1] > pairs[i][-1]:
        last = pairs[i]

print(cnt)