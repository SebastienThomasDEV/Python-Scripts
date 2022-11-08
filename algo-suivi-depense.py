import os
from pathlib import Path
import sys


def afficheracceuil():
    print("\n")
    print("       | 1) créer un suivi       |")
    print("       | 2) charger un suivi     |")
    print("       | 3) quitter le programme |\n")


def creerunsuivi():
    try:
        suivi = input("veuillez entrez un nom de suivi :")
        if suivi == "":
            continuer = True
            while continuer:
                suivi = input("Entrez une nom de suivi valide: ")
                if suivi != "":
                    continuer = False
        print(f"Vous avez créer : {suivi} ")
        solde = input("quel est votre solde : ")

        if solde == "":
            continuer = True
            while continuer:
                try:
                    solde = int(input("Entrez un solde valide: "))
                except:
                    pass
                if solde != "":
                    continuer = False

        print(f"Votre solde actuel : {solde} $ ")
        login = os.getlogin()
        chemindesuivi = "C:\\Users\\" + login + "\\Comptapython\\" + suivi
        fichier = open(chemindesuivi, 'wt')
        fichier.write("solde:" + solde)

        nomdecategorie = input("veuillez entrez une catégorie :")
        if nomdecategorie == "":
            continuer = True
            while continuer:
                nomdecategorie = input("Entrez une nouvelle catégorie valide: ")
                if nomdecategorie != "":
                    continuer = False
        fichier.write(f"@{nomdecategorie}:")
        for i in range(1, 99):
            categorie = input("veuillez entrez une catégorie (pour arreter ne rien entrer): ")
            if categorie == "":
                break
            fichier.write(f"@{categorie}:")

        fichier.close()
        print(f"\nVous avez créer le suivi {suivi} d'un solde de {solde}\n")
    except:
        print('\n')
        pass


def chargerunsuivi():  # récupère le contenu d'un suivi sous forme de liste avec les infos à l'interieur
    global suivichoisi
    print("\n")
    myDirectory = "C:\\Users\\" + os.getlogin() + "\\Comptapython"
    p = Path(myDirectory)
    continuer = True
    while continuer:

        for x in os.scandir(p):
            y = str(x)
            print(y[11:-2])
        print("\n")

        try:
            suivichoisi = input("selectionner le suivi dans la liste : ")
            print(f"Vous avez choisi : {suivichoisi}\n ")
            fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi,
                                'r')  # ouvre le fichier
            readline = fichiersuivi.readline()  # stock dans readline la chaine de caractère du fichier
            suiviliste = readline.split('@')  # créer une liste avec les informations du suivi
            fichiersuivi.close()
            continuer = False
        except:
            continuer = True
            print("Choisissez une catégorie valide\n")

    return suiviliste


def choixacceuil():
    continuer = True
    while continuer:
        try:
            a = int(input("Quel est votre choix ? :"))
            continuer = False
        except:
            print("Entrez un choix valide :")

    if a == 1:
        print(100 * "\n")
        print("Vous avez choisi créer un suivi")
        creerunsuivi()
    if a == 2:
        print(100 * "\n")
        print("Vous avez choisi charger un suivi")
        affichersuivi(chargerunsuivi())
        menusuivi()
    if a == 3:
        print(100 * "\n")
        print("Vous quittez le programme")
        sys.exit()


def makeBaseRep():  # Créer les fichiers/répertoire de base du programme

    try:
        login = os.getlogin()
        chemindeBase = "C:\\Users\\" + login + "\\Comptapython"
        os.mkdir(chemindeBase)  # créer un fichier compta python dan C:\Users\NomUtilisateurConnecté\Comptapython
        cheminSuivi = "C:\\Users\\" + login + "\\Comptapython\\FichierSuivi"  # créer un fichier compta python dan C:\Users\NomUtilisateurConnecté\Comptapython\FichierSuivi
    except:
        print("Fichier Comptapython déjà existant")


def affichersuivi(suiviliste):
    global printsolde
    solde = suiviliste[0][6:]
    liste = suiviliste[1:]
    print(100 * "\n")
    print("\nBonjour {0}, Votre solde de base était de {1} €\n".format(os.getlogin(), solde))
    print("Voici la liste de vos dépenses: ")
    soldeactuel = float(solde)
    for i in liste:  # itère dans la chaine de caractère récupéré les informations du suivi
        categorie = ""
        condition = True
        compteur = 0
        while condition:
            if i[compteur] == ":":
                condition = False
            categorie += i[compteur]
            compteur += 1
        print(categorie)
        listenombre = i[compteur:].split(',')  # créer une liste des valeurs entrée
        print(listenombre)
        if len(listenombre) > 1:
            listenombre = [float(nb) for nb in listenombre]  # créer une compréhension de liste
            sommesdesnb = sum(listenombre)
            print(f"- {sommesdesnb} €")
            soldeactuel = soldeactuel - sommesdesnb
    printsolde = soldeactuel


def menusuivi():
    print(f"Votre solde actuel est de {printsolde} €\n")
    print("| 1) ajouter une catégorie de dépense      |")
    print("| 2) ajouter une dépense à une cartégorie  |")
    print("| 3) supprimer une catégorie               |")
    print("| 4) supprimer une dépense a une catégorie |")
    print("| 5) revenir à l'écran d'acceuil           |")
    choix = input("\nEntrez votre choix: ")
    if choix == '1':
        print(100 * "\n")
        ajoutercategorie()
    elif choix == '2':
        print(100 * "\n")
        ajouterdepense()
    elif choix == '3':
        print(100 * "\n")
        suprimmercategorie()
    elif choix == '4':
        print(100 * "\n")
        suprimmerdepense()
    elif choix == '5':
        print(100 * "\n")
        print("Retour au menu")
    else:
        print("\n" * 100)
        print("Entrez un choix valide")
        menusuivi()


def ajoutercategorie():
    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'r')  # ouvre le fichier
    readline = fichiersuivi.readline()  # stock dans readline la chaine de caractère du fichier
    fichiersuivi.close()
    chainefichier = readline
    print(100 * "\n")
    nomdecategorie = input("Entrez une nouvelle catégorie: ")
    if nomdecategorie == "":
        continuer = True
        while continuer:
            nomdecategorie = input("Entrez une nouvelle catégorie valide: ")
            if nomdecategorie != "":
                continuer = False
    chainefichier += '@' + nomdecategorie + ':'
    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'w')
    fichiersuivi.write(chainefichier)
    fichiersuivi.close()
    pass


def ajouterdepense():
    a = True
    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'r')  # ouvre le fichier
    readline = fichiersuivi.readline()  # stock dans readline la chaine de caractère du fichier
    suiviliste = readline.split('@')
    ctg = suiviliste[1:]
    fichiersuivi.close()
    print(100 * "\n")
    print(ctg)
    print("\n")
    try:
        continuer = True
        while continuer:
            choixctg = input("Entrez la catégorie choisie : ")
            if (choixctg + ':') in ctg:
                continuer = False
            else:
                print("catégorie invalide ")
    except:
        pass
    liste = suiviliste
    length = len(choixctg) + 1
    compteur = 0
    liste2 = []
    print(100 * "\n")

    print(ctg)

    while a:
        continuer2 = True
        while continuer2:
            try:
                valeur = input(f"Entrez une nouvelle dépense à la catégorie {choixctg} : ")
                if valeur == '':
                    continuer2 = False
                else:
                    valeur = str(int(valeur))
                    continuer2 = False

            except:
                print("Entrez une dépense valide!")
        if valeur == "":
            a = False
        if valeur != "" and compteur > 0:
            for i in liste:
                if i.find(choixctg) == 0:
                    liste[liste.index(i)] += "," + str(valeur)
                    print(100 * "\n")
                    print(f"\nVous avez ajouté {valeur} € à votre catégorie {choixctg}.\n")
                    liste2.append(valeur)
        if valeur != "" and compteur == 0:
            compteur += 1
            for i in liste:
                lengthi = len(i)
                if i.find(choixctg) == 0:
                    if i.find(choixctg) == 0 and length < lengthi:
                        liste[liste.index(i)] += "," + str(valeur)
                        print(100 * "\n")
                        print(f"\nVous avez ajouté {valeur} € à votre catégorie {choixctg}.\n")
                        liste2.append(valeur)
                        break
                    liste[liste.index(i)] += str(valeur)
                    print(100 * "\n")
                    print(f"\nVous avez ajouté {valeur} € à votre catégorie {choixctg}.\n")
                    liste2.append(valeur)
    nliste = "@".join(suiviliste)
    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'w')
    fichiersuivi.write(nliste)
    fichiersuivi.close()
    listenombre = [float(nb) for nb in liste2]
    sommeliste = sum(listenombre)
    chaineliste = ",".join(liste2)
    print(100 * "\n")
    print(f"Vous avez ajoutez {chaineliste} € (pour un total de -{sommeliste} €) dans la catégorie {choixctg} \n")
    print("\n")


def suprimmercategorie():
    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'r')  # ouvre le fichier
    readline = fichiersuivi.readline()  # stock dans readline la chaine de caractère du fichier
    readline = readline.split("@")
    fichiersuivi.close()
    t = readline[0]
    u = readline[1:]
    print(100 * "\n")
    a = input("selectionner la catagorie a supprimer : ")
    print(f"Vous avez selectionner : {a}")
    for i in u:  # sélectionne dans la liste
        if i.find(a) == 0:
            placecategorie = u.index(i)
            del u[placecategorie]
    nliste = "".join(t) + "@" + "@".join(u)
    print(u)

    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'w')
    fichiersuivi.write(nliste)
    fichiersuivi.close()
    print(f"\nLa catégorie {a} a bien été supprimer")

    pass


def suprimmerdepense():
    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'r')  # ouvre le fichier
    readline = fichiersuivi.readline()  # stock dans readline la chaine de caractère du fichier
    fichiersuivi.close()
    chainefichier = readline
    chainefichier = chainefichier.split('@')
    listefichiersolde = chainefichier[0]
    listefichier = chainefichier[1:]
    print(100 * "\n")
    print(listefichier)
    print("\n")
    categoriesupp = input("Dans quelle catégorie souhaitez vous supprimer une dépense ?: ")
    depensesupp = input("Indiquer la dépense à supprimer: ")

    for i in listefichier:  # sélectionne dans la liste le la catégorie à supprimer l158-l159
        if i.find(categoriesupp) == 0:
            placecategorie = listefichier.index(i)  # récupère le numéro de la place de la catégorie
            substr = i[len(categoriesupp) + 1:]  # récupère les dépense sans le nom de catégorie
            listedepense = substr.split(',')  # créer une liste avec les dépense
            listedepense.remove(depensesupp)  # supprime l'élément sélectionné

    categorieetdepense = categoriesupp + ':' + ','.join(listedepense)  # sa donne bambam:50,70
    del listefichier[placecategorie]
    listefichier.insert(placecategorie, categorieetdepense)
    listefichier = [listefichiersolde] + listefichier  # rajoute le solde dans la liste
    strfichier = '@'.join(listefichier)
    fichiersuivi = open("C:\\Users\\" + os.getlogin() + "\\Comptapython\\" + suivichoisi, 'w')
    fichiersuivi.write(strfichier)
    fichiersuivi.close()
    print(100 * "\n")
    print(f"\nVous avez bien supprimé la dépense de {depensesupp} € dans la catégorie {categoriesupp}\n")


def ecraserfichier():
    pass
