# TODO fix issue when no pieces are certain color NoneType -> move line 60
# TODO fix issue with random piece selection in start menu makes computer self-play

import OthelloClasses as C
import OthelloAdditionalProcedures as P
import pygame
import sys
from Computer import Computer
class Game():
    """
    Class for Othello Game. Handles Pygame UI elements

    Attributes
    ----------
    board: Board
    real: List[List[int]]
    gui: GUI
    font: pygame.Font
    screen: pygame.Display
    time: pygame.time.Clock
    color: int
        represents color of user piece
    opponent: int
        represents color of opponent piece
    game_state: int
        0 -> game is unfinished
        1 -> game has finished
    winner: int
        represents color of winning piece
    user: int
        represents color of user
    computer: Computer
    """
    def __init__(self,screen, time, font, color=0, opponent=0):
        pygame.init()

        self.board = C.Board()
        self.real = self.board.returnBoard()
        self.screen = screen
        self.gui = C.GUI(screen, self.real)

        self.time = time
        self.font = font
        self.color = color
        self.opponent = opponent

        self.game_state = 0
        self.winner = 0

        self.user = color
        self.turn  = 1
        self.computer = Computer(self.turn)
    def main(self):
        """
        Main game loop
        :return:
        """
        turn = 1
        while True:
            truth = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close window
                    pygame.quit()
                    sys.exit() # Flag that we are done so we exit this loop
                if self.opponent == 0 or self.user == turn:
                    # If user move vs computer or game is user vs user
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = P.getMousePosition(event)
                        turn = P.returnTurn(turn)
                        self.board.setCo(pos[0], pos[1])
                        original_color = self.board.get_color()
                        coord_color = self.board.changeBoard(turn)
                        valid = self.board.checkValid(turn)
                        index = len(valid)
                        if valid[index - 1] != None and original_color == 0:
                            self.board.flipPieces(turn)
                            if not self.board.checkAnyMoveValid(P.returnTurn(turn)):
                                self.winner = self.board.checkWinner()
                                self.game_state = 1
                        elif valid[index - 1] == None or original_color != 0:
                            self.board.resetMove(original_color)
                            turn = P.getOppositeTurn(turn)
                        self.gui.drawBoard(self.real, turn, self.board.get_piece_counts())
                else:
                    turn = P.returnTurn(turn)
                    move = self.computer.getMove(0, turn, True, 6, self.board)
                    self.board.setCo(move[0], move[1])
                    coord_color = self.board.changeBoard(turn)
                    valid = self.board.checkValid(turn)
                    index = len(valid)
                    if valid[index - 1] != None:
                        self.board.flipPieces(turn)
                        if not self.board.checkAnyMoveValid(P.returnTurn(turn)):
                            self.winner = self.board.checkWinner()
                            self.game_state = 1
                    elif valid[index - 1] == None or original_color != 0:
                        self.board.resetMove(original_color)
                        turn = P.getOppositeTurn(turn)
                    self.gui.drawBoard(self.real, turn, self.board.get_piece_counts())

            if self.game_state != 0:
                break



            pygame.display.update()  # Go ahead and update the screen with what we've drawn.
            self.gui.drawBoard(self.real, turn, self.board.get_piece_counts())
            self.time.tick(20)
