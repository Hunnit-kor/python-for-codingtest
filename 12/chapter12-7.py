from itertools import combinations
import sys
input=sys.stdin.readline
#n,m입력받기
n,m=map(int,input().split())
#도시의 정보를 입력받을 리스트 초기화 
city=[]
#도시의 정보 입력받기 
for i in range(n):
  city.append(list(map(int, input().split())))
#치킨집 정보를 얻을 리스트 초기화
chicken=[]
#집 정보를 얻을 리스트 초기화
home=[]
for i in range(n):
  for j in range(n):
    #도시일경우
    if city[i][j]==2:
      chicken.append([i,j])
    #집일경우
    elif city[i][j]==1:
      home.append([i,j])

#조합으로 치킨집 m개 정하기
comb=combinations(chicken,m)

minv=99999999999

#치킨조합중 하나를 택해서 거기서 최소거리구하기
for dist in comb:
  #합산 0
  sumv=0
  #각 집마다 각 조합에서 최소거리를 구해서 더하기
  for house in home:
    sumv+=min([abs(house[0]-i[0])+abs(house[1]-i[1]) for i in dist])
    #합이 최소보다 크면 다음으로
    if sumv>minv:
      break
  #합이 최소보다 작으면 그합을 최솟값으로 초기화하기 
  if sumv<minv:
    minv=sumv

print(minv)
        


  
