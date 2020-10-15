number=input()
number=list(map(int,number))
#0으로 셀변수 와 1로 셀 변수
count0=0
count1=0

#1로만들기
if number[0]==0:
    count1+=1
#0으로 만들기
if number[0]==1:
    count0+=1

for i in range(1,len(number)):
  #0으로 만들기 
  if number[i]!= 0:
    #1인데 그전단계가 0이면 1더해주기
    if number[i-1]==0:
       count0+=1
  #1로만들기
  if number[i]!= 1:
    #0인데 그전다계가 1이면 1더해주기
    if number[i-1]==1:
      count1+=1
#0으로 뒤집는 것과 1로 뒤집는 것중 더 작은거 출력하기
print(min(count0,count1))