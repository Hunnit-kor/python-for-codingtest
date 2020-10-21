from collections import deque
#보드의 크기
n=int(input())
#사과의 개수 입력받기
k=int(input())
#보드 리스트 초기화
board=[[0]*(n) for _ in range(n)]
#사과 위치 입력받기
for i in range(k):
  a,b=map(int,input().split())
  board[a-1][b-1]=1
#뱀의 방향 전환횟수 입력받기
l=int(input())
#뱀의 방향전환 리스트 초기화하기
turns=deque()
for  i in range(l):
  data=list(input().split())
  turns.append((int(data[0]),data[1]))
#도는 함수 만들기
def turn(s):
  global d
  if s=='L':
    d-=1
    if d==-1:
      d=3
  elif s=='D':
    d+=1
    if d==4:
      d=0

#뱀의 몸 리스트 초기화하기
snake=[[0]*n for _ in range(n)]
snake[0][0]=1
a=[1,2,3,4]

#이동하는 기본단위
dx=[0,1,0,-1]
dy=[1,0,-1,0]
d=0
q=[(0,0)]
def snakes():
  global l
  #회전정보
  index=0
  #시간변수
  time=0  
  #뱀 머리 위치
  headx=0
  heady=0
  #뱀꼬리위치
  tailx=0
  taily=0
  while 1:
    
    #시간이 정해진 시간보다 작을동안
    
        time+=1
        #머리에서 더해주기
        x=headx+dx[d]
        y=heady+dy[d]
        #벽을 넘으면 끝내기
        if x<0 or x>=n or y <0 or y>=n:
            return time
        
        #자기몸이면 끝내기
        elif snake[x][y]==1:
          return time
        
      
        #사과를 만났을때 꼬리는 그대로 
        elif board[x][y]==1: 
            snake[x][y]=1
            board[x][y]=0
            headx=x
            heady=y
            
            
        #아무것도 없을때 꼬리는 한칸 앞으로     
        else:
          
          snake[x][y]=1
          headx=x
          heady=y
          #꼬리한칸씩 떼네기
          tailx,taily=q.pop(0)
          snake[tailx][taily]=0
        #갔던곳은 q에 넣어두기
        q.append((headx,heady))
        #도는 회수와 시간이 딱맞았을 경우에만 돌기
        if index<l and time==turns[index][0]:
          s=turns[index][1]
          index+=1
          turn(s)
  

print(snakes())
