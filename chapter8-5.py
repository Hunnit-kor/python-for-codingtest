import sys
n,m=map(int,sys.stdin.readline().split())
d=[]
for i in range(n):
  d.append(int(sys.stdin.readline()))

count=[10001]*(10001)

for i in range(n):
  count[d[i]]=1

for i in range(min(d)+1,m+1):
  for j in d:
    if count[i-j] !=10001:
      count[i]=min(count[i],count[i-j]+1)

if count[m]==10001:
  print(-1)
else:
  print(count[m])

