import pygame
import OthelloAdditionalProcedures as P
import random
import math
BLACK = (0,0,0)
WHITE = (255,255,255)
empty = 0
black = 1
white = 2

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
        print(self.board)
        print("X: ",self.movex)
        print("Y: ",self.movey)

        #Check North Direction
        done = False
        counter = 1
        if self.board[self.movex][self.movey-counter] == self.opp and done == False:
            while self.board[self.movex][self.movey - counter] == self.opp and done == False:
                counter += 1
                if self.board[self.movex][self.movey - counter] == turn:
                    done = True
                    self.direction.append("N")
                    print("Move Valid: ",self.direction)
                elif done == False and self.board[self.movex][self.movey - counter] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
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
                    print("Move Valid: ",self.direction)
                elif done == False and self.board[self.movex][self.movey + counter] == 0:
                    done = True
                    counter = 1
                    print("Move not Valid")
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

        # colours
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,128,0)

        # display
        self.boardsize = (400,400)
        self.squaresize = 50
        self.screen = pygame.display.set_mode(self.boardsize)
        self.radius = 5

        # images
        self.images = ["black.png","white.png"]

    def drawBoard(self):
        img = pygame.image.load("othello-board.png")
        self.screen.blit(img,(0,0))
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] == 1:
                    img = pygame.image.load(self.images[0])
                    pygame.draw.circle(self.screen,(255,255,255),(x * 50 + 23 , y* 50 + 23  ),25)
                elif self.board[x][y] == 2:
                    img = pygame.image.load(self.images[1])
                    pygame.draw.circle(self.screen,(0,0,0),(x * 50 + 23  , y * 50 + 23  ),25)
        pygame.display.flip()


