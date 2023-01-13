import time as t
from playsound import playsound

def tid(slut):
    nuTid = t.time()
    if slut <= nuTid:
        return 1
    else: return 0

def jg():
    slut = t.time()
    längd = 5
    slut = slut + längd
    while tid(slut) != 1:
        tidKvar = int(slut) - int(t.time())
        print(tidKvar)
        t.sleep(1)
    print(0)

def timer(längd, slut):
    slut = slut + längd
    if tid(slut) != 1:
        tidKvar = int(slut) - int(t.time())
        print(tidKvar)
        return True
    else:
        print("bob")
        return False

start = float(t.time())
while timer(5, start):
    t.sleep(1)
    
