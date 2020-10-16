#숫자 입력받기
number=input()
#리스트 정수화 시키기
number=list(map(int,number))
#가운데 값 구하기
mid=len(number)//2
#절반씩 넣을 리스트 초기화
a=[]
b=[]
#중간자리 전까지 리스트추가
for i in number[:mid]:
  a.append(i)
#중간자리 후부터 리스트 추가
for j in number[mid:len(number)]:
  b.append(j)
#합이 같으면 럭키 출력
if sum(a)==sum(b):
  print("LUCKY")
#아니면 레디 출력
else:
  print("READY")