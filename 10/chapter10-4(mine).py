import copy
from collections import deque
import sys
input=sys.stdin.readline

#강의 개수 n개 입력받기
n=int(input())

#각 강의의 시간을 입력받는 리스트
time=[0]*(n+1)

#선수강의를 관리하기위한 진입차수 리스트
indegree=[0]*(n+1)
#강의의 정보를 입력받는 그래프
graph=[[]for i in range(n+1)]
#각 강의 개수의 선수과목들 입력받기
for i in range(1,n+1):
  data=list(map(int,input().split()))
  time[i]=data[0]
  for x in data[1:-1]:
    graph[x].append(i)
    indegree[i]+=1

#위상정렬함수
def topology_sort():
  #타임 리스트 복사
  result=copy.deepcopy(time)
  q=deque()
  for i in range(1,n+1):
    if indegree[i]==0:
      q.append(i)
  #q가 진행되는 동안
  while q:
    now=q.popleft()
    for i in graph[now]:
      indegree[i]-=1
      #나는 진입차수가 0이될 때 시간을 더해주어야 된다고 생각했다
      if indegree[i]==0:
        result[i]=max(result[i],time[i]+result[now])
        q.append(i)
  for i in range(1,n+1):
    print(result[i])
    
topology_sort()