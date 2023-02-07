import os
from time import sleep
import keyboard as k
import random

balls = ""
a = "█████████████████████████████████████████████████████"
b = "█████████████████████████████████████████████████████"
c = "█████████████████████████████████████████████████████"
d = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
e = "██████╔╝██║░░██║╚██████╔╝██║██████╔╝███████╗░░░██║░░░"
f = "╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░"
nuts = ["b", "x", "r"]
stopPressed = False
space = ""
width = os.get_terminal_size().columns
aLen = len(a)
bLen = len(b)
index = 0

colors = ["0", "1","2","3","4","5","6","7","8","9","a"]
print("color" + colors[1])
os.system("color " + colors[1])


while not k.is_pressed(" ") and stopPressed is False:
    os.system("color " + colors[index])
    index = index + 1
    
    if index > 10:
        index = 0
    while len(a) != width:
        a = " " + a
        print(a)
        sleep(0.01)
        if k.is_pressed(" "):
            stopPressed = True
            break
    
    os.system("color " + random.choice(colors))
    while len(a) != aLen:
        a = a[1:]  
        print(a)
        sleep(0.01)
        if k.is_pressed(" "):
            stopPressed = True
            break
 ## Stage two
sleep(1)

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

sleep(1)

stopPressed = False 
while not k.is_pressed(" ") and stopPressed is False:
    while len(c) != width:
        length = len(c) - 1
        for i in range(length):
            space = space

        print(space, end="\r")
        c = " " + c
        print(c, end="\r")
        sleep(0.1)
        if k.is_pressed(" "):
            stopPressed = True 
            break

    while len(c) != bLen:
        length = len(c) - 1
        print(space, end="\r")
        c = c[1:]
        print(c, end="\r")
        sleep(0.01)
        if k.is_pressed(" "):
            stopPressed = True
            break 
print("\n")
a = a.strip(" ")
print(a)
print("1" + balls)