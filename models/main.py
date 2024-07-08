import cprint
import chess.svg
import chess as ch
import ChessEngine as engine

def save_board_state(board, filename='chess_board.svg'):
    """Save the current state of the board to an SVG file."""
    image = chess.svg.board(board)
    with open(filename, 'w') as f:
        f.write(image)
    f.close()

def play_engine_move(board, color, max_depth):
    """Make a move using the chess engine and update the board state."""
    chessbot = engine.Engine(board, color, max_depth)
    move = chessbot.get_best_move()
    board.push(move)
    save_board_state(board)

def play_human_move(board):
    """Prompt the human player to make a move and update the board state."""
    try:
        if len(list(board.legal_moves)) == 0:
            return
        else:
            legal_moves = list(board.legal_moves)
            legal_moves = [move.uci() for move in legal_moves]
            legal_moves_str = ' '.join(legal_moves)
            cprint.cprint.err(f'legal moves: {legal_moves_str}', interrupt=False)
            move = input('enter your move: ')
            if move.upper() == 'UNDO':
                try:
                    board.pop()
                    board.pop()
                    save_board_state(board)
                    play_human_move(board)
                except IndexError:
                    cprint.cprint.fatal("no more moves to undo...")
            elif move.upper() == 'END':
                board.reset()
                save_board_state(board)
                cprint.cprint.fatal('the game is now terminated...')
                exit()
            else:
                board.push_san(move)
                save_board_state(board)
    except ValueError:
        cprint.cprint.fatal('invalid move! please try again...')
        play_human_move(board)

def start_game(board, color, max_depth):
    """Start the game and alternate moves between the human player and the engine."""
    cprint.cprint.info('enter UNDO/END to interrupt the game')

    if color in ['b', 'black']:
        while not board.is_game_over():
            cprint.cprint.ok('the engine is thinking...')
            play_engine_move(board, ch.WHITE, max_depth)
            play_human_move(board)
    else:
        while not board.is_game_over():
            play_human_move(board)
            cprint.cprint.ok('the engine is thinking...')
            play_engine_move(board, ch.BLACK, max_depth)

    save_board_state(board)

    outcome = board.outcome()
    if outcome.winner is None:
        cprint.cprint.warn('GAME OVER')
    elif (outcome.winner == ch.WHITE and color in ['w', 'white']) or (outcome.winner == ch.BLACK and color in ['b', 'black']):
        cprint.cprint.info('YOU WIN')
    else:
        cprint.cprint.fatal('YOU LOSE')

    board.reset()

def get_user_input():
    """Prompt the user to choose the color and difficulty level for the game."""
    board = ch.Board()
    save_board_state(board)

    color = None
    colors = ['b', 'black', 'w', 'white']
    while color not in colors:
        color = input('choose your color (B/W): ').lower()
    color = color.lower()
    
    level = None
    max_depth = None
    levels = {
        'easy' : 3,
        'medium' : 5,
        'difficult' : 7,
        'auto' : 5
    }
    while level not in levels.keys():
        level = input('choose difficulty level (auto/easy/medium/difficult): ').lower()
    max_depth = levels[level]

    start_game(board, color, max_depth)

def main():
    get_user_input()

if __name__ == "__main__":
    main()
