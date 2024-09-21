a = int(input())
arr = list(map(int, input().split()))
dp={0}
for i in arr:
    dp = {i-j for j in dp}| {i+j for j in dp}
print("true" if 0 in dp else "false")