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
        print("Current board:")
        print(board)
    except ValueError:
        print("Invalid move")

#Save on PNG noation
with open("game.pgn", "w") as f:
    f.write(board.pgn)



### Debuggin weather I can create a chess baord out of just the help of chatgpt

#TODO: IMPLEMENT CHECK MATE AND CHECK
