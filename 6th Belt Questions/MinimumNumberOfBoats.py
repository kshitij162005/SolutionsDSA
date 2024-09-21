n,limit = list(map(int, input().split()))
people =list(map(int, input().split()))
boats = 0
b = len(people)

for i in range(b):
    for j in range(0,b-i-1):
        if people[j] > people[j+1]:
            people[j], people[j+1] = people[j+1], people[j]
l,r = 0, n-1

while l <= r:
    if people[l] + people[r] <= limit:
        l += 1
        r -= 1

    else:
        r -= 1
    boats += 1


print(boats)