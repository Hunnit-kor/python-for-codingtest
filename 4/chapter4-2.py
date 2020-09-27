import sys

#문자입력받기
d=sys.stdin.readline().rstrip()
#입력받은걸 행과 열이란 변수에 나누기
row=int(ord(d[0]))-int(ord('a'))+1
column=int(d[1])
x,y=row,column

#이동벡터 만들기
dx=[1,1,-1,-1,2,2,-2,-2]
dy=[2,-2,2,-2,1,-1,1,-1]
result=0
#이동할수 있는 경우의수 구하기
for i in range(8):
  nx=x+dx[i]
  ny=y+dy[i]
  if nx>=1 and nx<=8 and ny>=1 and ny<=8:
    result+=1

print(result)