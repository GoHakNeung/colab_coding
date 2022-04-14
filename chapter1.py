import initialize as init
init.start()

class problem_chcek : 
    def check() : 
        init.color_text('정답입니다.', 'green')

    def hint() : 
        init.color_text('힌트입니다.', 'blue')

    def solution() : 
        init.color_text('정답 예시입니다.', 'orange')

class question1(problem_chcek) : 
    _var = 'first'
    _expected = 3
    _hint = '1, 2 다음에는 무슨 숫자일까요?'
    _solution = 3


class question2(problem_chcek) : 
    _var = 'second'
    _expected = 'hi'
    _hint = 'hello를 다른말로 뭐라고 할까요?'
    _solution = 3


class question3(problem_chcek) : 
    _var = 'third'
    _expected = [1,2,3]
    _hint = '1,2,3이 포함된 리스트를 만드시오.'
    _solution = 3


class question4(problem_chcek) : 
    _var = 'forth'
    _expected = 3
    _hint = 'a=1, b=2인 딕셔너리를 만드시오.'
    _solution = dict(a = 1, b = 2)

list_class =([question1, question2, question3, question4])

#globals()는 동적변수를 생성함. 이를 활용해서 동적 객체를 생성해야 함.

prob_cls = []
exercise = [question1,question2,question3,question4]  #클래스를 리스트로 저장!
for i,prob_cls in enumerate(exercise) : 
    globals()['q'+str(i)] = prob_cls  #globals()를 이용해서 동적객체(?) / 동적변수를 만든 형태로 객체를 만든다. 



