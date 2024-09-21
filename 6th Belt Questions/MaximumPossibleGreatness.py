if __name__ == "__main__":
    a = int(input())
    arr = list(map(int, input().split()))

    for i in range(a):
        for j in range(0,a - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    p1 = 0
    p2 = 1
    count = 0
    
    while p2 < len(arr):
        if arr[p2] > arr[p1]:
            count += 1
            p1 += 1
            p2 += 1
        else:
            p2 += 1
            
    print(count)
