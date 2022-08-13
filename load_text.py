# 텍스트끼리 비교해서 out 비교하기!
answer = [] # 결과물을 저장하는 리스트이다. 
f = open('/content/파일명.txt', 'r') # 코랩기준, 읽어올 파일명을 입력한다. 
lines = f.readlines() #\n을 포함하고 있다. 그래서 일단 다 리스트로 불러온 다음 문자열 처리를 해준다. 
for line in lines : 
  line = line.strip() # 빈칸, 줄바꿈 없애주기
  answer.append(line) # 다시 리스트로 만들기
f.close()

print(answer)
