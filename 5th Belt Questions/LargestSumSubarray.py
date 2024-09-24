n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print(0)
else:
    current = maxi = arr[0]
    
    for num in arr[1:]:
        # Custom max logic
        if current + num > num:
            current = current + num
        else:
            current = num
        
        # Custom max logic for maxi
        if current > maxi:
            maxi = current
    
    print("Results")
    print(maxi)  