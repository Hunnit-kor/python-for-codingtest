import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

#도시개수 n, 통로개수 m, 메시지를 보내고자하는 도시c 입력받기
n,m,c=map(int,input().split())
#도시정보 입력받을 수 있는 그래프 만들기
graph=[[] for _ in range(n+1)]
#거리 무한으로 초기화하기
distance=[INF]*(n+1)
#방문정보 리스트만들기
visit=[False]*(n+1)
#간선 정보 입력받기
for i in range(m):
  x,y,z=map(int,input().split())
  graph[x].append((y,z))

#다이크슈트라 만들기
def dijkstra(start):
  q=[]
  #전파 받는 도시개수 변수 전체초기화
  global count
  heapq.heappush(q,(0,start))
  distance[start]=0
  #시작 노드를 제외
  count=-1
  while q:
    #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
    dist,now=heapq.heappop(q)
    if visit[now]==False:
      visit[now]=True
      count+=1
    if dist>distance[now]:
      continue
    #현재노드와 인접한 다른 노드 확인하기
    for i in graph[now]:
      cost=dist+i[1]
      #현재노드를 거쳐서 다른 노드로 이동할때가 더 짧은경우
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))
dijkstra(c)
# 최대거리를 뽑기 위한 작업
for i in range(n+1):
  if distance[i]==INF:
    distance[i]=0

print(count,end=" ")
print(max(distance))
