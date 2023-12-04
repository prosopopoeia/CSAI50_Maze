"""
Tic Tac Toe Player
"""
import copy
import math
import sys

X = "X"
O: str = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    playa = X
    xcount = 0
    ycount = 0
    for row in board:
        xcount += row.count(X)
        ycount += row.count(O)
    if ycount < xcount:
        playa = O
    return playa


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[i]):
            if board[i][j] == EMPTY:
                available_actions.add((i, j))
            j += 1
        i += 1
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    ##  NEED TO RETURN EXCEPTION IF INVALID!
    new_board = copy.deepcopy(board)
    i, j = (0, 0)
    if action is not None:
        i, j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_player = None
    i = 0

    if board[0][0] == board[1][0] == board[2][0] != EMPTY:
        winning_player = board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != EMPTY:
        winning_player = board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != EMPTY:
        winning_player = board[0][2]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        winning_player = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        winning_player = board[0][2]
    
    while i < len(board):
        if board[i].count('X') == 3:
            winning_player = board[i][0]
        if board[i].count('O') == 3:
            winning_player = board[i][0]
        i += 1
        
    return winning_player


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    i = 0
    over = False
    if winner(board) is not None:
        over = True
    if not over:
        over = not any(EMPTY in sublist for sublist in board)
    return over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return_value = 0
    if winner(board) == 'X':
        return_value = 1
    elif winner(board) == 'O':
        return_value = -1
    return return_value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    action_set = actions(board)
    optimal_move = None
    move_value = 0

    if player(board) == O:
        best_move_value = sys.maxsize
        for action in action_set:
            move_value = max_val(result(board, action))
            if move_value < best_move_value:
                best_move_value = move_value
                optimal_move = action
    else:
        if len(action_set) == 9:  # if this is the first move
            optimal_move = (0, 0)  # then optimal move is a corner, we will select the upper left side
        else:
            best_move_value = -sys.maxsize
            for action in action_set:
                move_value = min_val(result(board, action))
                if move_value > best_move_value:
                    best_move_value = move_value
                    optimal_move = action

    return optimal_move


def min_val(board):
    v = sys.maxsize
    if terminal(board):
        return utility(board)
    action_set = actions(board)
    for action in action_set:
        max_move = max_val(result(board, action))
        v = min(v, max_move)
    return v


def max_val(board):
    v = -sys.maxsize
    if terminal(board):
        return utility(board)
    action_set = actions(board)
    for action in action_set:
        v = max(v, min_val(result(board, action)))
    return v # None