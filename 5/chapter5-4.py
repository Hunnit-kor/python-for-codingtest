from collections import deque
import sys

#n,m입력받기
n,m=map(int,sys.stdin.readline().split())
queue=deque()

#미로 맵 만들기
world=[]
for i in range(n):
  world.append(list(map(int,sys.stdin.readline().split())))
#bfs함수 만들기
def bfs(a,b):
  dx=[1,-1,0,0]
  dy=[0,0,1,-1]
  queue.append((a,b))
  while queue:
    x,y=queue.popleft()
    for i in range(3):
      nx=x+dx[i]
      ny=y+dy[i]
      if nx>=0 and nx<n and ny>=0 and ny< m:
            if world[nx][ny]==1:
              world[nx][ny]=world[x][y]+1
              queue.append((nx,ny))
      else: 
        continue

bfs(0,0)
print(world[n-1][m-1])      

      
  
  