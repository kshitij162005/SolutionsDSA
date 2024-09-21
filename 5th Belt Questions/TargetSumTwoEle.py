size=int(input())
arr=list(map(int,input().split()))
k=int(input())
ans=[]
for i in range(size):
  for j in range(i+1):
    if arr[j]+arr[i]==k:
      ans.append([j,i])
if len(ans)>0:
  for i in ans:
    print(*i)
else:
  print("-1")