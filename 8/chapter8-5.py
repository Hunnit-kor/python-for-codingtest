import sys
#n,m입력받기
n,m=map(int,sys.stdin.readline().split())

#화폐 종류 리스트 만들고 입력받기
d=[]
for i in range(n):
  d.append(int(sys.stdin.readline()))

#개수 셀 리스트 만들고 설정값은 10001
count=[10001]*(10001)

#화폐 1개의 값은 1로 표현하기
for i in range(n):
  count[d[i]]=1

#화폐값을 뺀것에 1을 더해서 다이나믹 프로그래밍 구현
for i in range(min(d)+1,m+1):
  for j in d:
    if count[i-j] !=10001:
      count[i]=min(count[i],count[i-j]+1)

#기본값이면 -1 아니면 화폐로 구성된 최솟값 출력
if count[m]==10001:
  print(-1)
else:
  print(count[m])