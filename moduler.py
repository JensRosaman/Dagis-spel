import random
from time import sleep as sleep
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

shopItems = ["1. kapten Konrads Krut - 10 Riksdaler", 
                        "2. Gunnar Gröna Gummibjönar - 3 Riksdaler", 
                        "3. Pers pallade äpplen - 4 Riksdaler",
                        "4. Kalles Kristall Godis - 9 Riksdaler"]    
    

    
### SYSTEM FUNCTIONS


def setSpeed(txtSpeed):
    "Sets the speed for the slowtxt function, requires a number between 1 - 10 where 1 is the slowest usage: setspeed(INTEGER)"
    txtSpeed = txtSpeed ** -1
    txtSpeed = txtSpeed / 100
    global textSpeed
    textSpeed = txtSpeed

def slowtxt(text):
    "Outputs strings one charachter at a time with a delay dictated by the 'setspeed()' usage: slowtext(STRING)    "
    for char in text:
        print(char, end="",flush=True)
        sleep(textSpeed)
    print("\n")

def check(answer, wanted):
    "Checks for a list of substrings inside the argument usage: if check(INPUT,[LIST OF WANTED SUBSTRINGS]):"
    answer = answer.lower()

    # Block of code checks for special commands such as inventory
    if "väska" in answer:
        inventory()
        return False

    elif "avsluta" in answer:
        slowtxt("Hejdå O/")
        sleep(1)
        os.system("EXIT")


    for word in wanted:
        if answer is not None and word in answer:
            return True
    
    return False

def clear():
    os.system('cls')







# Inventory functions 

def addinv(newItem):
    'Adds a new item to the inventory usage: addinv("THE ITEM")'
    newItem = str(newItem)
    items.append(newItem)

def extractItem(extrRquest):
    "Checks if the requested item is in the inventory and removes it usage: extractItem("
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
    



### Locations

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

    

def bathroom():
    "The room bathroom, only incudes interactions with 'Ragnar'"
    ShopItems = ["kapten Konrads Krut - 10 Riksdaler", 
                        "Gunnar Gröna Gummibjönar - 3 Riksdaler", 
                        "Pers pallade äpplen - 4 Riksdaler",
                        "Kalles Kristall Godis - 9 Riksdaler"]
    if npc.ragnarMet is False:                      
        slowtxt("""Du tar ett stort kliv in i det mörka rummet med endast en lampa som fungerar.
        Borta i andra änden av rummet så står en klasskammrat och skymer sig i mörkret\n""")
        npc.ragnarMet = True

    else:
        slowtxt("""När du återigen stiger in i det illa luktande badrummet så står en bekant skepnad på samma ställe. """)
    
    
    
    slowtxt("""
    Vill du kasta tärning eller vill du ta en titt på mitt utbud?, efter en sekund så fortsätter han; 
    
    - Annars så tycker jag att du drar här ifrån för här är det endast Rangar och hans kunder som får härja!\n""")
    
    
    slowtxt("Stannar du kvar, eller går du ut?")
    
    # The shop
    if check(input("-->"), ["ja", "stanna", "yes" , "spela", "köpa", "oui"]):
        slowtxt("Så vad blir det, köpa eller spela?")
        ragnarMenu = input("-->")
        if check(ragnarMenu, ["köpa", "affär"]):
            rangnarShop()

        elif check(ragnarMenu, ["spela", "casino", "tärning"]):
            rangarDices()
        
        elif check(ragnarMenu, ["gå", "ut", "nej"]):
            



### GAMES

def rockPaperScissor():
  "Simulates a game of rockpaper scissors Gets input from the user and randomizes its own and returns the result"
  stop = True
  while stop:
    slowtxt("Vad Väljer du; sten , sax eller påse?")
    playerInput = input("-->").lower()
    for acceptedInput in ["sten" , "sax" , "påse"]:
      if acceptedInput in playerInput:
        playerInput = acceptedInput
        stop = False
        break

  botPick = random.choice(range(2))
  print(botPick)
  
 # Assignes a string based on the randomized number
  
  if botPick == 0:
    botPick = "sten"
    
  elif botPick == 1:
    botPick = "sax"

  elif botPick == 2:
    botPick = "påse"

  # Compares the bots choice and the player and checks for win conditions
    
  if botPick == playerInput:
    return "draw"

  elif botPick == "sten":
    if playerInput == "påse":
      return "win"
    else:
      return "loss"

  elif botPick == "påse":
    if playerInput == "sax":
      return "win"
    else:
      return "loss"
    
  elif botPick == "sax":
    if playerInput == "sten":
      return "win"
  else:
    return "draw"



def TicTacToe():
  'Simulates the game TicTacToe against a bot. Returns "win" , "draw" , "loss"  - depending on corresponding circumstance'
  one = " "
  two = " "
  three = " "
  four = " "
  five = " "
  six = " "
  seven = " "
  eight = " "
  nine = " "
  cords = [one , two , three , four , five , six , seven , eight , nine]
  board = f"""
    {cords[0]}  I  {cords[1]}  I  {cords[2]}
   --- I --- I ---
    {cords[3]}  I  {cords[4]}  I  {cords[5]}
   --- I --- I ---
    {cords[6]}  I  {cords[7]}  I  {cords[8]}
  """

  
  while " " in cords:

    # Collects each of the value in a row/collumn and stores it in a list used for checking for three in a row
    topRow = [cords[0],cords[1],cords[2]]
    middleRow = [cords[3],cords[4] , cords[5]]
    bottomRow = [cords[6],cords[7] , cords[8]]
    bottomDiagonal = [cords[6],cords[4] , cords[2]]
    topDiagonal = [cords[0] , cords[4] , cords[8]]
    leftCollumn = [cords[0] , cords[3] , cords[6]]
    middleCollumn = [cords[1] , cords[4] , cords[7]]
    rightCollumn = [cords[2] , cords[5] , cords[8]]

    # Visual representation of the playing board
    board = f"""
    {cords[0]}  I  {cords[1]}  I  {cords[2]}
   --- I --- I ---
    {cords[3]}  I  {cords[4]}  I  {cords[5]}
   --- I --- I ---
    {cords[6]}  I  {cords[7]}  I  {cords[8]}
    """

    # Checks for win, by removing duplicates and checking if theres only one left
    allRows = [topRow,middleRow,bottomRow,bottomDiagonal,topDiagonal,leftCollumn,middleCollumn,rightCollumn]
    for row in allRows:
        row = set(row)
        if not " " in row and len(row) == 1:
          if "X" in row:
            print("Grattis du vinna mkt bra")
            return "win"
          
          else:
            print("L bozo")
            return "loss"

    
    # X's turn X is the player and requires input
    print(board)
    while True:

      # Gets input and checks if it is as expected
      while True:
        newMoveX = input("Vilken ruta vill du kryssa? Obs ett tal mellan 1 - 9 som numrerar rutorna höger->väntster ")
        try:
          newMoveX = int(newMoveX)
          if newMoveX in range(1,9):
            break
          
          else:
            print("Obs endast tal mellan 1 - 9")
        except:
          print("Obs endast tal mellan 1 - 9")
      newMoveX = newMoveX - 1
      if cords[newMoveX] == " ":
        cords[newMoveX] = "X"
        break
      print("Den rutan är redan tagen gubben, välj en ny")

    # O's turn, compleatly dicated by chance
    if " " in cords:
      # Randomizes a number until it has found an usable one with no letter assinged
      while True:
        newMoveO = random.choice(range(0,8))
        if cords[newMoveO] == " ":
          break
      cords[newMoveO] = "O"

  # Outside while loop -> whole board filled -> draw
  return "draw"



def rangarDices():
    "Gambeling randomizes two number and a match yields a win"
    dieNumber = [1 , 2 , 3 , 4, 5, 6]
    result = []
    badInput = 0
    print("\nDu har just nu ", data.cash)
    slowtxt("""Hur mycket bettar du?
    Det rekomenderas att bara försöka beta pengar i heltal, Rangar gillar inte folk som leker run med han""")
    while True:
        diceBet = input("-->")
        # If thy shan't follow basic intstructions than thy shall feel order 66,  If the user writes the wrong input ten times kill the program 
        if badInput == 10:
            os.system("cls")
            sleep(0.5)
            slowtxt("""
            Rangar bröt många av dem tio budorden den dagen 
            och du slapp göra matteprovet för du är nu på en bättre plats.""")
            slowtxt("Må du vila i frid")
            sleep(1)
            os.system("exit")
        
        try:
            diceBet = int(diceBet)
            break
        except:
            slowtxt("Du kan bara betta pengar, så skriv ett vanligt heltal utan skräp innan Rangar bankar ner dig")
            badInput = badInput + 1

    # Simulates two dices being thrown and adds them to the result
    result.append(random.choice(dieNumber))
    slowtxt("Din första tärning blev:")
    print(result[0])
    result.append(random.choice(dieNumber))
    slowtxt("Din andra tärning blev:")
    print(result[1])
    print(result)

    # When the two dices match the set operation removes one of them and results in the length = 1
    if len(set(result)) == 1:
        diceBet = int(diceBet) * 2
        

        print("Du vann")



def rangnarShop():
    "Handles all of the shop from the NPC Rangar"
    slowtxt("Här är det jag har att erbjuda:")
    for item in shopItems:
        slowtxt(item)        
            
    print(f"\nJust nu har du {data.cash} riksdaler")
    slowtxt("- Så vad blir det?")
            
    while True:
        shopChoice = input("\n-->")
        if check(shopChoice, ["kapten", "konrads" ,"krut","1"]):

                addinv("kapten Konrads Krut")
                
        elif check(shopChoice, ["2" "gunnar" "gröna" "gummibjönar"]):
                addinv("Gunnar Gröna Gummibjönar")

        elif check(shopChoice, ["3" "Pers" "pallade" "päron"]):
                addinv("Pers pallade äpplen")
                
        elif check(shopChoice, ["4", "kalles", "kristall", "godis"]):
                addinv("Kalles Kristall Godis")

        slowtxt("\nNågot mer?")

        if check(input("-->"), ["n","nej","nope"]):
                    
            break        
                
                
            
            
             
            
            
            
            
        
    

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
        if npc.brittaCrystal == True:
            slowtxt(""" - Hallå elever får inte lämna matsalen under lunchen.
            Fast du råkar inte veta var det finns mer kristallgodis eller? 
            Om du gör det kan du ju gå och hämta det till Britta. Vill du ut?"""
            
            )
            if yes:
                slowtxt(""" - Om du inte kommer tillbaka med något godis blir det tofflan! Och säg inte om det här till någon!""")
                
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
    