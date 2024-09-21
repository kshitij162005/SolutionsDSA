def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    i = 0
    T = 0
    F = 0
    ans = 0
    n = len(answerKey)

    # Sliding window approach
    for j in range(n):
        if answerKey[j] == 'T':
            T += 1
        else:
            F += 1

        # If the minimum of T and F exceeds k, shrink the window
        while min(T, F) > k:
            if answerKey[i] == 'T':
                T -= 1
            else:
                F -= 1
            i += 1

        # Calculate the maximum length of the valid substring
        ans = max(ans, j - i + 1)

    return ans


# Input handling
if __name__ == "__main__":
    answerKey = input().strip()
    k = int(input().strip())

    result = maxConsecutiveAnswers(answerKey, k)
    print(result)