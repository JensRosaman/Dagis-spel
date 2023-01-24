import os
from time import sleep
import keyboard as k


balls = ""
a = "██████╗░░█████╗░░██████╗░██╗░██████╗███████╗████████"
b = "██╔══██╗██╔══██╗██╔════╝░██║██╔════╝██╔════╝╚══██╔══╝"
c = "██║░░██║███████║██║░░██╗░██║╚█████╗░█████╗░░░░░██║░░░"
d = "██║░░██║██╔══██║██║░░╚██╗██║░╚═══██╗██╔══╝░░░░░██║░░░"
e = "██████╔╝██║░░██║╚██████╔╝██║██████╔╝███████╗░░░██║░░░"
f = "╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░"
nuts = ["b", "x", "r"]
stopPressed = False
space = ""
width = os.get_terminal_size().columns
aLen = len(a)
bLen = len(b)


os.system("color a")


while not k.is_pressed(" ") and stopPressed is False:
    while len(a) != width:
        os.system("cls")
        a = " " + a
        print(a)
        sleep(0.1)
        if k.is_pressed(" "):
            stopPressed = True
            break

    while len(a) != aLen:
        os.system("cls")
        a = a[1:]
        print(a)
        sleep(0.01)
        if k.is_pressed(" "):
            stopPressed = True
            break

## Stage two
sleep(0.05)
stopPressed = False 
while not k.is_pressed(" ") and stopPressed is False:
    while len(b) != width:
        length = len(b) - 1
        for i in range(length):
            space = space

        print(space, end="\r")
        b = " " + b
        print(b, end="\r")
        sleep(0.1)
        if k.is_pressed(" "):
            stopPressed = True 
            break

    while len(b) != bLen:
        length = len(b) - 1
        print(space, end="\r")
        b = b[1:]
        print(b, end="\r")
        sleep(0.01)
        if k.is_pressed(" "):
            stopPressed = True
            break 

print(balls)
print("1" + balls)