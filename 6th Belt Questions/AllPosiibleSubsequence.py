a = input()
sub = ['']

for i in a:
    sub += [m + i for m in sub]

n = len(sub)

for i in range(n):
    for j in range(0, n-i-1):
        if sub[j] > sub[j+1]:
            sub[j], sub[j+1] = sub[j+1], sub[j]


fil = [m for m in sub if m]

print(*fil)
