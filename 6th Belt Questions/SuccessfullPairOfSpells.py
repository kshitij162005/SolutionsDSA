from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        result = []

        for spell in spells:
            required_potion = (success + spell - 1) // spell  
           
            index = bisect_left(potions, required_potion)
            result.append(len(potions) - index)

        return result

if __name__ == "__main__":
    m, n = map(int, input().split())
    
    spells = list(map(int, input().split()))
    potions = list(map(int, input().split()))
    success = int(input())
    
    sol = Solution()
    result = sol.successfulPairs(spells, potions, success)
    
    print(" ".join(map(str, result)))
