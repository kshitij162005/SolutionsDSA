def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def dividePlayers(skill):
    bubble_sort(skill)
    
    res = 0
    d = skill[0] + skill[-1] 

    for i in range(len(skill) // 2):
        s = skill[i]
        e = skill[-1 - i]
        if d != s + e: 
            return -1
        res += (s * e)

    return res


if __name__ == "__main__":
    n = int(input())
    skill = list(map(int, input().split()))

    result = dividePlayers(skill)

    print(result)
