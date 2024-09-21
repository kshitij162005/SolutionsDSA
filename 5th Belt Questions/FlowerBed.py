# a = int(input())
# b = int(input())
# c = list(map(int, input().split()))
# d = [0]+c+[0]
# for i in range(a):
#     if c[i-1] == 0 and c[i] == 0 and c[i+1] == 0:
#         c[i] = 1
#         b = b - 1
# if b <= 0:
#     print("True")
# else:
#     print("False")



a = int(input())
b = int(input())
c = list(map(int, input().split()))

d = [0] + c + [0]

for i in range(a):
    if(c[i-1] == 0 and c == 0 and c[i+1] == 0):
        c[i] = 1
        b -= 1

if b <= 0:
    print("True")
else:
    print("False")
    
