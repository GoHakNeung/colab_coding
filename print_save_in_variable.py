import sys 

f = open('파일이름.txt', 'w')  # 프린트할 내용을 저장하는 파일  
original = sys.stdout  # 복구하기 위해 잠시 저장
sys.stdout = f  # f 라는 곳에 프린트 한 내용이 저장된다. 
for i in range(10) : 
  print(i)
sys.stdout = original   # 원래의 stdout으로 복구

f.close()                     # 로그 파일 닫기
