# a = int(input())
# arr1 = list(map(int, input().split()))
# b = int(input())
# arr2 = list(map(int, input().split()))

# index = 0

# for i in range(b):
#     if index < a and arr1[index] <= arr2[i]:
#         index+=1
# print(index)


a = int(input())
arr1 = list(map(int, input().split()))
b = int(input())
arr2 = list(map(int, input().split()))

index = 0

for i in range(a):
    for j in range(0,a-i-1):
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
for i in range(b):
    for j in range(0,b-i-1):
        if arr2[j+1] > arr2[j]:
            arr2[j+1], arr2[j] = arr2[j], arr2[j+1]


for i in range(b):
    if index < a and arr1[index] <= arr2[i]:
        index += 1


print(index)