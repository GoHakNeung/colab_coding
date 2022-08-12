import re
from io import StringIO

history = re.compile('_i[0-9]')
# _i1, _i2, _i3 등 주피터 노트북에서 사용한 코드가 저장된 변수 불러오기
function = [] 
code = []
for i in list(dir()) : 
  if history.match(i) : 
    function.append(i[2:])
    f = StringIO()
    print(eval(i), file = f, end = '')
    code.append(f.getvalue())
    f.close()

code_history['list'] = code_history['list'].astype(int)
code_history = code_history.sort_values(by = 'list')

code_history.to_csv('code_history.csv', encoding = 'utf-8-sig', index=False)
