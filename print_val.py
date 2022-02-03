"""
파이썬의 print 함수에는 return 값이 없다. 그냥 바로 출력할 뿐이다. 
만약 print의 사용법을 그대로 차용하면서 print의 결과값을 변수로 저장하고 싶다면, 
사용자가 StringIO 클래스 기반 객체를 만들어 getvalue() 하면 된다. 그렇게 어렵지 않다. 아래가 그 예시이다.
"""

from io import StringIO

def return_print(*message):
    io = StringIO()
    print(*message, file=io, end="")
    return io.getvalue()

wow = return_print("하하", "호호", "히히")
print(wow)

# StringIO 객체를 이용해 print에 출력할 내용을 입력할 수 있다.
f = io.StringIO('asdfasdf')
print(f.read())

# print(file = f) f를 StringIO 객체에 저장하면 화면에 출력되지 않고 f에 저장된다. 
f = io.StringIO()
print('hello', file = f, end = '')
f.getvalue()

f.close() # open 했으니 닫아줘야지 