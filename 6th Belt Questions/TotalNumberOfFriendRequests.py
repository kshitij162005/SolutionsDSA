def numFriendRequests(ages):
    count = [0] * 121

    for age in ages:
        count[age] += 1

    ans = 0
    for ageA in range(15, 121):
        if count[ageA] == 0:
            continue  

        for ageB in range(ageA // 2 + 8, ageA + 1):
            if count[ageB] == 0:
                continue  

            ans += count[ageA] * count[ageB]

            if ageA == ageB:
                ans -= count[ageA]  

    return ans


if __name__ == "__main__":
    n = int(input())
    ages = list(map(int, input().split()))
    result = numFriendRequests(ages)
    print(result)
