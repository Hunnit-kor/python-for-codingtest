import sys
input=sys.stdin.readline
#팀 개수 n, 연산회수 m입력받기
n,m=map(int,input().split())

#팀 테이블 초기화
team=[0]*(n+1)
for i in range(n+1):
  team[i]=i

#팀 찾는 함수 만들기
def find_team(x):
  if team[x]!=x:
    team[x]=find_team(team[x])
  return team[x]

#팀 합치는 함수 만들기
def union_team(a,b):
  a=find_team(a)
  b=find_team(b)
  if a<b:
    team[b]=a
  else:
    team[a]=b

#연산회수 만큼 입력받기
for i in range(m):
  k,a,b=map(int,input().split())
  #k가 1일때 팀찾기 같으면 예스 다르면 노 출력
  if k==1:
    if find_team(a)==find_team(b):
      print("YES")
    else:
      print("NO")
  else:
    union_team(a,b)

