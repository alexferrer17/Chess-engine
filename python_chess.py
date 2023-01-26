import chess
import chess.engine
import subprocess
from stockfish import Stockfish

# Creates a new board
board = chess.Board()

# Start the engine
engine = Stockfish(path="/opt/homebrew/Cellar/stockfish/15.1/bin/stockfish")

# Initialize the moves list
moves = []
list_moves_uci = []


# Validate the move
while not board.is_game_over():

    # Get the move from the User

    print("Enter a move in SAN notation")
    user_move = input()

    # Validate the move
    try:

        # Making a user move
        board_move =  board.parse_san(user_move)
        board.push(board_move)

        #Formating the moves in uci format
        moves_uci = board_move.uci()
        list_moves_uci.append(moves_uci)
        print(list_moves_uci)

        # Validade the move and print board
        print("Move has been executed and is valid")
        print(board)

        # Check the list
        print(list_moves_uci)

        # Making the engine move
        engine.make_moves_from_current_position(list_moves_uci)
        engine_move = engine.get_best_move(1000)
        board_move_engine =  board.parse_san(engine_move)
        board.push(board_move_engine)
        list_moves_uci.append(engine_move)
        print(list_moves_uci)



        #print the engine move
        print(board)

        # Check for checks ;)
        if board.is_check():
            print("Check!")
        if board.is_checkmate():
            print("You got checkmated you lost!")
            break

    # Throw exception
    except ValueError:
        print("Invalid move")

# Save the game in PGN notation
with open("game.pgn", "w") as f:
    f.write(board.pgn())



#TODO: IMPLEMENT STOCKFISH!!

#DAY 1: IMPLEMENT THE IDEA... USING python chess library
#DAY 2: Impleneted check and checkmate feature and tried to implement a chess engine did not work
#DAY 3: #TODO: IMPLEMENT LELAA CHESS ENGINE OR STOCKFISH!!
#DAY 3: Debugging
#DAY 4: IMPLEMENTED STOCKFISH bugg on second interaction
