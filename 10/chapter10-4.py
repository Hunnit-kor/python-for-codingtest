from collections import deque
import copy
import sys
input=sys.stdin.readline

#노드의 개수 입력받기
v=int(input())
#모든 노드에 대한 진입차수는 0으로 초기화
indegree=[0]*(v+1)
#각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph=[[]for i in range(v+1)]
#각 강의 시간을 0으로 초기화
time=[0]*(v+1)
#방향 그래프의 모든 간선 정보를 입력받기
for i in range(1,v+1):
  data=list(map(int,input().split()))
  time[i]=data[0]
  for j in data[1:-1]:
    graph[j].append(i)
    indegree[i]+=1

#위상 정렬 함수
def topology_sort():
  result=copy.deepcopy(time)# 알고리즘 수행 결과를 담을 리스트
  q=deque()
  for i in range(1,v+1):
    if indegree[i]==0:
      q.append(i)
  
  #큐가 빌 때 까지 반복
  while q:
    now=q.popleft()
    #해당 원소와 연결된 노드들의 진입차수 1빼기
    for i in graph[now]:
      result[i]=max(result[i],result[now]+time[i])
      indegree[i]-=1
      #새롭게 진입차수가 0이되는 노드를 큐에 넣기
      if indegree[i]==0:
        q.append(i)
  #위상 정렬을 수행한 결과 출력
  for i in range(1,v+1):
    print(result[i])
topology_sort()