import math
import svgutils
import pygame
import io

BOARD_SIZE = 600
SQUARE_SIZE = 600/8

def getMousePosition(event):
    pos = [None] * 2
    pos[0] = event.pos[0]
    pos[1] = event.pos[1]

    position = [None] * 2
    position[0] = math.floor(pos[0]/SQUARE_SIZE)
    position[1] = math.floor(pos[1]/SQUARE_SIZE)
    return position

def returnTurn(turn):
    if turn == 1:
        turn = 2
    else:
        turn = 1
    return turn

def getOppositeTurn(turn):
    if turn == 1:
        nextturn = 2
    else:
        nextturn = 1
    return nextturn

def load_and_scale_svg(filename, scale):
    svg_string = open(filename, "rt").read()
    start = svg_string.find('<svg')
    if start >= 0:
        svg_string = svg_string[:start+4] + f' transform="scale({scale})"' + svg_string[start+4:]

    start = svg_string.find('<g style="')
    if start >= 0:
        svg_string = svg_string[:start + 10] + f'overflow=visible; ' + svg_string[start + 10:]

    svg = svgutils.compose.SVG(filename)
    svg.scale(scale)
    figure = svgutils.compose.Figure(float(svg.height) * 2, float(svg.width) * 2, svg)
    figure.save('svgNew.svg')
    svg_string = open('svgNew.svg', "rt").read()
    return pygame.image.load(io.BytesIO(svg_string.encode()))


