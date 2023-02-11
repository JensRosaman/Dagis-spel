import random
from time import sleep as sleep
import os
import sys


items = ["bomb", "Farmor bertas aska", "Gregs ADHD piller, Cigarette"]

# Contains a list of possible outcomes that can change based on player interactions
class npc:
    brittaCrystal = False
    ragnarHaveMet = False
    brittaAnger = 0
    brittasOverwatch = True
    bernardTrash = False
    brittaHaveMetClassroom = False
    brittaLetOut = False
    ragnarFirstMeetYard = False
    binHaveSearched = False
    brittaCrystalCount = 0
    gunpowderInPipe = False
    
    

class data:
    cash = 5
    time = 0
    period = 1
    name = ""
    


shopItems = ["1. Kapten Konrads Krut - 7 Riksdaler",
                        "2. Kalles Kristall Godis - 5 Riksdaler"]    
    

    
### ---------------------------- SYSTEM FUNCTIONS -------------------------- ###


def setSpeed(txtSpeed):
    "Sets the speed for the slowtxt function, requires a number between 1 - 10 where 1 is the slowest usage: setspeed(INTEGER)"
    txtSpeed = txtSpeed ** -1
    txtSpeed = txtSpeed / 10
    global textSpeed
    textSpeed = txtSpeed

def slowtxt(text):
    "Outputs strings one charachter at a time with a delay dictated by the 'setspeed()' usage: slowtext(STRING)    "
    for char in text:
        print(char, end="",flush=True)
        sleep(textSpeed)
    print("\n")

def check(answer, wanted):
    "Checks for a list of substrings inside the argument usage: if check(INPUT,[LIST OF WANTED SUBSTRINGS]): also handels commands"
    answer = answer.lower()
    
    # Checks if the time is over 3 during the lunch period after every input
    if data.period == 2 and data.time > 3:
        data.period = 3
        data.time = 0
        schoolyard()
        return False

    # Check for inventory command
    for alternative in ["väska", "inv", "inventory", "lager"]:
        if alternative in answer:
            inventory()
            return False

    # Check for the exit command
    for alternative in ["exit", "avsluta", "quit"]:
        if alternative in answer:
            slowtxt("Hejdå O/")
            sleep(1)
            sys.exit()

     # Skip forward in time if stuck       
    for alternative in ["sov"]:
        if alternative in answer:
            data.time = data.time + 10000

            
    # Check for the time command
    for alternative in ["tid"]:
        if alternative in answer:
            print(f"Tiden är {data.time} och perioden är {data.period}")
            return
    # Check if the answer corresponds to the wanted answer
    for word in wanted:
        if answer is not None and word in answer:
            return True

def gameOver():
    if data.cash < 0:
        slowtxt(f"""
        Din Mamma fick däremot leva med dem enorma skulderna som du lyckades bygga under din dagisdag
        När kronofogden knackade på så var det inte mycket som de lämna Du var hela {data.cash} 
        riksdaler i skuld och det var mer än vad er familj kunde klara av""")
    sleep(2)
    slowtxt("\n\nGrattis du klarade ett av sluten det finns fler slut att upptäcka\nTack för att du spelade!")
    sleep(1)
    quit()

# ------------------ Inventory functions -----------------

def addinv(newItem):
    'Adds a new item to the inventory usage: addinv(THE ITEM)'
    newItem = str(newItem)
    items.append(newItem)

def extractItem(extrRquest):
    "Checks if the requested item is in the inventory and removes it usage: extractItem("
    if extrRquest in items:
        items.remove(extrRquest)
        return True
    else:
        return False

def inventory():
    'Displays the users inventory and allows the user to interact with it'
    if len(items) > 0 :
            for item in items:
                # Prints items in items in a numbered list, +1 from their index so list starts at 1 instead of 0 for uses capability
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
                    slowtxt(f"Du plockar upp och kollar på {items[objChoice]}")
                    
                    if items[objChoice] == "Kalles Kristall Godis":
                        slowtxt(f"""
            Detta är 92{'%'} rent kristall godis som britta gillar väldigt mycket och släpper allting hon
            håller på med för att förtära""")

                    elif items[objChoice] == "ragnars kniv":
                        slowtxt("Den här kniven har ragnar letat överallt efter han skulle nog uppskatta om du gav tillbaka den")


                    
                    # Exits the loop and sends user back to the room they previously were.
                if invChoice == "2":
                    return None
    # Inform the user that the inventory is empty and dont run the function.
    elif len(items) < 1:
        slowtxt("Din väska är tom")
        sleep(0.5)
    



### -------------------------------- Locations ------------------------------ 

def classroom(): #3 time in classroom
    #Classroom is only availible in the morning.
    "Contains all the code for the 'room' classroom in the game, contains code for conversation items to interact and mini game"
    if data.period == 2 or data.period == 3:
        slowtxt("Klassrummet är låst just nu.")
        return

    elif data.time == 0: #If you don't go to the classroom immediately time will be less than 6 and you're considered "late"
            slowtxt("""
        Du går in i klassrummet. Vid tavlan står Britta och ser arg ut som vanligt. 
        På bänken till vänster om dig sitter Gunn-Marie och babblar om något. 
        Bänken till höger om dig är tom, Det är Ragnars bänk. Utöver Ragnar verkar resten
        av klassen vara där. \"TYSTNAD!\" säger Britta till klassen men ingen verkar lyssna. 
        Vad vill du göra?""")
        
    else:
            slowtxt(f"""
         - Du är jävligt sen, du borde skämmas {data.name} men jag är inte överasskad... 
        hör du läraren Britta säga framför dig. Bäst om jag inte gör henne arg igen.
        Ingen gillar henne egentligen men alla andra lärare slutade så det finns ingen annan än Britta. 
        På bänken till vänster om dig sitter Gunn-Marie och babblar om något. 
        Bänken till höger om dig är tom, Det är Ragnars bänk. Utöver Ragnar verkar resten av klassen vara där. 
        Britta fortsätter med sin genomgång fast klassen verkar inte så intresserad. 
        Dina ögon tynger ner dig och du känner dig lite frestad att sova bänken för att fördriva tiden. 
        Vad vill du göra?""")
            npc.brittaAnger = npc.brittaAnger + 1
    while True:
        if data.time > 2:
            data.period = data.period + 1
            data.time = 0
            npc.brittasOverwatch = True
            lunch()
            return None


        classroomChoice =  input("-->")

        if check(classroomChoice, ["gunn", "gunn-marie", "vänster", "marie"]):
            gunn_marie() 
            data.time = data.time + 1
        elif check(classroomChoice, ["britta", "lärare", "fram", "framåt"]):
            britta()
            data.time = data.time + 1
        #brittaAnger ska behållas i moduler, 3 brittaAnger för atombomb. gunn marie och britta funktioner ska ligga i moduler.py. 
        elif check(classroomChoice, ["bänk", "höger", "ragnar",]):
            ragnarsDesk()
            data.time = data.time + 1
        elif check(classroomChoice, ["sov"]):
            data.time = data.time + 10000000

            
def lunch():
    while True:
        "The lunch period."
        #meny för att välja funktioner
        if data.period == 1 or data.period ==3:
                slowtxt("       Förvånade så är matsalen bara öppen när det är MAT, kom tillbaka senare")
                break
        elif data.period == 2 and npc.brittaLetOut == True:
            slowtxt("       - Så har du något kristallgodis nu?, säger Britta aggresivt.")
            brittaChoice = input("-->")
            if check(brittaChoice, ["ja"]) and extractItem("Kalles Kristall Godis"):
                slowtxt("       Britta tar ditt godis och lämnar klassrummet raskt, hon sa inte ens tack.")
                npc.brittasOverwatch = False
            else:
                slowtxt("""    
        - Din snorunge, jag släppte ju ut dig så du kunde hämta kristallgodiset! 
        Gå och ät nu men jag kommer komma ihåg det här.""")
                npc.brittaAnger = npc.brittaAnger + 1
        elif data.period == 2:
            slowtxt("""
        - Okej klassen det är nu dags för lunch, kom med mig! Meddelar Britta och du går in i stora matsalen
            
        Väl där in slås du av den avskyvärda lukten och går och sätter dig vid din plats med ett glas vatten
        tillsammans med resten av klassen. Hela klassen sitter vid samma bord
        
        Kön där framme har nu minskat och du skulle kunna gå och hämta mat. 
        Vid dörren ut till korridoren höger om dig står Britta och vaktar och hon lär inte flytta sig
        på ett tag. Vänster om dig finns en sopptunna, undrar om det finns något intressant i den. 
        Bredvid dig sitter Gunn-Marie och babblar på som vanligt.
        """)

        while True:
            lunchChoice = input("-->")

            if check(lunchChoice, ["britta"]):
                data.time = data.time + 1
                britta()
                if npc.brittaLetOut == True:
                    slowtxt("""
        Du är nu tillbaka i korridoren, till vänster om dig finns badrummet och framför dig ligger klassrummet. 
        Dörren till höger leder tillbaka till matsalen. Var vill du gå?
        """)
                    break

            elif check(lunchChoice, ["mat", "äta", "soppa", "hämta", "fram"]):
                data.time = data.time + 1
                food()
                
            elif check(lunchChoice, ["sopptunna", "sopor","tunna", "vänster"]):
                data.time = data.time + 1
                bin()

            elif check(lunchChoice, ["gunn", "marie"]):
                data.time = data.time + 1
                gunn_marie()
            elif check(lunchChoice, ["sov"]):
                data.time = data.time + 10000000
        break

def schoolyard():
    'The second to last room contains functions for communicating with several diffrent NPC'

    data.time = 0
    slowtxt("""
    Med ett tjut så kör klockan igång med ett dövande ljud
    
    - Okej klassen lunchen är över, res på rumporna och gå ut innan jag behöver hämta Bernard.

    Du gör som Britta säger och kliver ut i det blindade solskenet hela klassen splitrar på sig och går
    till var sin del av skolgården. Själv står du kvar bredvid Britta vid dörren lite obestämt om vart du ska gå.

    I högra hörnet vid soptunnorna står Bernard och gräver en rektangulär grop med en avläng sopsäck bredvid
    när du kollar på honom så ler hann lite snett. 
    På andra sidan skolgården i skuggan så lutar sig Ragnar mot staketet
    och i mitten av skolgården sitter Gunn-Marie och spelar Tre I Rad. 
    Sen finns det också ett väldigt fint järnrör borta i vänstra hörnet.
    """)
    while True:
        stopTalking = True
        yardChoice = input("-->")

        # ends function and begins next function when time is up
        if data.time > 2:
            mathTest()
            return None
        elif npc.brittaAnger > 2:
            slowtxt(f"""
            Medans du sitter ute på gården ser du helt plötsligt himlen bli röd och dagiset omkringas av åskmoln.
            
            Du hör ett argt skrik från Britta som får luften runt dig att vibrera.
            Hon går mot dig med aggresiva steg som lämnar hela skolgården skakandes. 
            Sen blir allt mörkt. Vila nu, du är på en bättre plats. Som tur är så finns det inga matteprov i himlen.""")
            gameOver()
            
        elif check(yardChoice , ["bernard", "grop" , "höger" , "sopsäck"]):
            data.time = data.time + 1
            bernard()
        
        elif check(yardChoice , ["britta","bredvid"]):
            data.time = data.time + 1
            britta()

        # Early ending
        elif check(yardChoice,["rör","järn"]):
            slowtxt("""
            Framför dig står ett järnrör som man
            skulle kunna fylla med något..""")

            if extractItem("Kapten Konrads Krut"):
                slowtxt("""
                Med väskan ned tyngt av Konrads Krut skulle detta vara ett fint ställe
                att göra lite fyverkirier. Du har ett par tändstickor i fickan och skulle
                kunna göra en fin explosion. Gör du det?""")

                while True:
                    pipeChoice = input("-->")
                    if check(pipeChoice,["ja","jo","yes"]):
                        slowtxt("""
                        Precis efter antänding så hörs det en extremt hög knall som skakar fönstrena på skolan.
                        Alla barnen på skolan skriker av rädsla och springer och gömmer sig vid Bernads grop.
                        Efter att polisen anlände så stängs skolan ner och provet blir inställt och
                        barnen går hem för dagen.""")
                    
                    elif check(pipeChoice,["nej","no","nope"]):
                        slowtxt("Du vänder dig om och ställer dig och kollar ut över skolgården, Vart går du nu?")
                        break


        elif check(yardChoice,["gunn", "marie","mitten","tre i rad"]):
            data.time = data.time + 1
            slowtxt("- Hej vill du tjäna lite para? Reglerna är simpla satsa pengar och spela vinner du så dubblar du din insats")
            if check(input("-->"),["ja","ok","visst","spela"]):
                slowtxt("Hur mycket satsar du? - Obs endast heltal")
                while True:
                    TicTacToeBet = input("-->")
                    try:
                        TicTacToeBet = int(TicTacToeBet)
                        break
                    except:
                        slowtxt("Obs skriv endast ett hel tal utan bokstäver")

                while stopTalking:
                    result = TicTacToe()
                    # Checks for the result of the game
                    if result == "win":
                        slowtxt("- Gratts du vann, bra spelat du är ju nästan bättre än min pojkvänn")
                        data.cash = data.cash + TicTacToeBet
                    elif result == "loss":
                        data.cash = data.cash - TicTacToeBet
                        slowtxt("- Ajdå stackarn, det händer oss alla.")
                    elif result == "draw":
                        slowtxt("- Det blev lika! Bra spelat")
                    
                    # checks whether to loop again or exit
                    while stopTalking:
                        slowtxt("\nVill du köra igen?")
                        gunnChoice = input("-->")
                        if check(gunnChoice,["ja","ok","visst","spela"]):
                            break
                        elif check(gunnChoice,["nej","nope","n"]):
                            slowtxt("Ok stör mig inte då, min pojkvän kanske ser osss då.")
                            stopTalking = False
            
            else:
                slowtxt("       Ok stör mig inte då, min pojkvän kanske ser osss då.")
                slowtxt("       Du går tillbaka till skolgården. Vart går du?")
        
        # interactions with Ragnar
        elif check(yardChoice , ["andra", "sidan" , "ragnar", "staketet"]):
            data.time = data.time + 1
            if npc.ragnarHaveMet:
                slowtxt("       - Ah det är du igen, hittade du min dolk?")
            
            else:
                slowtxt("       - Ey du kom hit, har du sett min dolk?")
            while True:
                ragnarChoice = input("-->")
                if check(ragnarChoice,["ja","hittade","y"]):
                    if extractItem("Ragnars kniv") or extractItem("Rostig Brödkniv"):
                        slowtxt("""
            Åh skönt räddarn i nöden asså. Trodde aldrig att skulle kunna få äta upp mina äpplen.
            Jag antar att du förtjänar något i gentjänst, jag hittade facit till matteprovet så 
            vad sägs om att vi kör sten sax påse om den? För tro mig jag kommer behöver den också.""")
                        while True:
                            result = rockPaperScissor()
                            if not npc.ragnarFirstMeetYard:
                                npc.ragnarFirstMeetYard = True
                                if result == "win":
                                    slowtxt("       - Näh jag svär jag såg dig fuska, aja ta den du vann")
                                    addinv("facit")
                                    break
                                    
                                elif result == "draw":
                                    slowtxt("       - Det blev lika, vi kör igen")
                                    result = rockPaperScissor()
                                    continue

                                elif result == "loss":
                                    slowtxt("       - Haha för enkelt, säg mig för 5 riksdaler låter jag köra igen")
                                    
                            if data.cash > 5:
                                slowtxt("       Så vad tycker du ska vi köra nu?")
                                if check(input("-->"),["ja","visst","absolut"]):
                                    data.cash = data.cash - 5
                                    rockPaperScissor()
                            else:
                                slowtxt("       Kom tillbaka när du har mer pengar och så kör vi")
                                slowtxt("       Du går tillbaka till skolgården. Vart går du?")
                                break
                        break
                        
                    # if theres no knife in inv
                    else:
                        slowtxt("       Varför ljuger du din åsna, jag ser ju att du inte har den, stick här ifrån")
                        slowtxt("       Du går tillbaka till skolgården. Vart går du?")

                        break
                    
                # skips dialougue
                elif check(ragnarChoice,["nej","vilken","nope","n"]):
                    slowtxt("       Synd att höra, jag hade för mig att den var i klassrummet. Aja ses")
                    slowtxt("       Du går tillbaka till skolgården. Vart går du?")
                    break


def mathTest():
    # The final stage of game, dictattes between the diffrent endings

    
    # First ending - triggers if player has 'facit' in the inventory
    if extractItem("facit"):
        slowtxt("""
        Du sätter dig ner lite darande i benen tills du kommer ihåg facitet som du fick av Ragnar.
        Men stor skicklighet så kollar du på facit utan att hon ser och kopierar svaren till punkt och pricka.
        Med ditt matte betyg räddat och din mammas stolthet försäkrad så lämnar du in provet och går hem.
        """)
        gameOver()

    else:
        slowtxt("""
        Med tunga steg och låga förhoppningar vandrar du in i provsalen och sätter dig ner och kollar på den
        första flersvars frågan: Vad är derivatan gånger två av den primitiva funktionen av y = 4?""")
        
        # Question 1
        testAlternatives = [
            "Svaret är 4",
            "Svaret är 8",
            "Du blundar, slår dig själv i huvudet och gissar på något och hoppas på det bästa"
        ]

        for alternative in testAlternatives:
            # Inserts the index of the item at the start so the output is numbered
            index = testAlternatives.index(alternative)
            index = int(index) + 1
            alternative = str(index) + ". " + alternative
            slowtxt(alternative)
        
        slowtxt("\nVilket alternativ kryssar du i")
        answerQuestion = input("-->")

        
        slowtxt("""
        Du går vidare till nästa fråga som lyder: 
        Om Gunnar von Gyllensköld har tre bollar och förlorar 1.5 bollar på två minuter
        Hur många grader blir då derivatan utryckt i en enhets cirkel?
        """)
        # Question one:
        testAlternatives = [
            "Ungefär 9 radianer",
            "odefinierat",
            "1.5x Radianer",]
        
        # Adds a new option to the menu
        if npc.brittaAnger > 1:
            testAlternatives.append("Rita ett crufix på pappret och be till de högre makterna och förfäderna\n att de räddar dig. Med tanke på hur arg och konstig britta har varit idag så\n kanske det tar ut demonen ur henne också")
        
        
        
        for alternative in testAlternatives:
            # Inserts the index of the item at the start so the output is numbered
            index = testAlternatives.index(alternative)
            index = int(index) + 1
            alternative = str(index) + ". " + alternative
            slowtxt(alternative)
        
        slowtxt("\nVilket alternativ kryssar du i")
        answerQuestion = input("-->")

        # Third ending, is possible when Britta has reached anger 2
        if check(answerQuestion,["4","be","förfäder","gud"]) and npc.brittaAnger > 1:
            slowtxt("""
            Med förhoppningarna på botten och motivationen lika så, ritar du
            ett detaljerat crusifix och lägger dig ner med med huvhudet mot bänken
            med händerna knäppta och beende.
            
            Så fort du lämnar in pappret till Britta och hon tar tag i pappret med 
            crucifixet så är det som ett hål till en annan värld öppnas
            under hennes fötter och hon faller ner till det brinnande inferno där nedan""")

            sleep(1)

            slowtxt("""
            Utan någon lärare att rätta proven så blev det inte heller något underkänt
            Vart Britta försvann den dagen är det fortfarande ingen som vet""")
            gameOver()

        slowtxt("""
        Efter fem till frågor av liknande karaktär så lämnade du in provet
        
        När resultatet väl kom så var det värre än du förväntade dig och du fick alla fel
        Din Mamma som själv är mattelärare blev väldigt besviken på dig.""")
        gameOver()
            


def bernard():
    data.time = data.time + 1
    if data.period == 1:
       
        slowtxt(f"""
        - Hallå där borta, vad gör du ute i korridoren så här sent, borde inte du ha lektion? 
        - Vet du vad, jag bryr mig inte, kan du hjälpa mig bära den här säcken till köket?\n \n 
        På golvet bredvid Bernard ligger en skumt formad påse. 
        Jag är sen men borde jag hjälpa eller bara gå till klassrummet?""")
        while True:
            bernardChoice = input("-->")
            if check(bernardChoice,["ja","y", "hjälp"]):
                slowtxt("       Du hjälper Bernard flytta den märkligt människoformade soppåsen. Som belöning ger han dig två riksdaler.")
                slowtxt("\n       Du är nu tillbaka i korridoren. Var vill du gå?")
                data.cash = data.cash + 2
                npc.bernardTrash = True
                break
            elif check(bernardChoice, ["nej", "gå", "klassrum"]):
                slowtxt("       - Nähä? Men säg inte till någon om det här då. Dags och gå till klassrummet nu min gosse.")
                break

    elif data.period == 3:
    
        if npc.bernardTrash:
            slowtxt("       Aha det är du igen din lilla krabat. Tror du att du kan hjälpa mig igen med något?")
            while True:
                bernardChoice = input("-->")
                if check(bernardChoice, ["ja"]):
                    slowtxt("""
        Du hjälper Bernard flytta ännu en märkligt människoformad soppsäck. 
        Denna var jättetung, mer än den förra men till slut lyckas ni få ner den i sopptunnan. 
        Som belöning ger han dig 4 riksdaler.""")
                    data.cash = data.cash + 4
                    break
                elif check(bernardChoice, ["nej"]):
                    slowtxt("       Ja det var ju synd men jag förstår att nu ynglingar är upptagna i er ålder. Det är ju snart dags att söka jobb och sånt.")
                    break
        else:
            slowtxt("    - Nä du kom inte hit. Här finns bara sopptunnan och den luktar inte så gott. Gå och lek med dina kompisar istället.")
            



def bathroom():
    "The room bathroom, only incudes interactions with 'Ragnar'"
    
    if data.time == 0 or data.time == 1:
        data.time = data.time + 1
        
    ShopItems = ["Kapten Konrads Krut - 10 Riksdaler", 
                        "Gunnar Gröna Gummibjönar - 3 Riksdaler", 
                        "Pers pallade äpplen - 4 Riksdaler",
                        "Kalles Kristall Godis - 9 Riksdaler"]
    if npc.ragnarHaveMet is False:                      
        slowtxt("""
        Du tar ett stort kliv in i det mörka rummet med endast en lampa som fungerar.
        Borta i andra änden av rummet så står en klasskammrat och skymer sig i mörkret\n""")
        npc.ragnarHaveMet = True

    else:
        slowtxt("När du återigen stiger in i det illa luktande badrummet så står en bekant skepnad på samma ställe.")
    
    
    
    slowtxt("""
        Vill du kasta tärning eller vill du ta en titt på mitt utbud?, efter en sekund så fortsätter han; 
    
        - Annars så tycker jag att du drar här ifrån för här är det endast ragnar och hans kunder som får härja!\n""")
    
    
    slowtxt("       Stannar du kvar, eller går du ut?")
    
    # Selection for the next path, calls a corresponding function
    if check(input("-->"), ["ja", "stanna", "yes" , "spela", "köpa", "oui"]):
        slowtxt("       Så vad blir det, köpa eller spela?")
        ragnarMenu = input("-->")
        if check(ragnarMenu, ["köpa", "affär"]):
            ragnarShop()

        elif check(ragnarMenu, ["spela", "casino", "tärning"]):
            ragnarDices()
        
        # Exits the room and returns to 'main.py'
        elif check(ragnarMenu, ["gå", "ut", "nej", "inget"]):
            slowtxt("Nähä, stick här ifrån då!")
            sleep(1)
            slowtxt("- Vänta föresten om du ser min dolk någonstans kom till mig")
            return None
            



### ------------------------ MiniGAMES ------------------ ###



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

 # Chooses a random number from a set of 3 which detrmines the bots output
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

  # Each one - nine corresponds to a point on the board going from left to right
  one = " "
  two = " "
  three = " "
  four = " "
  five = " "
  six = " "
  seven = " "
  eight = " "
  nine = " "
  coordinates = [one , two , three , four , five , six , seven , eight , nine]
  board = f"""
    {coordinates[0]}  I  {coordinates[1]}  I  {coordinates[2]}
   --- I --- I ---
    {coordinates[3]}  I  {coordinates[4]}  I  {coordinates[5]}
   --- I --- I ---
    {coordinates[6]}  I  {coordinates[7]}  I  {coordinates[8]}
  """

  
  while " " in coordinates:
    # Collects each of the value in a row/collumn and stores it in a list used for checking for three in a row
    topRow = [coordinates[0],coordinates[1],coordinates[2]]
    middleRow = [coordinates[3],coordinates[4] , coordinates[5]]
    bottomRow = [coordinates[6],coordinates[7] , coordinates[8]]
    bottomDiagonal = [coordinates[6],coordinates[4] , coordinates[2]]
    topDiagonal = [coordinates[0] , coordinates[4] , coordinates[8]]
    leftCollumn = [coordinates[0] , coordinates[3] , coordinates[6]]
    middleCollumn = [coordinates[1] , coordinates[4] , coordinates[7]]
    rightCollumn = [coordinates[2] , coordinates[5] , coordinates[8]]

    # Visual representation of the playing board
    board = f"""
    {coordinates[0]}  I  {coordinates[1]}  I  {coordinates[2]}
   --- I --- I ---
    {coordinates[3]}  I  {coordinates[4]}  I  {coordinates[5]}
   --- I --- I ---
    {coordinates[6]}  I  {coordinates[7]}  I  {coordinates[8]}
    """

    # Checks for win, by removing duplicates and checking if theres only one left
    allRows = [topRow,middleRow,bottomRow,bottomDiagonal,topDiagonal,leftCollumn,middleCollumn,rightCollumn]
    for row in allRows:
        row = set(row)
        if not " " in row and len(row) == 1:
          if "X" in row:
            print(f"""
    {coordinates[0]}  I  {coordinates[1]}  I  {coordinates[2]}
   --- I --- I ---
    {coordinates[3]}  I  {coordinates[4]}  I  {coordinates[5]}
   --- I --- I ---
    {coordinates[6]}  I  {coordinates[7]}  I  {coordinates[8]}
    """)
            print("Tre i rad!")
            return "win"
          
          else:
            print("L bozo")
            return "loss"

    
    # X's turn X is the player and requires input
    print(board)
    while True:

      # Gets input and checks if it is as expected
      while True:
        slowtxt("Vilken ruta vill du kryssa? Obs ett tal mellan 1 - 9 som numrerar rutorna höger->väntster")
        newMoveX = input("--> ")
        try:
          newMoveX = int(newMoveX)
          
          # check if number corresponds to coordinate
          if newMoveX in range(1,10):
            break
          
          else:
            slowtxt("Obs endast tal mellan 1 - 9")
        except:
          slowtxt("Obs endast tal mellan 1 - 9")
      newMoveX = newMoveX - 1
      if coordinates[newMoveX] == " ":
        coordinates[newMoveX] = "X"
        break
      print("Den rutan är redan tagen, välj en ny")

    # O's turn, compleatly dicated by chance
    if " " in coordinates:
      # Randomizes a number until it has found an usable one with no letter assinged
      while True:
        newMoveO = random.choice(range(0,8))
        if coordinates[newMoveO] == " ":
          break
      coordinates[newMoveO] = "O"

  # Outside while loop -> whole board filled -> draw
  return "draw"



def ragnarDices():
    "Gambeling randomizes two number and a match yields a win"
    dieNumber = [1 , 2 , 3 , 4, 5, 6]
    result = []
    badInput = 0
    print(f"Du har just nu {data.cash} riksdaler")
    slowtxt("""
    - Hur mycket satsar du?
    Det rekomenderas att bara försöka satsa pengar i heltal, ragnar gillar inte folk som leker runt med han""")
    while True:
        diceBet = input("-->")
        # If the user writes wrong input ten times kill the program 
        if badInput == 10:
            os.system("cls")
            sleep(0.5)
            slowtxt("""
            ragnar bröt många av dem tio budorden den dagen 
            och du slapp göra matteprovet för du är nu på en bättre plats.""")
            slowtxt("Må du vila i frid")
            sleep(2)
            exit()
        try:
            diceBet = int(diceBet)
            data.cash = data.cash - diceBet
            break

        # On invalid input inform the user.
        except:
            slowtxt("Du kan bara betta pengar, så skriv ett vanligt heltal utan skräp innan ragnar bankar ner dig")
            badInput = badInput + 1

    # Simulates two dices being thrown and adds them to the result
    result.append(random.choice(dieNumber))
    slowtxt("Din första tärning blev:")
    print(result[0])
    result.append(random.choice(dieNumber))
    slowtxt("Ragnars tärning blev")
    print(result[1])
    
    # When the first die is bigger than the second the player wins
    if result[0] > result[1]:
        data.cash = data.cash + int(diceBet) * 2
        diceBet = str(diceBet)        
        print(f"Du vann {diceBet}")
        slowtxt("""
        - Ut härifrån medans jag räknar mina pengar igen.
        
        Du går tillbaka till korridoren, Vart går du nu?""")
        return  None
    
    elif result[1] == result[0]:
        slowtxt("""
        Det blev lika, men huset vinner alltid så jag behåller pengarna
        - Ut härifrån medans jag räknar mina pengar.
        
        Du går tillbaka till korridoren, Vart går du nu?""")
        return None
    else:
        slowtxt(""" 
        - Ha! Jag vann
        - Ut härifrån medans jag räknar mina pengar.
        
        Du går tillbaka till korridoren, Vart går du nu?""")
        return None
        

def ragnarShop():
    "Handles all of the shop from the NPC ragnar"
    slowtxt("       Här är det jag har att erbjuda:")
    ### By defualt the shop includes:  
    # ["1. kapten Konrads Krut - 10 Riksdaler",
    # "2. Gunnar Gröna Gummibjönar - 3 Riksdaler", 
    # "3. Pers pallade äpplen - 4 Riksdaler",
    # "4. Kalles Kristall Godis - 9 Riksdaler"]
    
    for item in shopItems:
        slowtxt(item)        

    slowtxt("""
    - Jag rekomenderar starkt kristallgodiset, asså tro mig Britta blir helt galen över dem!
    - Äpplena är inte så dumma heller om du vill vara på hennes snälla sida.""")        
    
    print(f"        Just nu har du {data.cash} riksdaler")
    slowtxt("       - Så vad blir det?")
            
    while True:
        shopChoice = input("\n-->")
        if check(shopChoice, ["kapten", "konrads" ,"krut","1"]):
            data.cash = data.cash - 7
            addinv("Kapten Konrads Krut")
            slowtxt("       Något mer?")
               

        elif check(shopChoice, ["2", "kalles", "kristall", "godis"]):
            data.cash = data.cash - 5
            addinv("Kalles Kristall Godis")
            slowtxt("       Något mer?")

        
        elif check(input("-->"), ["n","nej","nope","allt"]):
            break
    slowtxt("       Vill du kasta tärning eller gå tillbaka till korridoren")

    ragnarChoice = input("-->")     
    if check(ragnarChoice,["dra","ut","sticka","tillbaka","klassrum", "korridor"]):
        slowtxt("       - Kom gärna igen")
        slowtxt("       Du återvänder till korridoren, vart går du nu?")
        return None
            
    elif check(ragnarChoice, ["spela", "tärningar"]):
        ragnarDices()


### ----------------------------- NPC ------------------------- ###







def britta():

    if data.period == 1:
        
            if npc.brittaHaveMetClassroom == False:
                slowtxt(f"""
        - Hörrudu, ska inte du jobba eller? 
        Du vet ju att elever som inte jobbar får F. 
        Tillbaks till din bänk med dig, eller vänta.
        Förresten, har du något sånt där blått kristallgodis eller?""")
                npc.brittaHaveMetClassroom = True
            else:
                slowtxt(f"      Har du nåt kristallgodis nu eller?")

            while True:
                brittaChoice = input()
                if check(brittaChoice, ["ja"]) and extractItem("Kalles Kristall Godis"):
                    slowtxt(f"""
        - "Ge det till mig!" Britta rycker ut godiset ur din ficka innan du hinner reagera.
        - "Okej klassen, jag kommer strax tilbaka, jobba flitigt nu!" Säger Britta, sen lämnar hon klassrummet.""")
                    npc.brittasOverwatch = False
                    npc.brittaCrystal = True
                    return
                elif check(brittaChoice, ["ja"]) and not extractItem("Kalles Kristall Godis"):
                    slowtxt("    - Nu ljuger du ju bara för mig! Tillbaks till bänken och jobba!")
                    return
                elif check(brittaChoice, ["nej", "no"]):
                    slowtxt(f"""
         - Nähä? Vad gör du här då, tillbaks till din bänk innan jag tar fram tofflan!""")  
                    return        

    if data.period == 2:
        if npc.brittaCrystal == True:
            slowtxt(""" 
        - Hallå elever får inte lämna matsalen under lunchen!
        Fast du råkar inte veta var det finns mer kristallgodis eller? 
        Om du gör det kan du ju gå och hämta det till Britta. Vill du ut?"""
            
            )
            brittaChoice = input("-->")
            if check(brittaChoice, ["ja"]):
                slowtxt("""
         - Om du inte kommer tillbaka med något godis blir det tofflan! Och säg inte om det här till någon!""")
                npc.brittaLetOut = True

                slowtxt(""" 
        - Nähä, bort med dig då, gå och ät din soppa med de andra snorungarna.""")
                
        else: 
            slowtxt(""" 
        - Hallå elever får inte lämna matsalen under lunchen. Fast vänta, 
        har du något blått kristallgodis eller?""")
            brittaChoice = input("-->")
            if check(brittaChoice, ["ja"]) and extractItem("Kalles Kristall Godis"):
                slowtxt(""" 
        - Okej klassen, Jag kommer strax tillbaka. 
        Bete er nu och ät er soppa! Det finns mycket nyttigt i den! 
        Säger Britta och lämnar matsalen""")
                npc.brittasOverwatch = False
            else:
                slowtxt(""" 
         - Nähä, bort med dig då, gå och ät din soppa med de andra snorungarna.""")
    if data.period == 3:
        slowtxt("       Nej jag kommer inte leka med dig, gå och skaffa lite vänner istället.")


def gunn_marie():
    slowtxt("       - Varför pratar du med mig? Jag har en pojkvän.")

def ragnarsDesk():
    if npc.brittasOverwatch is True:    
        
        slowtxt(f"""
        Du går för att öppna Ragnars bänk, kanske finns något intressant där inne?  
        "Hörrudu! Det där är väl ändå inte din bänk eller? 
        Tillbaks din din plats eller så skickar jag dig till rektorn!\" 
        hör du Britta säga. Jag får testa igen när hon är distraherad. 
        Bäst om jag undviker göra henne arg.""")
        npc.brittaAnger = npc.brittaAnger + 1

    else:

        slowtxt(f"""
        Du går för att öppna Ragnars bänk, det kanske finns något intressant där inne? 
        Du öppnar bänken och det ser ut som ett totalt bombnedslag, saker överallt. 
        Du fortsätter rota runt lite tills du ser något glansigt. Vågar du kolla?""")

        if check(input("-->"), ["ja", "japp", "inspektera", "kolla", "kika" ]):
        
            slowtxt(f"""
        Du tar upp objektet. Det verkar vara någon sorts kniv täkt med någon röd juice
        förmodligen från en frukt.
        Du lägger den snabbt i fickan och stänger Ragnars bänk innan Britta ser något.""")
            addinv("Ragnars kniv")

        else:
            slowtxt(f"""    Du lägger tillbacka objektet och stänger Ragnars bänk innan Britta ser något""")

            

def food():
    slowtxt(f"""
    Du går fram till mattanten och visar upp din skål.
    -Här får du lite soppa, det finns alltid mer om du vill ha!
    Du kollar ner i skålen och ser en grå soppa som ser giftig ut.
    """)
    addinv("Skolans Soppa")
    

def bin():

        if npc.binHaveSearched == False and npc.brittasOverwatch == False:
            slowtxt("       Du rotar igenom sopptunnan och hittar en gammal smörkniv.")
            addinv("Rostig Brödkniv")
            npc.binHaveSearched = True
        elif npc.binHaveSearched == False and npc.brittasOverwatch == True:
            slowtxt(f"""
        - Hallå {data.name}! Inte rota i sopptunnan. 
        Jag vill inte behöva förklara för dina förälderar varför du ser hemlös ut när de hämtar dig.
        För mitt eget bästa borde jag inte göra henne arg.""")
            npc.brittaAnger = npc.brittaAnger + 1
        elif npc.binHaveSearched == True:
            slowtxt("       Du har redan rotat igenom sopptunnan. Det finns inget mer där.")