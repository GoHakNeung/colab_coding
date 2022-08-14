# 코드 불러오기?
code = []
code_input = []
code_output = []

# sum.py로 저장된 코드를 불러온다.
# 사전에 sum.py를 저장해야 한다.(%%writefile sum.py 명령어 실행)
f = open('/content/sum.py', 'r')
lines = f.readlines()
for line in lines : 
  line = line.strip()
  if line != '' : 
    code.append(line)    
    if line.find('input') >= 0 : 
      code_input.append(code.index(line))
    if line.find('print') >= 0 : 
     code_output.append(code.index(line))

f.close()

print(code) # 전체 코드 리스트로
print(code_input) # input 코드가 있는 인덱스
print(code_output) # print 코드가 있는 인덱스
