import sys

#n,k입력받기
n,k=map(int,sys.stdin.readline().split())

count=0

#n이 1일될때까지의 최소 경우의 구하기
while n>1:
  if n>=k:
    target=n//k*k
    count+=n-target
    if n%k==0:
      count+=1
      n//=k
    else:
      n=target
  else:
    count+=n-1
  
print(count)