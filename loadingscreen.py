from time import sleep as sleep
import random as ra
import os



def loadScr(antal):
    
    tips = ["Visste du att spelet är nästan till fullo kopierat från det ritkiga spelet 'Kindergarten'",
        "Prata med så många du kan så att du kan planera din resa bättre",
        "Spela om spelet flera gånger för att få de tre olika slutet",
        "Visste du att 90% av alla tips är onödiga",
        "Den här laddnings skärmen är artificiel och helt onödig"]
    
    for i in range(antal):
        os.system("cls")
        print("""
    ██████╗░░█████╗░░██████╗░██╗░██████╗███████╗████████╗
    ██╔══██╗██╔══██╗██╔════╝░██║██╔════╝██╔════╝╚══██╔══╝
    ██║░░██║███████║██║░░██╗░██║╚█████╗░█████╗░░░░░██║░░░
    ██║░░██║██╔══██║██║░░╚██╗██║░╚═══██╗██╔══╝░░░░░██║░░░
    ██████╔╝██║░░██║╚██████╔╝██║██████╔╝███████╗░░░██║░░░
    ╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░
    """)
        print("                      LADDAR")
        
        # Chooses a random tip and displays it slowly
        print(ra.choice(tips))
        sleep(1.5)



loadScr(3)
