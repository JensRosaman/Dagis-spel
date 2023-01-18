import random as rand
from time import sleep as sleep
from playsound import playsound
import os


items = ["bomb", "Farmor bertas aska", "Gregs ADHD piller, Cigarette"]

class npc:
    brittaCrystal = False
    ragnarMet = False
    brittabrittaAnger = 0
    brittasOverwatch = True
    bernardTrash = False
    

class data:
    cash = 5

    
    

    



def setSpeed(txtSpeed):
    "Sets the speed for the slowtxt function, requires a number between 1 - 10 where 1 is the slowest"
    txtSpeed = txtSpeed ** -1
    txtSpeed = txtSpeed / 100
    global textSpeed
    textSpeed = txtSpeed

def slowtxt(text):
    "Outputs strings one charachter at a time with a delay dictated by the 'setspeed()' function usage: inputs a string as a argument"
    for char in text:
        print(char, end="",flush=True)
        sleep(textSpeed)
    print("\n")

def check(answer, wanted):
    "Checks if the desired string is in the answer follows answer , wanted"
    answer = answer.lower()
    for word in wanted:
        if answer is not None and word in answer:
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
    



## Locations

def classroom(time, name, brittaAnger): 
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
            brittaAnger = brittaAnger + 1
    while True:
        choice =  input("-->")

        if choice == 1:
            gunn_marieclassroom() 
        if choice == 2:
            brittaclassroom()
        #brittaAnger ska behållas i moduler, 3 brittaAnger för atombomb. gunn marie och britta funktioner ska ligga i moduler.py. 

def lunch():
    "The lunch period."
    slowtxt("""
    - Okej klassen det är nu dags för lunch, kom med mig! Meddelar Britta och du går in i stora matsalen
    
    Väl där in slås du av den avskyvärda lukten och går och sätter dig vid din plats med ett glas vatten
    tilsammans med resten av klassen .
    Hela klassen sitter vid samma bord------------- Kön har nu minskat och du skulle kunna gå och 
    hämta mat. Vid dörren ut till korridoren står Britta och vaktar och hon lär inte flytta sig på ett tag.
    """)

# brittas ilska öka du dör, 
def schoolyard(data):
    slowtxt("""
    Med ett tjut så kör klockan igång med ett dövande ljud
    
    - Okej klassen lunchen är över, res på rumporna och gå ut innan jag behöver hämta Bernard.

    Du gör som Britta säger och kliver ut i det blindade solskenet hela klassen splitrar på sig och går
    till var sin del av skolgården. Själv står du kvar bredvid Britta vid dörren lite obestämt om vart du ska gå.

    I högra hörnet vid soptunnorna står Bernard och gräver en rektangulär grop med en avläng sopsäck bredvid
    när du kollar på honom så ler hann lite snett. På andra sidan skolgården så 
    """)

def bernardCorridoor(time):
    slowtxt(f"""Hallå där borta, vad gör du ute i korridoren så här sent, borde inte du ha lektion? 
                Vet du vad, jag bryr mig inte, kan du hjälpa mig bära den här säcken till köket?\n \n 
                På golvet bredvid Bernard ligger en skumt formad påse. Jag är sen men borde jag hjälpa eller bara gå till klassrummet?""")
    time = time - 1

    
# Ej klar , lägg till check om man träffat hnm
def bathroom():
    "The room bathroom, only incudes interactions with 'Ragnar'"
    ShopItems = ["kapten Konrads Krut - 10 Riksdaler", 
                        "Gunnar Gröna Gummibjönar - 3 Riksdaler", 
                        "Pers pallade äpplen - 4 Riksdaler",
                        "Kalles Kristall Godis - 9 Riksdaler"]
    if npc.ragnarMet is True:                      
        slowtxt("""Du tar ett stort kliv in i det mörka rummet med endast en lampa som fungerar. /n 
        Borta i andra änden av rummet så står en klasskammrat och skymer sig i mörkret\n""")
    
    
    slowtxt("""Vill du kasta tärning eller vill du ta en titt på mitt utbud?, efter en sekund så fortsätter han; 
    \n Annars så tycker jag att du drar här ifrån!\n""")
    slowtxt("Stannar du kvar, eller går du ut?")
    
    # The shop
    if check(input("-->"), ["ja", "stanna", "yes" , "spela", "köpa", "oui"]):
        slowtxt("Så vad blir det, köpa eller spela?")
        ragnarMenu = input("-->")
        if check(ragnarMenu, ["köpa", "affär"]):
            shopItems = ["1. kapten Konrads Krut - 10 Riksdaler", 
                        "2. Gunnar Gröna Gummibjönar - 3 Riksdaler", 
                        "3. Pers pallade äpplen - 4 Riksdaler",
                        "4. Kalles Kristall Godis - 9 Riksdaler"]
            
            for item in shopItems:
                print(item)
            
            print(f"Just nu har du {data.cash}")
            slowtxt("- Så vad blir det?")
            
            while True:
                pass
            
            
             
            
            
            
            
        
    

def finalboss():
    pass

# NPC

def britta():
    
    if period == 1:
    
        slowtxt(f"""Hörrudu, ska inte du jobba eller? 
        Du vet ju att elever som inte jobbar får F. Tillbaks till din bänk med dig, eller vänta.
        Du råkar inte ha något sånt där blått kristallgodis eller?""")

        if yes:
            slowtxt(f"""\"Ge det till mig!\" Britta rycker ut godiset ur din ficka innan du hinner reagera. \"Okej klassen, jag kommer strax tilbaka, jobba flitigt nu!\" Säger Britta, sen lämnar hon klassrummet.""")
            brittasOverwatch = False
        else:
            slowtxt(f"""Nähä? Vad gör du här då, tillbaks till din bänk innan jag tar fram tofflan!""")

    if period == 2:
        if brittaCrystal == True:
            slowtxt(""" - Hallå elever får inte lämna matsalen under lunchen.
            Fast du råkar inte veta var det finns mer kristallgodis eller? 
            Om du gör det kan du ju gå och hämta det till Britta. Vill du ut?"""
            
            )
            if yes:
                slowtxt(""" - Om du inte kommer tillbaka med något godis blir det tofflan! Och säg inte om det här till någon!""")
                #till korridoren med dig
        else: 
            slowtxt(""" - Hallå elever får inte lämna matsalen under lunchen. Fast vänta, du råkar inte ha något blått kristallgodis eller?""")
            if yes:
                slowtxt(""" - Okej klassen, Jag kommer strax tillbaka. Bete er nu och ät er soppa! Det finns mycket nyttigt i den. Säger Britta och lämnar klassrummet""")
            else:
                slowtxt(""" - Nähä, bort med dig då, gå och ät din soppa med de andra snorungarna.""")

def gunn_marieclassroom():
    pass

def ragnarsdesk(time):
    if brittasOverwatch is True:    
        
        slowtxt(f"""Du går för att öppna Ragnars bänk, kanske finns något intressant där inne?  
        \"Hörrudu! Det där är väl ändå inte din bänk eller? Tillbaks din din plats eller så skickar jag dig till rektorn!\" 
        hör du Britta säga. Jag får testa igen när hon är distraherad. """)
        brittaAnger = brittaAnger + 1
        time = time + 1

    else:

        slowtxt(f"""Du går för att öppna Ragnars bänk, det kanske finns något intressant där inne? 
        Du öppnar bänken och det ser ut som ett totalt bombnedslag, saker överallt. 
        Du fortsätter rota runt lite tills du ser något glansigt.""")

        if check(input(), ["ja", "japp", "inspektera", "kolla", "kika" ]):
        
            slowtxt(f"""Du tar upp objektet. Det verkar vara någon sorts TEMPORARY.
             Du lägger den snabbt i fickan och stänger Ragnars bänk innan Britta ser något.""")

            addinv("Ragnars objekt")
            time = time + 1
        else:

            slowtxt(f"""Du lägger tillbacka objektet och stänger Ragnars bänk innan Britta ser något""")
            time = time + 1
            

def food():
    slowtxt(f"""Du går fram till mattanten och visar upp din skål.
    -Här får du lite soppa, det finns alltid mer om du vill ha!
    Du kollar ner i skålen och ser en grå soppa som ser giftig ut.""")
    addinv("Skolans Soppa")
    