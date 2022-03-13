
from IPython.display import IFrame
from study_python import color_output as c

def question_entry() : 
  url_question = ['https://playentry.org/ws/62285c5c096ca500fe6104aa']
  url_solution = ['https://playentry.org/ws/62289461b47f14016a1cd639']
  return IFrame(url_question[0], width = '100%', height = 375)

def solution_entry() : 
  url_question = ['https://playentry.org/ws/62285c5c096ca500fe6104aa']
  url_solution = ['https://playentry.org/ws/62289461b47f14016a1cd639']
  return IFrame(url_solution[0], width = '100%', height = 375)

class variable() : 
  def check() : 
    bag = '수학책'
    print(c.bc_gray+"bag = '수학책'\nprint(bag)"+c.reset)
    print('\npring(bag) 결과입니다.')
    print(bag)

