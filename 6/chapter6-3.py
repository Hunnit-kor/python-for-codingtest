import sys
#n입력받기
n=int(sys.stdin.readline())
a=[]
#리스트 입력받기
for i in range(n):
  d=sys.stdin.readline().split()
  a.append((d[0],int(d[1])))
#성적 낮은순으로 정렬하기
a.sort(key=lambda x :x[1])
for i in range(n):
  print(a[i][0],end=" ")
