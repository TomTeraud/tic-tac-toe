"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    # """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_player_turns = 0
    o_player_turns = 0
    # Counts turns of each players
    for row in board:
        for cell in row:
            if cell == X:
                x_player_turns = x_player_turns + 1
            if cell == O:
                o_player_turns = o_player_turns + 1

    if x_player_turns > o_player_turns:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    a = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                a.add((i,j))
    return a


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action in actions(board):
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board)
        return new_board
    raise ValueError("Not valid action!!!")
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = get_board_lines(board)
    # Empty board
    if len(lines) == 1:
        return None
    
    for line in lines:
        if None not in line and len(set(line)) == 1:
            return line[0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is None:
        # Is there available moves on board?
        if len(actions(board)) == 0:
            return True
        else:
            return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w is None:
        return 0
    return 1 if w == X else -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # None if there is winner or tie(no empty cells left on board)
    if terminal(board):
        return None
    
    tie_action = None
    if player(board) is X:
        # loop for maximizing player
        for action in actions(board):
            max_v = min_value(result(board, action))
            if max_v == 1:
                return action
            elif max_v == 0:
                tie_action = action
        return tie_action
                
    else:
        # loop for minimizing player
        for action in actions(board):
            min_v = max_value(result(board, action))
            if min_v == -1:
                return action
            elif min_v == 0:
                tie_action = action
        return tie_action
       
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def get_board_lines(board):
    """
    Returns target lines on board as set of tuples
    """
    r0 = board[0][0], board[0][1], board[0][2]
    r1 = board[1][0], board[1][1], board[1][2]
    r2 = board[2][0], board[2][1], board[2][2]
    c0 = board[0][0], board[1][0], board[2][0]
    c1 = board[0][1], board[1][1], board[2][1]
    c2 = board[0][2], board[1][2], board[2][2]
    d0 = board[0][0], board[1][1], board[2][2]
    d1 = board[2][0], board[1][1], board[0][2]    
    
    return {r0, r1, r2, c0, c1, c2, d0, d1}
