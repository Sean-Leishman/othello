import pygame
import OthelloAdditionalProcedures as P
import random
import math
BLACK = (0,0,0)
WHITE = (255,255,255)
empty = 0
black = 1
white = 2

BOARD_SIZE = 600
SQUARE_SIZE = 600/8

class Piece():
    def __init__(self, x, y, color):
        self.pos = [x,y]
        self.color = color
        self.img = self.load_img()
        self.rect = self.load_rect()

    def load_img(self):
        black_circle_filename = "images\\black_circle(1).svg"
        white_circle_filename = "images\\white_circle(1).svg"

        if self.color == 1:
            return P.load_and_scale_svg(black_circle_filename, (SQUARE_SIZE - 5) / 300)
        elif self.color == 2:
            return P.load_and_scale_svg(white_circle_filename, (SQUARE_SIZE - 5) / 300)
        return None

    def load_rect(self):
        width = self.img.get_width()
        return pygame.Rect((SQUARE_SIZE - width)/2 + self.pos[0] * SQUARE_SIZE, (SQUARE_SIZE - width)/2 + self.pos[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    def get_img(self):
        return self.img

    def get_rect(self):
        width = self.img.get_width()
        print(self.pos[0] * SQUARE_SIZE,(SQUARE_SIZE - width)/2, SQUARE_SIZE, width, 400 * 5 / 300)
        return pygame.Rect(width/(2*SQUARE_SIZE) + self.pos[0] * SQUARE_SIZE, width/(2*SQUARE_SIZE) + self.pos[1] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

class Board():

    def __init__(self):

        self.board = [[0] * 9 for i in range(9)]
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
        self.board[self.movex][self.movey] = turn

    def returnBoard(self):
        return self.board

    def checkValid(self,turn):
        counter = 1
        valid = False
        done = False
        self.opp = P.getOppositeTurn(turn)
        self.direction = [None]

        #Check North Direction
        done = False
        counter = 1
        if self.board[self.movex][self.movey-counter] == self.opp and done == False:
            while self.board[self.movex][self.movey - counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex][self.movey - counter] == turn:
                    done = True
                    self.direction.append("N")
                elif done == False and self.board[self.movex][self.movey - counter] == 0:
                    done = True
                    counter = 1
        else:
            print("Move Not Valid")

        # Check South Direction
        done = False
        counter = 1
        if self.board[self.movex][self.movey + counter] == self.opp:
            while self.board[self.movex][self.movey + counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex][self.movey + counter] == turn:
                    done = True
                    self.direction.append("S")
                elif done == False and self.board[self.movex][self.movey + counter] == 0:
                    done = True
                    counter = 1
        else:
            print("Move Not Valid")

        # Check West Direction
        done = False
        counter = 1
        if self.board[self.movex - counter][self.movey] == self.opp:
            while self.board[self.movex - counter][self.movey] == self.opp and done == False:
                counter += 1
                if self.board[self.movex - counter][self.movey] == turn:
                    done = True
                    self.direction.append("W")
                    print("Move Valid: ",self.direction)
                elif done == False and self.board[self.movex - counter][self.movey] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
        else:
            print("Move Not Valid")

        # CHeck East Direction
        done = False
        counter = 1
        if self.board[self.movex + counter][self.movey] == self.opp:
            while self.board[self.movex + counter][self.movey] == self.opp and done == False:
                counter += 1
                if self.board[self.movex + counter][self.movey] == turn:
                    done = True
                    self.direction.append("E")
                    print("Move Valid: ",self.direction)
                elif done == False and self.board[self.movex + counter][self.movey] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
        else:
            print("Move Not Valid")

        # Check North East Direction
        done = False
        counter = 1
        if self.board[self.movex + counter][self.movey - counter] == self.opp:
            while self.board[self.movex + counter][self.movey - counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex + counter][self.movey- counter] == turn:
                    done = True
                    self.direction.append("NE")
                    print("Move Valid ",self.direction)
                elif self.board[self.movex + counter][self.movey- counter] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
        else:
            print("Move Not Valid")

        # Check North West Direction
        done = False
        counter = 1
        if self.board[self.movex - counter][self.movey - counter] == self.opp:
            while self.board[self.movex - counter][self.movey - counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex - counter][self.movey- counter] == turn:
                    done = True
                    self.direction.append("NW")
                    print("Move Valid ",self.direction)
                elif self.board[self.movex - counter][self.movey- counter] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
        else:
            print("Move Not Valid")

        # Check South East Direction
        done = False
        counter = 1
        if self.board[self.movex + counter][self.movey + counter] == self.opp:
            while self.board[self.movex + counter][self.movey + counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex + counter][self.movey + counter] == turn:
                    done = True
                    self.direction.append("SE")
                    print("Move Valid: ",self.direction)
                elif self.board[self.movex + counter][self.movey + counter] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
        else:
            print("Move Not Valid")

        # CHeck South West Direction
        done = False
        counter = 1
        if self.board[self.movex - counter][self.movey + counter] == self.opp:
            while self.board[self.movex - counter][self.movey + counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex - counter][self.movey + counter] == turn:
                    done = True
                    self.direction.append("SW")
                    print("Move Valid: ", self.direction)
                elif done == False and self.board[self.movex - counter][self.movey + counter] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
        else:
            print("Move Not Valid")
        print(counter)

        return self.direction

    def flipPieces(self,turn):
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

    def resetMove(self):
        self.board[self.movex][self.movey] = 0

    def checkDuplicate(self):
        if self.board[self.movex][self.movey] != 0:
            return True
        else:
            return False

    def resetDuplicate(self,turn):
        self.opp = P.getOppositeTurn(turn)
        self.board[self.movex][self.movey] = self.opp

class GUI():

    def __init__(self,board):

        self.board = board

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
        self.boardsize = (600,600)
        self.squaresize = 50
        self.screen = pygame.display.set_mode(self.boardsize)
        self.radius = 5

    def drawBoard(self, board):
        self.board = board
        self.screen.fill(self.white)

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

        pygame.display.flip()


