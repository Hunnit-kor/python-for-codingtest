import sys

#문자입력받기
d=sys.stdin.readline().rstrip()
d[0]=int(ord(d[0]))-int(ord('a'))+1
d[1]=int(d[1])
x,y=d[0],d[1]
dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]
result=0

for i in range(8):
  nx=x+dx[i]
  ny=y+dy[i]
  if nx>=1 and nx<=8 and ny>=1 and ny<=8:
    result+=1

