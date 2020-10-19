def solution(s):
  #문자열 s의 길이
  length=len(s)
  #기본적으로 정답은 문자열 s의 길이
  answer=len(s)
  #그 문자열의 길이 반만큼의 덩어리까지 반복
  for step in range(1,length//2+1):
    #가장 기본적으로 주어지는 prev
    prev=s[0:step]
    #압축된 문자열을 담을 변수 초기화
    compress=""
    #몇번 반복될지 갯수 셀 변수 1로 초기화
    count=1
    #step만큼 뛰어넘기
    for j in range(step,len(s),step):
      #이전 단계랑 똑같으면 1더해주기
      if s[j:j+step]==prev:
        count+=1
      #아닐경우 이전의 저장해둔 덩어리랑 카운트 compress에 넣기
      else:
        compress+=str(count)+prev if count>=2 else prev
        prev=s[j:j+step]
        count=1
   #남은거 더해주기
    compress+=str(count)+prev if count>=2 else prev
    #가장 길이가 짧으거 구하기
    answer=(answer,len(compress))
  return answer