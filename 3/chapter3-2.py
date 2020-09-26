import sys

#n,m,k 입력받기
n,m,k=map(int,sys.stdin.readline().split())
d=list(map(int,sys.stdin.readline().split()))

#리스트 정렬
d.sort(reverse=True)
#가장 큰 값을 최대로 나올수있는거 만큼더하고 두번째로 큰수 더해서 덩어리 만들기
chunk=d[0]*k+d[1]

#m을 덩어리 단위인k+1로 나누어서 나온 몫만큼 덩어리랑 곱하기
result=m//(k+1)*chunk

#나머지만큼 가장 큰 수 곱하기
result+=m%(k+1)*d[0]

print(result)
