def afficher_plateau(board):
    print("\n")
    for i in range(0,9,3):
        print(board[i],"|",board[i+1],"|",board[i+2])
        if i <6:
            print("--+---+--")
    print()
