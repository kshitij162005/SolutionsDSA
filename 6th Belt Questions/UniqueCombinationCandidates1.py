n = int(input())
candidates = list(map(int, input().split()))
target = int(input())
ans = []

# 7th Test case fail hone ka kaaran
candidates = sorted(candidates)

def check(cand, target, i, currSum, temp):
    if currSum > target or i >= len(cand):
        return
    if(currSum == target):
        ans.append(temp[:])

    for j in range(i, len(cand)):
        temp.append(candidates[j])
        check(cand, target , j, currSum + cand[j], temp)
        temp.pop()

check(candidates, target, 0, 0, [])
sorted_combinations = sorted(ans)
if(ans):
    for combination in sorted_combinations:
        print(*combination)
else:
    print(-1)