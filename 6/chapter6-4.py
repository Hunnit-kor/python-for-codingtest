import sys
#n,k입력받기
n,k=map(int,sys.stdin.readline().split())

#a,b리스트의 배열 입력받기
a=list(map(int,sys.stdin.readline().split()))
b=list(map(int,sys.stdin.readline().split()))

#a는 오름차순 b는 내림차순으로 배열 정렬
a.sort()
b.sort(reverse=True)

#a와 b배열 k번 바꿀 수 있으면 바꾸기
for i in range(k):
  #a가 b원소 보다 클때는 반복문 x
  if a[i]>b[i]:
    break
  #나머지 경우에는 바꾸기
  else:
    a[i],b[i]=b[i],a[i]
print(sum(a))