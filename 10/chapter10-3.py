
import sys
input=sys.stdin.readline

#집의 개수 n, 길의 개수m개 입력받기
n,m=map(int,input().split())
#길의 정보를 담을 리스트
edges=[]
#길의 정보 입력받기
for i in range(m):
  a,b,c=map(int,input().split())
  #유지비 부터 정렬하기위해 튜플의 맨앞에 둠
  edges.append((c,a,b))

#부모 테이블 초기화
parent=[0]*(n+1)
for i in range(1,n+1):
  parent[i]=i

#같은 집합 찾는 함수 만들기
def find_parent(x):
  if parent[x]!=x:
    parent[x]=find_parent(parent[x])
  return parent[x]

#두 집합을 한집합으로 만들기
def union_parent(a,b):
  a=find_parent(a)
  b=find_parent(b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

edges.sort()
#삭제시킬 길 변수 초기화
delete=0
#유지비 초기화
result=0
#유지비 구하기
for i in edges:
  cost,a,b=i
  if find_parent(a)!=find_parent(b):
    union_parent(a,b)
    delete=cost
    result+=cost
#가장 유지비 많이드는길을 없앤다
result-=delete    

print(result)


