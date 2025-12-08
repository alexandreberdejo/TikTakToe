import random



# IA NIVEAU 1 : ALÉATOIRE

def ia_niveau_1(board, signe):
    cases_vides = [i for i in range(9) if board[i] == " "]
    return random.choice(cases_vides)


# IA NIVEAU 2 : GAGNER / BLOQUER
def ia_niveau_2(board, signe):
    adversaire = "O" if signe == "X" else "X"

    combinaisons = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    # 1) Tenter de gagner
    for a, b, c in combinaisons:
        if board[a] == board[b] == signe and board[c] == " ":
            return c
        if board[a] == board[c] == signe and board[b] == " ":
            return b
        if board[b] == board[c] == signe and board[a] == " ":
            return a

    # 2) Bloquer l’adversaire
    for a, b, c in combinaisons:
        if board[a] == board[b] == adversaire and board[c] == " ":
            return c
        if board[a] == board[c] == adversaire and board[b] == " ":
            return b
        if board[b] == board[c] == adversaire and board[a] == " ":
            return a

    # 3) Sinon jouer au hasard
    cases_vides = [i for i in range(9) if board[i] == " "]
    return random.choice(cases_vides)


# IA NIVEAU 3 : ia_minmax (IMBATTABLE)
def ia_minmax(board, depth, is_maximizing, signe, adversaire):
    if victoire(board, signe):
        return 10 - depth
    if victoire(board, adversaire):
        return depth - 10
    if match_nul(board):
        return 0

    if is_maximizing:
        meilleur_score = -9999
        for i in range(9):
            if board[i] == " ":
                board[i] = signe
                score = ia_minmax(board, depth+1, False, signe, adversaire)
                board[i] = " "
                meilleur_score = max(meilleur_score, score)
        return meilleur_score

    else:
        meilleur_score = 9999
        for i in range(9):
            if board[i] == " ":
                board[i] = adversaire
                score = ia_minmax(board, depth+1, True, signe, adversaire)
                board[i] = " "
                meilleur_score = min(meilleur_score, score)
        return meilleur_score


def ia_niveau_3(board, signe):
    adversaire = "O" if signe == "X" else "X"
    meilleur_score = -9999
    meilleur_coup = None

    for i in range(9):
        if board[i] == " ":
            board[i] = signe
            score = ia_minmax(board, 0, False, signe, adversaire)
            board[i] = " "
            if score > meilleur_score:
                meilleur_score = score
                meilleur_coup = i

    return meilleur_coup

# Fonction de sélection IA

def ordinateur(board, signe, niveau):
    if niveau == 1:
        return ia_niveau_1(board, signe)
    if niveau == 2:
        return ia_niveau_2(board, signe)
    if niveau == 3:
        return ia_niveau_3(board, signe)
    return ia_niveau_1(board, signe)



# AFFICHER LE PLATEAU

def afficher_plateau(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")


# CONDITIONS DE VICTOIRE
def victoire(board, s):
    combinaisons = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for a, b, c in combinaisons:
        if board[a] == board[b] == board[c] == s:
            return True
    return False


def match_nul(board):
    return " " not in board


# TOUR JOUEUR HUMAIN
def tour_joueur(board, signe):
    while True:
        try:
            choix = int(input(f"Joueur {signe}, choisissez une case (0-8) : "))
            if choix < 0 or choix > 8:
                print("Veuillez choisir un nombre entre 0 et 8.")
            elif board[choix] != " ":
                print("Case déjà prise.")
            else:
                board[choix] = signe
                break
        except:
            print("Entrée invalide.")


# TOUR ORDINATEUR
def tour_ordinateur(board, signe, niveau):
    print(f"L’ordinateur ({signe}) réfléchit (niveau {niveau})...")
    choix = ordinateur(board, signe, niveau)
    board[choix] = signe
    print(f"L’ordinateur joue en case {choix}.")


# MENU PRINCIPAL
def menu():
    print("MENU TIC TAC TOE ")
    print("1 - Joueur vs Joueur")
    print("2 - Joueur vs Ordinateur")

    choix = input("Choisissez un mode : ")

    if choix == "1":
        return "PVP", None     # pas de niveau IA
    elif choix == "2":
        niveau = int(input("Choisissez niveau IA : 1 (facile) | 2 (moyen) | 3 (difficile) : "))
        return "IA", niveau
    else:
        print("Choix invalide. Par défaut : Joueur vs Joueur.")
        return "PVP", None


# JEU PRINCIPAL
def jeu():
    mode, niveau_ai = menu()

    board = [" "] * 9
    joueur = "X"

    while True:
        afficher_plateau(board)

        if mode == "IA" and joueur == "O":  
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
