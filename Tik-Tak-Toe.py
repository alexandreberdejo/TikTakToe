def afficher_plateau(board):
    print("\n")
    for i in range(0,9,3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i <6:
            print("--+---+--")
    print()

def victoire(board,s):
    combinaisons=[[0,1,2],[3,4,5][6,7,8],
                [0,3,6], [1,4,7], [2,5,8],
                [0,4,8], [2,4,6]
]

    for i in combinaisons:
        if board[i[0]]==board[i[1]] == board[i[2]] == s:
            return True
        return False


