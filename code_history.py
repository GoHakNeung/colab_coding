import re
import pandas as pd
from io import StringIO

history = re.compile('_i[0-9]')
function = [] #_i1, _i2 코드가 저장된 변수 저장하는 리스트
code = [] # _i1, _i2에 있는 코드를 저장하는 리스트 
for i in list(dir()) : 
  if history.match(i) : # 많은 변수 중 _i1, _i2 같은 형태만 불러오기
    function.append(i[2:]) # _i1, _i2처럼 된 코드가 저장된 변수에서 1,2,3,4 처럼 숫자로 바꾸기
    f = StringIO()
    print(eval(i), file = f, end = '')
    code.append(f.getvalue())
    f.close()

# 데이터 프레임에 코드를 실행한 순서를 list 열에 저장하고 코드 code 열에 저장한다.  
code_history = pd.DataFrame({'list' : function, 
                            'code' : code})
code_history['list'] = code_history['list'].astype(int)
code_history = code_history.sort_values(by = 'list') # list를 정렬

code_history.to_csv('code_history.csv', encoding = 'utf-8-sig', index=False)
