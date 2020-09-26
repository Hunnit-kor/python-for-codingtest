import sys
#구하고자 하는 숫자 입력
x=int(sys.stdin.readline())
#다이나믹 프로그래밍을 구현하기 위한 리스트 만들기
a=[0]*(x+1)
a[2]=1

#각 숫자마다 1이될수 있는 최솟값 구하기 
for i in range(3,x+1):
  a[i]=a[i-1]+1
  if i%5==0:
    a[i]=min(a[i],a[i//5]+1)
  if i%3==0:
    a[i]=min(a[i],a[i//3]+1)
  if i%2==0:
    a[i]=min(a[i],a[i//2]+1)

print(a[x])