def bag_of_tokens_score(tokens, power):
    tokens.sort()
    score = 0
    max_score = 0
    left = 0
    right = len(tokens) - 1

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            score += 1
            left += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            score -= 1
            right -= 1
        else:
            break

    return max_score

if __name__ == "__main__":
    n = int(input())
    tokens = list(map(int, input().split()))
    power = int(input())

    result = bag_of_tokens_score(tokens, power)
    print(result)
