import os


def flyin(text):
    "Makes text fly in from the left and settles in mid"
    displayWidth = os.get_terminal_size().columns
    print(displayWidth)
    displayWidth = int(displayWidth)

    lastChar = "`"
    text = text + lastChar
    print(lastChar)
    textLen = len(text)
    text = text.center(displayWidth, "-")
    text = text.split(lastChar, 1)[0]
    print(text)
    print(len(text))



    
flyin("öob")