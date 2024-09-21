import sys

def countArrangement(n):
    # Initialize dp table with -1
    dp = [[-1] * (1 << (n + 1)) for _ in range(n + 1)]
    
    # Define the recursive function
    def rec(place, state):
        if place == n + 1:
            return 1
        if dp[place][state] != -1:
            return dp[place][state]
        ans = 0
        for i in range(1, n + 1):
            if (state & (1 << i)) == 0 and (i % place == 0 or place % i == 0):
                ans += rec(place + 1, state | (1 << i))
        dp[place][state] = ans
        return ans
    
    return rec(1, 0)

# Input handling
if __name__ == "__main__":
    input_n = int(input())
    result = countArrangement(input_n)
    print(result)