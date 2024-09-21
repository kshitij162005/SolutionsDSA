def num_moves_stones_ii(stones):
    stones.sort()
    n = len(stones)
    high = max(stones[n - 1] - n + 2 - stones[1], stones[n - 2] - stones[0] - n + 2)

    low = n
    i = 0
    for j in range(n):
        while stones[j] - stones[i] >= n:
            i += 1
        if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
            low = min(low, 2)
        else:
            low = min(low, n - (j - i + 1))

    return [low, high]

if __name__ == "__main__":
    n = int(input())
    stones = list(map(int, input().split()))

    result = num_moves_stones_ii(stones)

    print(result[0],result[1])
