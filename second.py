from IPython.display import display, Markdown, HTML

def start() : 
    display(HTML("<style>.container { width:80% !important; }</style>"))

def color_text(text, color, add_ = ' '):
    infomation = '<span style="color:{}">{}</span> {}' .format(color, text, add_)
    return display(Markdown(infomation))

from IPython.display import IFrame

def question_1() : 
  url_question = ['https://playentry.org/ws/625f9f1425afa902a125e2c1']
  return IFrame(url_question[0], width = '100%', height = 650)


def question_2() : 
  url_question = ['https://playentry.org/ws/62285c5c096ca500fe6104aa#']
  return IFrame(url_question[0], width = '100%', height = 650)

def question_3() : 
  url_question = ['https://playentry.org/ws/6260e8a115cd40009e972fc8']
  return IFrame(url_question[0], width = '100%', height = 650)

def question_4() : 
  url_question = ['https://playentry.org/ws/62ac8fc5d5597a04b9954069']
  return IFrame(url_question[0], width = '100%', height = 650)

def entry_exercise() : 
  url_question = ['https://playentry.org/ws/62ac9c816ea89d001b2f578f']
  return IFrame(url_question[0], width = '100%', height = 650)


