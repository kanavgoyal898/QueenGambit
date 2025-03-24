import time
import random

import chess as ch
import engine as engine

import chess.svg
def save_board_state(board, filename='chess_board.svg'):
    """Save the current state of the board to an SVG file."""

    time.sleep(2)
    image = chess.svg.board(board)
    with open(filename, 'w') as f:
        f.write(image)

def play_engine_move(board, color, max_depth):
    """Make a move using the chess engine and update the board state."""

    chess_bot = engine.Engine(board, color, max_depth)
    move = chess_bot.get_best_move()
    if isinstance(move, ch.Move):
        board.push(move)
        save_board_state(board)
    else:
        return

def play_human_move(board, is_crazy=False):
    """Prompt the human player to make a move and update the board state."""

    try:
        if len(list(board.legal_moves)) == 0:
            return
        else:
            legal_moves = list(board.legal_moves)
            legal_moves = [move.uci() for move in legal_moves]
            legal_moves_str = ' '.join(legal_moves)
            print('enter UNDO/END to interrupt the game...')
            print(f'legal moves: {legal_moves_str}')
            move = input('enter your move: ') if not is_crazy else random.choice(legal_moves)
            if move.upper() == 'UNDO':
                try:
                    board.pop()
                    board.pop()
                    save_board_state(board)
                    play_human_move(board, is_crazy)
                except IndexError:
                    print("no more moves to undo...")
                    play_human_move(board, is_crazy)
            elif move.upper() == 'END':
                board.reset()
                save_board_state(board)
                print('the game is now terminated...')
                exit()
            else:
                board.push_san(move)
                save_board_state(board)
    except ValueError:
        print('invalid move! please try again...')
        play_human_move(board, is_crazy)

def start_game(color, max_depth, is_crazy=False, is_bot=False):
    """Start the game and alternate moves between the human player and the engine."""

    board = ch.Board()
    save_board_state(board)

    while not board.is_game_over():

        if color in ['b', 'black']:
            print('the engine is thinking...')
            play_engine_move(board, ch.WHITE, max_depth)

            if not is_bot:
                play_human_move(board, is_crazy)
            else:
                play_engine_move(board, ch.BLACK, max_depth)

        else:
            if not is_bot:
                play_human_move(board, is_crazy)
            else:
                play_engine_move(board, ch.WHITE, max_depth)

            print('the engine is thinking...')
            play_engine_move(board, ch.BLACK, max_depth)

    save_board_state(board)

    outcome = board.outcome()
    if outcome.winner is None:
        print('GAME OVER')
    elif (outcome.winner == ch.WHITE and color in ['w', 'white']) or (outcome.winner == ch.BLACK and color in ['b', 'black']):
        print('YOU WIN')
    else:
        print('YOU LOSE')
    board.reset()

    time.sleep(8)
    save_board_state(board)

def get_user_input():
    """Prompt the user to choose the color and difficulty level for the game."""

    color = None
    level = None
    max_depth = None
    crazy = None
    is_crazy = None
    bot = None
    is_bot = None

    colors = ['b', 'black', 'w', 'white']
    levels = {'easy' : 3, 'medium' : 5, 'difficult' : 7, 'auto' : 5}
    boolean_values = {'y' : True, 'yes': True, 'n': False, 'no': False}
    
    while color not in colors:
        color = input('choose your color (B/W): ').lower()
    color = color.lower()
    
    while level not in levels.keys():
        level = input('choose difficulty level (AUTO/EASY/MEDIUM/DIFFICULT): ').lower()
    max_depth = levels[level]

    while bot not in boolean_values.keys():
        bot = input('bot level? (yes/no): ').lower()
    is_bot = boolean_values[bot]

    if not is_bot:
        while crazy not in boolean_values.keys():
            crazy = input('crazy level? (yes/no): ').lower()
        is_crazy = boolean_values[crazy]


    start_game(color, max_depth, is_crazy, is_bot)

def main():
    get_user_input()

if __name__ == "__main__":
    main()
