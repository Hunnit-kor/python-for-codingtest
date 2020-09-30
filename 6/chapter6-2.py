import sys
#n입력받기
n=int(sys.stdin.readline())
d=[]
#리스트의 배열 입력받기
for i in range(n):
  d.append(int(sys.stdin.readline()))
#내림차순으로 정리
d.sort(reverse=True)
print(d)