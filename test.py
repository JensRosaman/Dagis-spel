import os

def flyin(text):
    displayWidth = os.get_terminal_size().columns
    print(displayWidth)
    displayWidth = int(displayWidth)
    lastChar = text[-1]
    textLen = len(text)
    text = text.center(displayWidth, " ")
    text = text.split(lastChar)
    print(text)
    print(len(text))
flyin("bob")