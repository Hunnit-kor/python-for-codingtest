import sys
#n,m입력받기
n,m=map(int,sys.stdin.readline().split())
#떡 길이 전체 입력받기
dduck=list(map(int,sys.stdin.readline().split()))

#이진함수로 최대길이 구하는 함수
def binarysearch(start,end,dduck):
  while start<=end:
    mid=(start+end)//2
    total=0
    for i in dduck:
      if mid<i:
        total+=i-mid
    #총량이 m보다 작은경우 end=mid-1
    if total<m:
      end=mid-1
    #나머지 경우에 start=mid+1
    else:
      
      result=mid
      start=mid+1
  return result

print(binarysearch(1,max(dduck),dduck))