from copy import deepcopy
import OthelloAdditionalProcedures as P
from operator import itemgetter
import math

class Computer():
    def __init__(self, color):
        self.color = color
    def getMove(self, curDepth, turn, maxTurn, targetDepth, board):
        copy_board = deepcopy(board)
        max_val = -math.inf
        max_move = None
        for idx,move in enumerate(copy_board.getValidMoves(turn)):
            old_board = deepcopy(copy_board)
            copy_board.setCo(move[0], move[1])
            copy_board.changeBoard(turn)
            copy_board.checkValid(turn)
            copy_board.flipPieces(turn)
            minimax_val = self.minimax(curDepth+1, P.getOppositeTurn(turn), not maxTurn, targetDepth, copy_board, -math.inf, math.inf)
            if max_val < minimax_val:
                max_val = minimax_val
                max_move = move
        return max_move

    def minimax(self, curDepth, turn, maxTurn, targetDepth, board, alpha, beta):
        copy_board = deepcopy(board)
        if (curDepth == targetDepth or not copy_board.checkAnyMoveValid(turn)):
            white_pieces, black_pieces = copy_board.get_piece_counts()
            if white_pieces > black_pieces:
                if self.color == 1:
                    score = white_pieces / (white_pieces+black_pieces)
                else:
                    score = -white_pieces / (white_pieces+black_pieces)
            elif black_pieces > white_pieces:
                if self.color == 2:
                    score = black_pieces / (white_pieces+black_pieces)
                else:
                    score = -black_pieces / (white_pieces+black_pieces)
            else:
                score = 0
            return score

        scores = []
        moves = []
        if maxTurn:
            for idx,move in enumerate(copy_board.getValidMoves(turn)):
                bestval = -math.inf
                old_board = deepcopy(copy_board)
                copy_board.setCo(move[0], move[1])
                copy_board.changeBoard(turn)
                copy_board.checkValid(turn)
                copy_board.flipPieces(turn)
                minimax_val = self.minimax(curDepth+1, P.getOppositeTurn(turn), not maxTurn, targetDepth, copy_board, alpha, beta)
                copy_board = old_board
                bestval = max(minimax_val, bestval)
                alpha = max(bestval, alpha)
                if beta <= alpha:
                    break
            return bestval
        else:
            for idx,move in enumerate(copy_board.getValidMoves(turn)):
                worstval = math.inf
                old_board = deepcopy(copy_board)
                copy_board.setCo(move[0], move[1])
                copy_board.changeBoard(turn)
                copy_board.checkValid(turn)
                copy_board.flipPieces(turn)
                minimax_val = self.minimax(curDepth+1, P.getOppositeTurn(turn), not maxTurn, targetDepth, copy_board, alpha, beta)
                copy_board = old_board
                worstval = min(minimax_val, worstval)
                beta = min(worstval, beta)
                if beta <= alpha:
                    break
            return worstval