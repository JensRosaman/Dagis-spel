import keyboard as k
import time as t

def key():
    while not k.is_pressed('o'):
        print("deex nuts")


def timed():
    start = t.strftime("%S",t.localtime())
    start = int(start)
    print(f"start tiden är {start}")
    print(t.localtime()[4])
    slut = t.strftime("%S",t.localtime())
    slut = int(slut)
    räka = 0
    while (start + 3) > slut:
        print(räka)
        räka = räka + 1
        slut = t.strftime("%S",t.localtime())
        slut = int(slut)
        t.sleep(1)

def sek():
   return int(t.strftime("%S",t.localtime()))

def timer(slut):
    nuTid = int(sek())
    if slut <= nuTid:
        return 1
    else: return 0
    
slut = int(t.strftime("%S", t.localtime()))
slut = int(t.strftime("%M", t.localtime()))
längd = 59
slut = slut + längd
while timer(slut) != 1:
    print(slut - int(sek()))
    t.sleep(1)
print(0)