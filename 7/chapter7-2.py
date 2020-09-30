import sys
#n입력받고 n만큼의 원소를 갖는 리스트a입력받기
n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

#m입력받고 m만큼의 원소를 갖는 리스트b입력받기
m=int(sys.stdin.readline())
b=list(map(int,sys.stdin.readline().split()))

#이진법 탐색함수 만들기
def binarysearch(start,end,target):
  while start<=end:
    mid=(start+end)//2
    #중간값이 타겟보다 작을경우 start=mid+1
    if a[mid]<target:
      start=mid+1
    #중간값이 타겟보다 클경우 end=mid-1
    elif a[mid]>target:
      end=mid-1
    else:
      return mid
  return None

for i in b:
  if binarysearch(0,len(a)-1,i)==None:
    print("No",end=" ")
  else:
    print("Yes",end=" ")
