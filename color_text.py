from IPython.display import display, Markdown

def color_text(text, color, add_ = ' '):
    infomation = '<span style="color:{}">{}</span> {}' .format(color, text, add_)
    return display(Markdown(infomation))