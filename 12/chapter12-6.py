#벽면이 성립되는지 확인하기
def check(result):
  #모두 되는지 일일이 확인하기
  for i in result:
    x,y,a=i
    #기둥일 때
    if a==0:
      #바닥이거나 보의 한쪽 끝부분 위에 있거나 기둥위에 있어야 설치가능
      if y==0 or [x-1,y,1] in result or [x,y,1] in result or [x,y-1,0] in result:
         continue 
      return False
    
    #보일 경우 
    else:
      #한쪽 끝부분이 기둥 위에 있거나, 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 설치가능
      if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
        continue
      return False
  return True

def solution(n,build_frame):
  result=[]
  #빌드 프레임 반복
  for frame in build_frame:
    x,y,a,b= frame
    #설치일 경우
    if b==1:
      result.append([x,y,a]) 
      if not check(result):
        result.remove([x,y,a])
    #삭제일 경우
    else:
      if [x,y,a] in result:

        result.remove([x,y,a])
        if not check(result):
          result.append([x,y,a])
  return sorted(result)