#우선순위 큐 사용
import heapq
def solution(food_times,k):
  #food_times배열의 합이 k보다 작으면 k초후에 먹을게 없으므로 -1을 리턴
  if sum(food_times)<= k:
    return -1
  q=[]
  for i in range(len(food_times)):
    heapq.heappush(q,(food_times[i],i+1))
  #먹을 음식개수
  dish=len(food_times)
  #이전 음식의 시간 담을 변수
  prev=0
  #이때까지 먹은 음식 시간 담을 변수
  sum1=0
  #우선순위가 높은것부터 한접시씩 없애기
  while sum1+(q[0][0]-prev)*dish<=k:
    
    now=heapq.heappop(q)[0]
    #prev를 이때 빼주는 이유는 now를 prev에 넣어주는데 위 반복문 실행시 중첩 안되기위해서다
    sum1+=(now-prev)*dish
    prev=now
    dish-=1
  
  leftovers=sorted(q,key=lambda x : x[1])
  answer=leftovers[(k-sum1)%len(leftovers)][1]

  return answer