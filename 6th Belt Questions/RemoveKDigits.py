def removeKdigits(num, k):
    stack = []
    for c in num:
        while stack and k>0 and stack[-1] > c:
            stack.pop()
            k -= 1
        stack.append(c)
    while stack and k>0:
        stack.pop()
        k -= 1
    if not stack:
        return "0"
    return str(int("".join(stack)))
num = input()
k = int(input())
ans = removeKdigits(num,k)
print(ans)