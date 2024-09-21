def getPermutation(n, k):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    nums = [str(i) for i in range(1, n + 1)]
    k -= 1
    result = ""

    while n > 0:
        n -= 1
        index, k = divmod(k, factorial(n))
        result += nums.pop(index)

    return result

n, k = map(int, input().split())
print(getPermutation(n, k))
