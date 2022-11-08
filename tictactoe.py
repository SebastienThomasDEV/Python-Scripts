ligne1 = [0, 0, 0]
ligne2 = [0, 0, 0]
ligne3 = [0, 0, 0]
ligne123 = [ligne1, ligne2, ligne3]
turn = 1
fin = True
win = 0  # =0 quand personne n'a gagné,=1 quand le joueur 1 a gagné,=2 quand le joueur 2 a gagné.
print('Bienvenue dans Tic-Tac-Toe ')
joueur1 = input("Entrez nom du joueur 1")
joueur2 = input("Entrez nom du joueur 2")


def affichage():
    print("___1___2___3___")
    print("1| {0} | {1} | {2} |".format(ligne1[0], ligne1[1], ligne1[2]))
    print("_______________")
    print("2| {0} | {1} | {2} |".format(ligne2[0], ligne2[1], ligne2[2]))
    print("_______________")
    print("3| {0} | {1} | {2} |".format(ligne3[0], ligne3[1], ligne3[2]))

def analyse():
	for i in range(3):
      global fin
      global win
      if ligne1[i] == ligne2[i] == ligne3[i] == 1: # analyse si les lignes ont été remplies par un joueur
            affichage()
            win = 1
            fin = False
        if ligne1[i] == ligne2[i] == ligne3[i] == 2:
            affichage()
            win=2
            fin = False
      for i, j, k in ligne1, ligne2, ligne3:  # analyse si les colonnes ont été remplies par un joueur
        if i == j == k == 1:
        	  affichage()
            win=1
            fin = False
        if i == j == k == 2:
          	affichage()
            win=2
            fin = False
      if ligne1[0] == ligne2[1] == ligne3[2]:#diagonale descendante
      	if ligne1[0]==1:
        	win=1
        	fin=False
      	elif ligne1[0]==2:
        	win=2
        	fin=False
	if ligne1[2] == ligne2[1] == ligne3[0]:#diagonale ascendante
      	if ligne1[2]==1:
        	win=1
        	fin=False
      	elif ligne1[2]==2:
        	win=2
        	fin=False
  
  
while fin:
    if turn == 1:
        affichage()
        choixligne = int(input(f"C'est le tour du {joueur1} Entrez la ligne souhaité"))
        choixcolonne = int(input(f"C'est le tour du {joueur1} Entrez le numero de colonne souhaité"))
        ligne123[choixligne - 1][choixcolonne - 1] = 1
        turn = 0
        analyse()
    if turn == 2:
        affichage()
        turn = 1
        choixligne2 = int(input(f"C'est le tour du {joueur2} Entrez la ligne souhaité"))
        choixcolonne2 = int(input(f"C'est le tour du {joueur2} Entrez le numero de colonne souhaité"))
        ligne123[choixligne2 - 1][choixcolonne2 - 1] = 2
        analyse()
    if turn == 0:
        turn = 2

print(f"le joueur {win} a gagné")
