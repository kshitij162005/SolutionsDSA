nums = input()
a = int(input())
res = []
for i in nums:
    if a > 0 and res and res[-1] > i:
        res.pop()
        a-=1

    res.append(i)

if a > 0:
    res = res[:-a]

result = ''.join(res).lstrip('0')

if not result:
    result = "0"
print(result)
