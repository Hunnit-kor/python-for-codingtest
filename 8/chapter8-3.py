import sys

#식량 창고 개수 n과 창고 입력받기 
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

a[1]=max(a[0],a[1])
# 얻을 수 있는 최대 식량 다이나믹프로그래밍으로 구현하기
for i in range(2,n):
  a[i]=max(a[i-1],a[i-2]+a[i])

#최대 식량출력하기
print(a[n-1])