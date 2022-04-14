from IPython.display import display, Markdown, HTML

def start() : 
    display(HTML("<style>.container { width:80% !important; }</style>"))

def color_text(text, color, add_ = ' '):
    infomation = '<span style="color:{}">{}</span> {}' .format(color, text, add_)
    return display(Markdown(infomation))