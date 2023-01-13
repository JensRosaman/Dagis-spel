import random as rand


def slots(para):
    "Kastar två tärningar och ger"
    #lista följer mallen [creds , bet]
    resultat = []
    tal = [1 , 2 , 3 , 4, 5, 6]
    if input("Vill du muta personalen? y/n") == "y":
        muta = input("Hur mycket?\n-> 20\n-> 30 ")
        
        if muta == "20" or muta == "30":
            muta = int(muta)
            para[1] = para[1] - muta
        
            while muta >= 1:
                tal.append(5)
                muta = muta - 10

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


para = []
with open("save.txt", "r") as txt:
    creds = txt.read()
    txt.close()
creds = int(creds)
print("Du har just nu ", credsl)
para.append(creds)
para.append(int(float(input("hur mkt bettar du"))))

creds = slots(para)
creds = str(creds)
with open("save.txt", "w") as txt:
    txt.write(creds)
    txt.close()
print("Du har nu ", creds, "credits")

   



