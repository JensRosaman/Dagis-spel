import random as rand


def slots(para):
    "Kastar två tärningar och ger"
    resultat = []
    tal = [1 , 2 , 3 , 4, 5, 6]
   

    resultat.append(rand.choice(tal))
    resultat.append(rand.choice(tal))
    resultat.append(rand.choice(tal))
    
    print(resultat)

    if len(set(resultat)) == 1:
        totcreds = (para[0] * 2) + para[1]
        para[0] = para[0] * 2
        print("du vann ", para[0])
        return totcreds
    
    else:
        totcreds = (para[0]) - (para[1])
        return totcreds


def dices():
    dieNumber = [1 , 2 , 3 , 4, 5, 6]
    result = []
    diceBet = input("-->")
    
    result.append(rand.choice(dieNumber))
    result.append(rand.choice(dieNumber))
    print(result)

    if len(set(result)) == 1:
        diceBet = int(diceBet) * 2
        

        print("Du vann")



dices()
