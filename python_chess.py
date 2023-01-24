import chess

#Creates a new board
board = chess.Board()

#Validate the move
while not board.is_game_over():
    #Get the move from the User
    move = input("Enter a move in SAN notation: ")
    #Validate the move
    try:
        move = board.parse_san(move)
        board.push(move)
        print("Move has been executed and is valid")
        #Checks if the move is either check or checkmate
        print("Current board:")
        print(board)
        if board.is_check():
            print("Check!")
        if board.is_checkmate():
            print("You got checkmated you lost!")
            break
    except ValueError:
        print("Invalid move")

#Save on PNG noation
with open("game.pgn", "w") as f:
    f.write(board.pgn)


#TODO: IMPLEMENT LELAA CHESS ENGINE
