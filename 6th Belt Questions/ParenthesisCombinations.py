n = int(input())
result = []
stack = [("", 0, 0)]

while stack:
    current, openn, closee = stack.pop()
    
    if len(current) == n * 2:
        result.append(current)
    else:
        if openn < n:
            stack.append((current + "(", openn + 1, closee))
        if closee < openn:
            stack.append((current + ")", openn, closee + 1))

for i in range(len(result)):
    for j in range(0, len(result) - i - 1):
        if result[j] > result[j + 1]:
            result[j], result[j + 1] = result[j + 1], result[j]

print(" ".join(result))


