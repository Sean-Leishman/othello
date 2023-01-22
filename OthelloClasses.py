import pygame
import OthelloAdditionalProcedures as P
import random
import math
BLACK = (0,0,0)
WHITE = (255,255,255)
empty = 0
black = 1
white = 2

SCREEN_SIZE = 800

BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE/8

class Piece():
    """
    Class used to represent pieces

    Attributes
    ----------
    pos: List[int]
    img: pygame.Img
    rect: pygame.Rect
    """
    def __init__(self, x, y, color):
        """
        :param x: int
            represents x coordinate of piece
        :param y: int
            represents y coordinate of piece
        :param color: int
            represents color of piece
        """
        self.pos = [x,y]
        self.color = color
        self.img = self.load_img()
        self.rect = self.load_rect()

    def load_img(self):
        """
        Initialise pygame.Image object from filenames
        :return: pygame.Image depending on piece color
        """
        black_circle_filename = "images\\black_circle(1).svg"
        white_circle_filename = "images\\white_circle(1).svg"

        if self.color == 1:
            return P.load_and_scale_svg(black_circle_filename, (SQUARE_SIZE - 5) / 300)
        elif self.color == 2:
            return P.load_and_scale_svg(white_circle_filename, (SQUARE_SIZE - 5) / 300)
        return None

    def load_rect(self):
        """
        Initialise pygame.Rect object for Piece
        :return: pygame.Rect
        """
        width = self.img.get_width()
        return pygame.Rect((SQUARE_SIZE - width)/2 + self.pos[0] * SQUARE_SIZE, (SQUARE_SIZE - width)/2 + self.pos[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    def get_img(self):
        return self.img

    def get_rect(self):
        width = self.img.get_width()
        return pygame.Rect(width/(2*SQUARE_SIZE) + self.pos[0] * SQUARE_SIZE, width/(2*SQUARE_SIZE) + self.pos[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

class Board():
    """
    Class used for game state and logic

    Attributes
    ----------
    board: List[List[int]]
        8*8 2D array representing the board with each integer representing a color
    movex: int
        X position of newly moved piece
    movey: int
        Y position of newly moved piece
    opp: int
    direction: List[str]
        directions in which pieces should be flipped from [movex, movey]
    """
    def __init__(self):

        self.board = [[0] * 8 for i in range(8)]
        self.board[3][4] = black
        self.board[4][3] = black
        self.board[3][3] = white
        self.board[4][4] = white
        self.movex = 0
        self.movey = 0
        self.opp = 0
        self.direction = [None]

    def setCo(self,x,y):
        self.movex = x
        self.movey = y

    def changeBoard(self,turn):
        """
        Set position on board to a color

        :param turn: int
            represents color of piece
        :return: int
            color of piece that has been placed
        """
        if self.board[self.movex][self.movey] == 0:
            self.board[self.movex][self.movey] = turn
        return self.board[self.movex][self.movey]

    def get_color(self):
        return self.board[self.movex][self.movey]
    def returnBoard(self):
        return self.board

    def checkWinner(self):
        """
        Check which color piece has a greater number of pieces on the board
        :return: int
            represents color of piece with a greater number of pieces on the board
        """
        white_pieces, black_pieces = self.get_piece_counts()
        if white_pieces > black_pieces:
            return white
        elif black_pieces > white_pieces:
            return black
        return 0

    def get_piece_counts(self):
        """
        Count number of pieces belonging to each color
        :return: (int,int)
            number of pieces for each color
        """
        white_pieces = 0
        black_pieces = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == black:
                    black_pieces += 1
                elif self.board[x][y] == white:
                    white_pieces += 1
        return (white_pieces, black_pieces)
    def checkAnyMoveValid(self, turn):
        """
        Checks whether any move for the turn is available
        :param turn: int
            represents color of the current turn
        :return: Bool
            true if a move is available
        """
        org_x = self.movex
        org_y = self.movey
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 0:
                    self.setCo(x,y)
                    if self.checkValid(turn)[-1] != None:
                        self.setCo(org_x, org_y)
                        return True
                    self.setCo(org_x, org_y)
        return False

    def getValidMoves(self, turn):
        """
        Find all valid moves available for the turn
        :param turn: int
            represents the color of the current turn
        :return: List[(int,int)]
            all valid moves -> E.g. [(x,y), (x1,y1)]
        """
        org_x = self.movex
        org_y = self.movey
        valid_moves = []
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # Make all moves and check if the move is valid and add to list
                if self.board[x][y] == 0:
                    self.setCo(x,y)
                    if self.checkValid(turn)[-1] != None:
                        valid_moves.append((x,y))
                        self.setCo(org_x, org_y)
                    self.setCo(org_x, org_y)
        return valid_moves
    def checkValid(self,turn):
        """
        Checks if move is valid by checking which directions pieces would be flipped
        :param turn: int
            represents color of current turn
        :return: List[str]
            represents directions in which pieces will be flipped
        """
        counter = 1
        valid = False
        done = False
        self.opp = P.getOppositeTurn(turn)
        self.direction = [None]

        #Check North Direction
        done = False
        counter = 1
        if self.movey-counter >= 0 and self.board[self.movex][self.movey-counter] == self.opp and done == False:
            while self.movey-counter-1 >= 0 and self.board[self.movex][self.movey - counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex][self.movey - counter] == turn:
                    done = True
                    self.direction.append("N")
                elif done == False and self.board[self.movex][self.movey - counter] == 0:
                    done = True
                    counter = 1

        # Check South Direction
        done = False
        counter = 1
        if self.movey+counter <= 7 and self.board[self.movex][self.movey + counter] == self.opp:
            while self.movey+counter+1 <= 7 and self.board[self.movex][self.movey + counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex][self.movey + counter] == turn:
                    done = True
                    self.direction.append("S")
                elif done == False and self.board[self.movex][self.movey + counter] == 0:
                    done = True
                    counter = 1

        # Check West Direction
        done = False
        counter = 1
        if self.movex-counter >= 0 and self.board[self.movex - counter][self.movey] == self.opp:
            while self.movex-counter-1 >= 0 and self.board[self.movex - counter][self.movey] == self.opp and done == False:
                counter += 1
                if self.board[self.movex - counter][self.movey] == turn:
                    done = True
                    self.direction.append("W")
                elif done == False and self.board[self.movex - counter][self.movey] == 0:
                    done = True
                    counter = 1

        # CHeck East Direction
        done = False
        counter = 1
        if self.movex+counter <= 7 and self.board[self.movex + counter][self.movey] == self.opp:
            while self.movex+counter+1 <= 7 and self.board[self.movex + counter][self.movey] == self.opp and done == False:
                counter += 1
                if self.board[self.movex + counter][self.movey] == turn:
                    done = True
                    self.direction.append("E")
                elif done == False and self.board[self.movex + counter][self.movey] == 0:
                    done = True
                    counter = 1

        # Check North East Direction
        done = False
        counter = 1
        if self.movex+counter <= 7 and self.movey-counter >= 0 and self.board[self.movex + counter][self.movey - counter] == self.opp:
            while self.movex+counter+1 <= 7 and self.movey-counter-1 >= 0 and self.board[self.movex + counter][self.movey - counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex + counter][self.movey- counter] == turn:
                    done = True
                    self.direction.append("NE")
                elif self.board[self.movex + counter][self.movey - counter] == 0:
                    done = True
                    counter = 1

        # Check North West Direction
        done = False
        counter = 1
        if self.movex-counter >= 0 and self.movey-counter >= 0 and self.board[self.movex - counter][self.movey - counter] == self.opp:
            while self.movex-counter-1 >= 0 and self.movey-counter-1 >= 0 and self.board[self.movex - counter][self.movey - counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex - counter][self.movey- counter] == turn:
                    done = True
                    self.direction.append("NW")
                elif self.board[self.movex - counter][self.movey- counter] == 0:
                    done = True
                    counter = 1
        # Check South East Direction
        done = False
        counter = 1
        if self.movex+counter <= 7 and self.movey+counter <= 7 and self.board[self.movex + counter][self.movey + counter] == self.opp:
            while self.movex+counter+1 <= 7 and self.movey+counter+1 <= 7 and self.board[self.movex + counter][self.movey + counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex + counter][self.movey + counter] == turn:
                    done = True
                    self.direction.append("SE")
                elif self.board[self.movex + counter][self.movey + counter] == 0:
                    done = True
                    counter = 1

        # CHeck South West Direction
        done = False
        counter = 1
        if self.movex-counter >= 0 and self.movey+counter <= 7 and self.board[self.movex - counter][self.movey + counter] == self.opp:
            while self.movex-counter-1 >= 0 and self.movey+counter+1 <= 7 and self.board[self.movex - counter][self.movey + counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex - counter][self.movey + counter] == turn:
                    done = True
                    self.direction.append("SW")
                elif done == False and self.board[self.movex - counter][self.movey + counter] == 0:
                    done = True
                    counter = 1

        return self.direction

    def flipPieces(self,turn):
        """
        Switch pieces in between same color piece in each direction and original position
        :param turn: int
            represents color of turn piece
        :return:
        """
        for x in range(len(self.direction)):
            # In north Direction
            if self.direction[x] == "N":
                counter = 1
                while self.board[self.movex][self.movey - counter] != turn:
                    self.board[self.movex][self.movey - counter] = turn
                    counter += 1

            # In South Direction
            if self.direction[x] == "S":
                counter = 1
                while self.board[self.movex][self.movey + counter] != turn:
                    self.board[self.movex][self.movey + counter] = turn
                    counter += 1

            # In East Direction
            if self.direction[x] == "E":
                counter = 1
                while self.board[self.movex + counter][self.movey] != turn:
                    self.board[self.movex + counter][self.movey] = turn
                    counter += 1

            # In West Direction
            if self.direction[x] == "W":
                counter = 1
                while self.board[self.movex - counter][self.movey] != turn:
                    self.board[self.movex - counter][self.movey] = turn
                    counter += 1

            # In North East Direction
            if self.direction[x] == "NE":
                counter = 1
                while self.board[self.movex + counter][self.movey - counter] != turn:
                    self.board[self.movex + counter][self.movey - counter] = turn
                    counter += 1

            # In North West Direction
            if self.direction[x] == "NW":
                counter = 1
                while self.board[self.movex - counter][self.movey - counter] != turn:
                    self.board[self.movex - counter][self.movey - counter] = turn
                    counter += 1

            # In South East Direction
            if self.direction[x] == "SE":
                counter = 1
                while self.board[self.movex + counter][self.movey + counter] != turn:
                    self.board[self.movex + counter][self.movey + counter] = turn
                    counter += 1

            # In South West Direction
            if self.direction[x] == "SW":
                counter = 1
                while self.board[self.movex - counter][self.movey + counter] != turn:
                    self.board[self.movex - counter][self.movey + counter] = turn
                    counter += 1

    def resetMove(self, move):
        self.board[self.movex][self.movey] = move

    def checkDuplicate(self):
        if self.board[self.movex][self.movey] != 0:
            return True
        else:
            return False

    def resetDuplicate(self,turn):
        self.opp = P.getOppositeTurn(turn)
        self.board[self.movex][self.movey] = self.opp

class GUI():
    """
    Class that is used to display GUI
    """
    def __init__(self,screen, board):

        self.board = board
        self.screen = screen

        self.font = pygame.font.SysFont('Comic Sans MS', 30)

        self.img_board = [[None] * 9 for i in range(9)]
        self.img_board[3][4] = Piece(3, 4, black)
        self.img_board[4][3] = Piece(4, 3, black)
        self.img_board[3][3] = Piece(3, 3, white)
        self.img_board[4][4] = Piece(4, 4, white)

        # colours
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,128,0)

        # display
        self.boardsize = (BOARD_SIZE,BOARD_SIZE)
        self.squaresize = SQUARE_SIZE
        self.screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        self.radius = 5

    def drawBoard(self, board, turn, piece_counts):
        self.board = board
        self.screen.fill((128,128,128))

        for i in range(8):
            for j in range(8):
                if i % 2 == 0 and j % 2 == 0 or i % 2 == 1 and j % 2 == 1:
                    pygame.draw.rect(self.screen, (153, 102, 51),
                                     (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(self.screen, (255, 204, 153),
                                     (i * SQUARE_SIZE, j * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 1:
                    self.img_board[x][y] = Piece(x,y,1)
                    self.screen.blit((self.img_board[x][y]).get_img(), (self.img_board[x][y]).get_rect())
                elif self.board[x][y] == 2:
                    self.img_board[x][y] = Piece(x,y,2)
                    self.screen.blit((self.img_board[x][y]).get_img(),(self.img_board[x][y]).get_rect())

        text_surface = self.font.render(str(piece_counts), False, (0, 0, 0))
        self.screen.blit(text_surface, (BOARD_SIZE, 0))

        turn_piece = Piece(8,1, P.getOppositeTurn(turn))
        self.screen.blit((turn_piece.get_img()), turn_piece.get_rect())

        pygame.display.flip()


