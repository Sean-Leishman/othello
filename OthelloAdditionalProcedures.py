import math
def getMousePosition(event):
    pos = [None] * 2
    pos[0] = event.pos[0]
    pos[1] = event.pos[1]

    position = [None] * 2
    position[0] = math.floor(pos[0]/50)
    position[1] = math.floor(pos[1]/50)
    print("found mouse at",position[0],position[1])
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

