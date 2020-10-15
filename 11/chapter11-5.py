#n입력받기
n,m=map(int,input().split())
#볼링공 무게 입력받을 리스트 만들기
weight=list(map(int,input().split()))

#경우의 수 변수 초기화
count=0


for i in range(n-1):
  for j in range(i+1,n):
    #두 볼링공의 무게가 같은지 확인
   if  weight[i]!=weight[j]:
     #다를 경우 경우의 수 증가
      count+=1

#경우의 수를 출력한다
print(count)
