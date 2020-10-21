#배열을 90도로 돌리는 함수
def turn_90(key):
  n=len(key)
  result=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      result[j][n-i-1]=key[i][j]
  return result

#맞는지 체크
def check(big):
  n=len(big)//3
  for i in range(n,2*n):
    for j in range(n,2*n):
      if big[i][j]!=1:
        return False
  return True
    
def solution (key,lock):
  
  n=len(lock)
  m=len(key)
  #좌물쇠를 3배로 옮기기
  big=[[0]*3*n for _ in range(3*n)]
  #기본좌물쇠를 가운데로 옮기기
  for i in range(n,2*n):
    for j in range(n,2*n):
      big[i][j]=lock[i-n][j-n]
  
  for i in range(4):
    key=turn_90(key)

    #열쇠 평행이동하기  
    for x in range(1,2*n):
      for y in range(1,2*n):
        for i in range(m):
          for j in range(m):
            #x,y는 평행이동 크기 i랑j 더하는이유는 그평행기준으로부터 열쇠 넣기
            big[x+i][y+j]+=key[i][j]
        if check(big) == False:
          for i in range(m):
            for j in range(m):
              big[x+i][y+j]-=key[i][j]
        else: return True
  return False  

