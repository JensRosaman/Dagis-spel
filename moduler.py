import random as rand
from time import sleep as sleep
from playsound import playsound
import os
anger = 0


items = ["bomb", "Farmor bertas aska", "Gregs ADHD piller, Cigarette"]

def setSpeed(txtSpeed):
    "Sets the the delay between each charachter in the 'slow"
    global textSpeed
    textSpeed = txtSpeed


def slowtxt(text):
    "Outputs strings one charachter at a time with a delay dictated by the 'setspeed()' function"
    for char in text:
        print(char, end="",flush=True)
        sleep(textSpeed)
    print("\n")

def check(answer, wanted):
    "Checks if the desired string is in the answer"
    for word in wanted:
        if answer != None and word in answer:
            return True
    
        else:
            return False


def clear():
    os.system('cls')

# Inventory functions 

def addinv(newItem):
    'Adds a new item to the inventory'
    newItem = str(newItem)
    items.append(newItem)

def extractItem(extrRquest):
    "Checks if the requested item is in the inventory and removes it"
    if extrRquest in items:
        items.remove(extrRquest)
        return extrRquest
    else:
        return "no"

def inventory():
    'Displays the users inventory and allows the user to interact with it'
    if len(items) > 0 :
            for item in items:
                # Prints items in items in a numbered list, +1 from their index so list starts at 1 instead of 0.
                slowtxt(f"{items.index(item)+1}. {item}") 
        
                while True:
                    slowtxt("Vad nu?\n 1.Pilla på något \n2. Stäng ner")
                    invChoice = input("-->")
                    # Allows user to interact with an item by choosing from their items
                    if invChoice == "1":
                        slowtxt("Vilket objekt vill du inspektera? (skriv talet i listan)")
                        objChoice = input("-->")
                        objChoice = int(objChoice)
                        #Subracts one in order to correspond to the index of the items list.
                        objChoice = objChoice - 1
                        slowtxt(f"Vad vill du göra med {items[objChoice]}")
                        input("-->")
                    
                    
                    # Exits the loop and sends user back to the room they previously were.
                    if invChoice == "2":
                        break
    # Inform the user that the inventory is empty and dont run the function.
    elif len(items) < 1:
        slowtxt("Din väska är tom")
        sleep(0.5)
    



# Locations

def classroom(time, name, anger): 
    #Classroom is only availible in the morning.
    "Contains all the code for the 'room' classroom in the game, contains code for conversation items to interact and mini game"
    if time == 6:
            slowtxt("""Du går in i klassrummet. Vid tavlan står Britta och ser arg ut som vanligt. På bänken till vänster om dig sitter
                    Gunn-Marie och babblar om något. Bänken till höger om dig är tom, Det är Ragnars bänk. Utöver Ragnar verkar resten
                     av klassen vara där. \"TYSTNAD!\" säger Britta till klassen men ingen verkar lyssna. Vad vill du göra?""")
        
    else:
            text = f"""\"Du är jävligt sen, du borde skämmas {name} men jag är inte överasskad\" hör du läraren Britta säga.
                         Ingen gillar henne egentligen men alla andra lärare slutade så det blir inte bättre än Britta. På 
                         bänken till vänster om dig sitter Gunn-Marie och babblar om något. Bänken till höger om dig är tom, 
                         Det är Ragnars bänk. Utöver Ragnar verkar resten av klassen vara där. Britta fortsätter med 
                         sin genomgång fast klassen verkar inte så intresserad. Vad vill du göra?"""
            slowtxt(text)
            anger = anger + 1
    while True:
        data = [time,cash]
        choice =  input("-->")

        if choice == 1:
            gunn-marie() 
        if choice == 2:
            britta()
        #anger ska behållas i moduler, 3 anger för atombomb. gunn marie och britta funktioner ska ligga i moduler.py. 

def food():
    pass

def BernardKorridor(time):
    slowtxt(f"""Hallå där borta, vad gör du ute i korridoren så här sent, borde inte du ha lektion? 
                Vet du vad, jag bryr mig inte, kan du hjälpa mig bära den här påsen till sopptunnan? \n \n 
                På golvet bredvid Bernard ligger en svart påse så full att det läcker någon vätska från öppningen.
                 Det ser ut som ketchup, den kanske kommer från matsalen? Jag skulle kunna fråga honom eller bara hjälpa till. """)
    time = time - 1

def bathroom():
    slowtxt("""Du tar ett stort kliv in i det mörka rummet med endast en lampa som fungerar. /n 
    Borta i andra änden av rummet så står en klasskammrat och skymer sig i mörkret \n \n Vill du spela """)
    pass

def finalboss():
    pass

# NPC