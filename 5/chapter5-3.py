import sys

#n,m입력받기
n,m=map(int,sys.stdin.readline().split())

d=[]
for i in range(n):
  d.append(list(map(int,sys.stdin.readline().split())))

def dfs(x,y):
  if x>=0 and x<n and y>=0 and y<m:
    
    if d[x][y]==0:
      d[x][y]=1
      dfs(x+1,y)
      dfs(x-1,y)
      dfs(x,y+1)
      dfs(x,y-1)
      return 1
    else:
      return 0 
  else:
    return 0

count=0
for i in range(n):
  for j in range(m):
    if dfs(i,j) ==1:
      count+=1
print(count)