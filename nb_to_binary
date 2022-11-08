choix = "Z"

while choix != "Q" and choix != "q":
    print("Conversion entier vers binaire ........ 1")
    print("Conversion binaire vers entier ........ 2")
    print("quitter ............................... Q")
    choix = input("votre choix ........................... ?")
    if choix == "1":
        binaire = ""
        nb = int(input("Entrez un entier : "))
        while nb != 0:
            binaire = str(nb % 2) + binaire
            nb = nb // 2
        print(f"La conversion en binaire de {binaire} ")
    else:
        if choix == "2":
            nb = 0
            k = 0
            binaire = input("Veillez entrez un nombre en binaire : ")
            while len(binaire) > 0 :
                nb += int(binaire[len(binaire)-1:]) * math.pow(2,k)
                binaire = binaire[:len(binaire)-1]
                k += 1
            print(f"La conversion en base 10 = {nb}")
