import OthelloClasses as C
import OthelloAdditionalProcedures as P
import pygame

pygame.init()

board = C.Board()
real = board.returnBoard()
gui = C.GUI(real)

clock = pygame.time.Clock()
done = False

turn  = 1
while done == False:
    truth = True
    for event in pygame.event.get():  # Check for an event (mouse click, key press)
        if event.type == pygame.QUIT:  # If user clicked close window
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = P.getMousePosition(event)
            turn = P.returnTurn(turn)
            board.setCo(pos[0],pos[1])
            if board.checkDuplicate() == True:
                board.resetDuplicate(turn)
            else:
                truth = False
                board.changeBoard(turn)
            valid = board.checkValid(turn)
            index = len(valid)
            if valid[index-1] != None:
                board.flipPieces(turn)
            elif valid[index- 1] == None and truth == False:
                board.resetMove()
                turn = P.getOppositeTurn(turn)
            gui.drawBoard(real)



    pygame.display.update()  # Go ahead and update the screen with what we've drawn.
    gui.drawBoard(real)
    clock.tick(20)

pygame.quit()  # Close the window and quit.
