import pygame
import math
import sys
import warnings
from copy import deepcopy
import pygame_menu
from StartMenu import StartMenu
from OthelloMain import Game
from RestartMenu import RestartMenu

WIDTH = 800
HEIGHT = 600

BOARD_WIDTH = 600
SQUARE_SIZE = BOARD_WIDTH / 8

WHITE = (255,255,255)
BLACK  = (0,0,0)

class Controller():
    """
    Class for Othello Game and Menu Wrapper

    Attributes
    ----------
    font: pygame.Font
    screen: pygame.Display
    time: pygame.time.Clock
    state: int
        -1 -> represents game is not started
        0 -> represents game that has finished and is at restart
        1 -> represents game that has been started/restarted
    startMenu: StartMenu
    color_selected: int
    opponent_selected: int
    """
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.time = pygame.time.Clock()
        self.state = -1
        self.start_menu = StartMenu()

        self.color_selected = None
        self.opponent_selected = None

    def main(self):
        """
        Main game loop

        :return:
        """
        winner = None
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.state == -1:
                # Game has not been started so display start menu
                self.start_menu.main(events,self.screen)
                pygame.display.update()
                if not self.start_menu.start_menu_state:
                    # Game is to be started and as such declare initialisation variables
                    self.state = 1
                    self.start_menu.start_menu_state = True

                    self.color_selected = self.start_menu.color
                    self.opponent_selected = self.start_menu.opponent
            elif self.state == 0:
                # Game that has been finished so set Restart Menu
                self.restart_menu.winner = winner
                self.restart_menu.main(events, self.screen)
                pygame.display.update()
                if not self.restart_menu.start_menu_state:
                    # Game has been restarted so set game variables
                    self.state = 1
                    self.restart_menu.start_menu_state = True

                    self.color_selected = self.restart_menu.color
                    self.opponent_selected = self.restart_menu.opponent
            elif self.state == 1:
                # Game has been set to start
                self.game = Game(self.screen, self.time, self.font
                                 , self.color_selected, self.opponent_selected)
                break
        # Start main game loop
        self.game.main()

        # Declare winner if one exists
        if self.game.game_state == 1:
            winner = self.game.winner
        else:
            winner = None
        self.game.game_state = 0
        self.state = 0

        # Display Restart Menu
        self.restart_menu = RestartMenu(winner)
        self.main()

if __name__ == "__main__":
    Controller().main()
