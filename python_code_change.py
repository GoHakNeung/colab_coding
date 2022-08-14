import sys  #맨 처음 한번 시작 온라인 저지 파일 불러올 때 시작

# 파이썬 코드로 실행해야 함. 라이브러리 내에서 시작하는 걸로
f = open('test.py', 'w')  
original = sys.stdout
sys.stdout = f

# 학생이 작성한 코드이다. 
# 작성한 코드를 적당히 손 봐서 print()해서 .py로 들어갈 코드가 적혀있다.
#1. 학생이 작성한 코드는 .py파일로 저장이 된다.
#2. .py 파일을 불러와서 input, print를 구분해서 코드를  리스트로 저정한다. 
#3. input에 정답 예제를 넣어서 확인한다.

order = 0  
for order in range(len(code)) : 
  if order in code_input : 
    print(code[order][:code[order].find('=')+1], 10)
  elif order in code_output : # 결과를 따로 변수에 저장해야 할 수도 있겠다. 그래야 결과를 비교할 수 있으닌까
    print(code[order])        # 수정 요망
  else : 
    print(code[order])

# 파이썬 코드로 실행해야 함. 원상복구
sys.stdout = original   
f.close()                     
 
