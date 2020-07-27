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
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    playerX = 0
    playerO = 0

    for row in board:
        for element in row:
            if element == X:
                playerX += 1
            elif element == O:
                playerO += 1

    if playerX > playerO:
        return O
    elif playerX == playerO and not terminal(board):
        return X
    else:
        return None
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row in range(len(board)):
        for element in range(len(board)):
            if board[row][element] != X and board[row][element] != O:
                possible_actions.add((row, element))

    return possible_actions
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if terminal(board):
        raise ValueError("Game Over")
    elif action not in actions(board):
        raise ValueError("Action Invalid")
    else:
        turn = player(board)
        state = copy.deepcopy(board)
        (i, j) = action
        state[i][j] = turn

    return state

    # raise NotImplementedError


def horizontal(board):
    if board[0][0] == board[0][1] == board[0][2] != None:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != None:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != None:
        return board[2][0]
    else:
        return None


def vertical(board):
    if board[0][0] == board[1][0] == board[2][0] != None:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != None:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != None:
        return board[0][2]
    else:
        return None


def diagonal(board):
    if board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    else:
        return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check row horizontally, vertically and diagonally
    if horizontal(board) != None:
        return horizontal(board)
    elif vertical(board) != None:
        return vertical(board)
    elif diagonal(board) != None:
        return diagonal(board)
    else:
        return None

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in board:
        for element in row:
            if element == EMPTY:
                return False
    return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    # raise NotImplementedError


def max_value(board,alpha,beta):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action),alpha,beta))
        alpha = max(alpha,v)
        if alpha >= beta:
            return v
    return v


def min_value(board,alpha,beta):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action),alpha,beta))
        beta = min(beta,v)
        if alpha >= beta:
            return v
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)

    # if AI start first and the board is empty, choose the center cell
    if board == initial_state():
        return (1, 1)

    alpha = float('-inf')
    beta = float('inf')
    if turn == X:  # max choose to maximise the minimum payoff
        # value = float('-inf')
        for action in actions(board):
            minimum = min_value(result(board, action),alpha,beta)
            if minimum > alpha:
                alpha = minimum
                move = action
    else:  # min choose to minimise the maximum payoff
        # value = float('inf')
        for action in actions(board):
            maximum = max_value(result(board, action),alpha,beta)
            if beta > maximum:
                beta = maximum
                move = action
    return move
    # raise NotImplementedError
