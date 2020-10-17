#문자열 입력받기
word=input()
alphabet=[]
number=[]

for i in word:
  if i.isdigit():
    number.append(i)
  else:
    alphabet.append(i)

number.sort()
alphabet.sort()
for i in alphabet:
  print(i,end="")
for j in number:
  print(j,end="")
