import sys
input=sys.stdin.readline

#n입력받기
n=int(input())

#사람수 리스트
count=0
#그룹수 변수
group=0

#공포도 입력받기
degree=list(map(int,input().split()))
degree.sort()


for i in degree:
  count+=1#현재인원 카운트하기
  if count>=i:#현재인원이 공포도보다 같거나 클때
    group+=1#그룹수 추가
    count=0#카운트 0으로 초기화

print(group)
