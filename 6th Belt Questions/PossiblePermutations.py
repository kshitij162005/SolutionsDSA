def permute(nums):
    result = []
    
    def backtrack(path, options):
        if not options:
            result.append(path)
            return
        for i in range(len(options)):
            backtrack(path + [options[i]], options[:i] + options[i+1:])
    backtrack([], nums)
    result.sort()
    return result


a = int(input())
nums = list(map(int, input().split()))
permutations = permute(nums)

for i in permutations:
    print(*i)
