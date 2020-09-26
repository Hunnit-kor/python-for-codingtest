import sys

#가로 길이 n입력받기
n=int(sys.stdin.readline())

#리스트 만들기
a=[0]*(n+1)

a[1]=1
a[2]=3
# 길이n까지 각 수마다의 가지수 다이나믹프로그래밍으로 구하기
for i in range(3,n+1):
  a[i]=a[i-1]+(a[i-2]*2)

#n일때의값 796796으로 나눈 나머지 구하기
print(a[n]%796796)