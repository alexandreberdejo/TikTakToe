import random


# IA NIVEAU 1 : Aléatoire

def ia_niveau_1(board, signe):
    cases_vides = [i for i in range(9) if board[i] == " "]
    return random.choice(cases_vides)



# IA NIVEAU 2 : Gagner / Bloquer 

def ia_niveau_2(board, signe):
    adversaire = "O" if signe == "X" else "X"

    combinaisons = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]


    for combo in combinaisons:
        a, b, c = combo
        if board[a] == signe and board[b] == signe and board[c] == " ":
            return c
        if board[a] == signe and board[c] == signe and board[b] == " ":
            return b
        if board[b] == signe and board[c] == signe and board[a] == " ":
            return a

    # 2) Bloquer l’adversaire
    for combo in combinaisons:
        a, b, c = combo
        if board[a] == adversaire and board[b] == adversaire and board[c] == " ":
            return c
        if board[a] == adversaire and board[c] == adversaire and board[b] == " ":
            return b
        if board[b] == adversaire and board[c] == adversaire and board[a] == " ":
            return a

    # 3) Jouer au hasard
    cases_vides = []
    for i in range(9):
        if board[i] == " ":
            cases_vides.append(i)

    return random.choice(cases_vides)



# IA NIVEAU 3 : Stratégique

def ia_niveau_3(board, signe):
    if board[4] == " ":
        return 4

    coins = [i for i in [0, 2, 6, 8] if board[i] == " "]
    if coins:
        return random.choice(coins)

    bords = [i for i in [1, 3, 5, 7] if board[i] == " "]
    if bords:
        return random.choice(bords)

    return ia_niveau_1(board, signe)


# ---------------------------------
# Choix IA selon niveau
# ---------------------------------
def ordinateur(board, signe, niveau):
    if niveau == 1:
        return ia_niveau_1(board, signe)
    if niveau == 2:
        return ia_niveau_2(board, signe)
    if niveau == 3:
        return ia_niveau_3(board, signe)
    return ia_niveau_1(board, signe)


# 
# Affichage du plateau

def afficher_plateau(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")



# Vérifier la victoire

def victoire(board, s):
    combinaisons = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combinaisons:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == s:
            return True
    return False


# 
# Match nul

def match_nul(board):
    return " " not in board



# Tour du joueur

def tour_joueur(board, signe):
    while True:
        try:
            choix = int(input(f"Joueur {signe}, choisissez une case (0-8) : "))
            if choix < 0 or choix > 8:
                print("Veuillez choisir un nombre entre 0 et 8.")
            elif board[choix] != " ":
                print("Cette case est déjà prise.")
            else:
                board[choix] = signe 
                break
        except:
            print("Entrée invalide. Essayez encore.")


# Tour ordinateur

def tour_ordinateur(board, signe, niveau):
    print(f"L'ordinateur ({signe}) réfléchit (IA niveau {niveau})...")
    choix = ordinateur(board, signe, niveau)
    board[choix] = signe
    print(f"L’ordinateur joue en case {choix}.")


# JEU PRINCIPAL

def jeu():
    print(" TIC TAC TOE ")

    mode = input("Mode de jeu : (1) 2 joueurs  |  (2) contre l'ordinateur : ")

    niveau_ai = 1
    if mode == "2":
        niveau_ai = int(input("Choisissez niveau IA : 1 (facile), 2 (moyen), 3 (difficile) : "))

    board = [" "] * 9
    joueur = "X"

    while True:
        afficher_plateau(board)

        if mode == "2" and joueur == "O":
            tour_ordinateur(board, joueur, niveau_ai)
        else:
            tour_joueur(board, joueur)

        if victoire(board, joueur):
            afficher_plateau(board)
            print(f"Le joueur {joueur} a gagné !")
            break

        if match_nul(board):
            afficher_plateau(board)
            print("Match nul !")
            break

        joueur = "O" if joueur == "X" else "X"


# Lancer le jeu
jeu()