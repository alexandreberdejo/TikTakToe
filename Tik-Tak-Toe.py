def afficher_plateau(board):
    print("\n")
    for i in range(0,9,3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i <6:
            print("--+---+--")
    print()

def victoire(board,s):
    combinaisons=[[0,1,2],[3,4,5],[6,7,8],
                [0,3,6], [1,4,7], [2,5,8],
                [0,4,8], [2,4,6]
]

    for i in combinaisons:
        if board[i[0]]==board[i[1]] == board[i[2]] == s:
            return True
        return False

import random

def ia_aleatoire(board):
    cases_vides = [i for i in range(9) if board[i] == " "]
    return random.choice(cases_vides)

# Les autres fonctions sont identiques à la version 1

def ia_niveau_2(board, signe):
    adv = "O" if signe == "X" else "X"
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    # Tentative de gagner
    for a,b,c in combos:
        if board[a]==signe and board[b]==signe and board[c]==" ": return c
        if board[a]==signe and board[c]==signe and board[b]==" ": return b
        if board[b]==signe and board[c]==signe and board[a]==" ": return a

    # Bloquer
    for a,b,c in combos:
        if board[a]==adv and board[b]==adv and board[c]==" ": return c
        if board[a]==adv and board[c]==adv and board[b]==" ": return b
        if board[b]==adv and board[c]==adv and board[a]==" ": return a

    # Sinon hasard
    return random.choice([i for i in range(9) if board[i]==" "])


def jeu():
    mode = input("1: 2 joueurs | 2: Contre IA : ")
    board = [" "] * 9
    joueur = "X"

    while True:
        afficher_plateau(board)

        if mode == "2" and joueur == "O":
            choix = ia_niveau_2(board, "O")
        else:
            choix = int(input(f"Joueur {joueur} choisissez (0-8) : "))

        if board[choix] != " ":
            print("Case occupée")
            continue

        board[choix] = joueur

        if victoire(board, joueur):
            afficher_plateau(board)
            print("Victoire de", joueur)
            break

        joueur = "O" if joueur == "X" else "X"
jeu()

