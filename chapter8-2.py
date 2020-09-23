import sys
x=int(sys.stdin.readline())
a=[0]*(x+1)
a[2]=1

for i in range(3,x+1):
  a[i]=a[i-1]+1
  if i%5==0:
    a[i]=min(a[i],a[i//5])
  if i%3==0:
    a[i]=min(a[i],a[i//3])
  if i%2==0:
    a[i]=min(a[i],a[i//2])
print(a[x])