import sys
#n,m입력받기
n,m=map(int,sys.stdin.readline().split())

#리스트입력받기
d=[]
for i in range(n):
  d.append(list(map(int,sys.stdin.readline().split())))

#각행마다 제일 작은수 입력받고 그중 제일큰거 고르기
small=-2
for i in range(n):
  if small>=min(d[i]):
    continue
  else:
    small=min(d[i])

print(small)