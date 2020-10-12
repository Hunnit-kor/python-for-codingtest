#문자열 s 입력받기
s=input()
#최대합산할 숫자 변수
number=0

for i in s:
  #정수화하기
  x=int(i)
  #0과1일 경우 더하기
  if x == 0 or x == 1:
    number+=x
  #나머지일 경우
  else:
    #number가 0이거나 5일경우 더한다
    if number==0 or x==1:
      number+=x
    #나머지일 경우 곱한다
    else:  
     number*=x

print(number)