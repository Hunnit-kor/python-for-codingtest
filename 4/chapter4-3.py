import  sys

#n,m,a,b,d 입력받기
n,m=map(int,sys.stdin.readline().split())
a,b,d=map(int,sys.stdin.readline().split())

#world입력받기
world=[]
for i in range(n):
  world.append(list(map(int,sys.stdin.readline().split())))
world[a][b]=1

#왼쪽으로 도는 함수만들기
def turn():  
   global d
   d-=1
   if d==-1:
      d=3

count=0
visit=1   

while 1:
  #단위벡터
  dx=[-1,0,1,0]
  dy=[0,1,0,-1]
  #왼쪽으로 돌기
  turn()
  
  #돌고난 방향으로 갔을 경우
  x=a+dx[d]
  y=b+dy[d]
  #육지가 아닌경우 다시 회전하기
  if world[x][y]!=0:
    count+=1
    if count==4:
      x=a-dx[d]
      y=b-dy[d]
      if world[x][y]!=0:
        break
      else:
        count=0
        a,b=x,y

    continue
  #육지인 경우 글로 가기 
  else:
    count=0
    world[x][y]=2
    visit+=1
    a,b=x,y
  

print(visit)