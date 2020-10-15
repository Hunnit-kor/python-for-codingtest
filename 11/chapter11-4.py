#n입력받기
n=int(input())
#동전 종류 입력받기
coin=list(map(int,input().split()))
coin.sort()

target=1

for i in coin:
  #만들수 없는 금액을 찾았을때 반복종료
  if target<i:
    break
  target+=i
#만들 수 없는 금액 출력
print(target)
