a = int(input())  
b = list(map(int, input().split()))
c = int(input())  

for i in range(a):
    summ = 0  
    for j in range(i, a):
        summ += b[j]  
        if summ == c:
            print(i, j)  
            break
    else:
        continue  
    break
else:
    print("No Subarray Found") 



