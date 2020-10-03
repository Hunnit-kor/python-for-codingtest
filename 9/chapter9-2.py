import sys
input=sys.stdin.readline
INF=int(1e9)

#전체 회사 수 n, 경로수 m 입력받기
n,m=map(int,input().split())

#회사들에 대한 그래프 만들기
graph=[[INF]*(n+1) for _ in range(n+1)]

#자기자신인 경우는 0
for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      graph[i][j]=0


#회사간 연결 도로 입력받기
for i in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1

# 소개팅하는 k회사와 마지막 종착회사인 x 입력받기
x,k=map(int,input().split())

#플루이드워셜
for c in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
       graph[a][b]=min(graph[a][b],graph[a][c]+graph[c][b])


if graph[1][k]==INF or graph[k][x]==INF:
  print(-1)
else:
  print(graph[1][k]+graph[k][x])
