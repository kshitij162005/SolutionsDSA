a = int(input())
arr1 = list(map(int, input().split()))
b = int(input())
arr2 = list(map(int, input().split()))

index = 0

for i in range(b):
    if index < a and arr1[index] <= arr2[i]:
        index+=1
print(index)