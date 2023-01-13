import math
import random
import moduler
import os
import moduler as m
from moduler import slowtxt as print_
from time import sleep


#input till funktionerna, följer mallen tid, period , pengar
data = []
name = ""
cash = 10
missinput = 0
# period refers to one of the 3 time periods during the day, morning, lunch and afternoon. 
# When time runs out during 1 period you move to the next one and your time resets back to 7.
# The game runs in cycles with each one having a limited and exclusive set of things to do.
time = 6
period = 1 

data = [time, period, cash]

#print_ ersätter print i vår kod
#print_ är print fast långsammare


# Main menu system, allows for instructions and //settings//

moduler.setSpeed(0.001)

os.system("color 2")
print_
print("""
 
██████╗░░█████╗░░██████╗░██╗░██████╗███████╗████████╗
██╔══██╗██╔══██╗██╔════╝░██║██╔════╝██╔════╝╚══██╔══╝
██║░░██║███████║██║░░██╗░██║╚█████╗░█████╗░░░░░██║░░░
██║░░██║██╔══██║██║░░╚██╗██║░╚═══██╗██╔══╝░░░░░██║░░░
██████╔╝██║░░██║╚██████╔╝██║██████╔╝███████╗░░░██║░░░
╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░   
""")
print("         Gjord av Vidar Borg och Oliver Granäng")
print_("""
---------------------------------------------------------------------------
""")

sleep(1)

print("                         Välkommen\n")

# Main menu which allows selection between options, instructions and starting the game
print_("\nOm det är första gången du spelar rekomenderas att läsa instruktionerna.\n")

nuts = ["               1.Starta spelet", 
        "               2.Instruktioner",
        "               3.Inställningar"]
for deez in nuts:
    print_(deez)

menuChoice = input("\n-->")

while True:
    if menuChoice == "1":
        break

    elif menuChoice == "2":
        print_("""
        Spelet utspelar sig en vanlig dag på ditt dagis där du har ett matteprov som du inte har studerat till.
        Du måste hitta något sätt att klara provet för du vet att din mamma kommer bli väldigt besviken på dig annars.
        I skolan kan du välja fritt vart du vill gå och du kan exempelvis plocka upp saker du hittar på marken eller prata med personer
        för att hjälpa dig på din resa att slingra dig ur ett F på matteprovet.

        För att röra dig runt skriv simpla kommandon så som gå höger, gå rakt fram, gå till klassrummet, klassrum, prata med Gunnbritt eller liknande.
        
        """)
        print_("Är du redo att börja ditt äventyr? y/n")
        ready = input("-->")
        if ready == "y":
            break

    # Settings
    elif menuChoice == "3":
        print_("Vilken texthastighet vill du ha? - obs endast tal inga bokstäver")

        txtSpeed = input("-->")
        txtSpeed = float(txtSpeed)
        moduler.setSpeed(txtSpeed)
        break



# The check function requieres an input following: choice, accepted strings
# moduler.check returns true if one of the items in list is included in the user input

# -- GAMESTART --
#The game/ the room "korridor" is the interconnecting room between all other rooms and acts as a hub
m.clear()
print_("\nDu rusar in i korridoren med endast 3 minuter kvar tills lektionen börjar\n Rakt fram ligger klassrummet och till vänster ligger toaletterna där du hör någon böka runt. Till höger om dig ligger matsalen och dörren bakom dig leder tillbaks till skolgården. \nVart går du?")

while True:
    data = [time,period,cash]
    choice =  input("-->") 
    

    # Controls the time and resets it to 7 when a new period begins
    if time == 0:
        period = period + 1
        time = time + 7
    #After the 3rd period you move into the final event instead of a 4th period. 
    if period > 3:
        moduler.finalboss()
            
    if period == 2:
        pass
   
    
    if moduler.check(choice, ["klassrum", "raktfram", "klassrummet", "frammåt"]):
        moduler.classroom(time, name)
    
    #Bathroom
    elif moduler.check(choice, []):
            moduler.bathroom(data)
        
    #Bamba
    elif moduler.check(choice, []):
            if period < 2:
                print_("Förvånade så är matsalen bara öppen när det är MAT, kom tillbaka senare")
            else:
                moduler.food(data)
   
    elif moduler.check(choice, []):
        # Bernard is the Janitor. Name can change later.
        moduler.BernardCorridor(data)
        
    elif moduler.check(choice, []):
        pass

    elif moduler.check(choice, ["inventory", "inv"]):
        moduler.inventory(data)
    
    elif m.check(choice,["exit","end", "quit","stäng av"]):
        print_("Hej då")
        os.system("EXIT")
        
    
    else:
        if missinput == 4:
            missinput = 0
            print_("Kom ihåg att använda dig av klara korta instruktioner så som till exempel: gå höger, kolla runt, gå klassrum eller prata med Gunnar.")
        
        else:
            missinput = missinput + 1
