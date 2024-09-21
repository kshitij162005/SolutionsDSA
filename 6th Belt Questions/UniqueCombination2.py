a = int(input())
candidates = list(map(int, input().split()))
target = int(input())
ans = []

def helper(candidates, target, i, temp):
    if target == 0:
        ans.append(temp[:])
        return
    for j in range(i, len(candidates)):
        if candidates[j] > target:
            break
        if j > i and candidates[j] == candidates[j - 1]:
            continue
        temp.append(candidates[j])
        helper(candidates, target - candidates[j], j + 1, temp)
        temp.pop()

candidates.sort()
helper(candidates, target, 0, [])
if not ans:
    print(-1)
else:
    for combination in ans:
        print(" ".join(map(str, combination)))
