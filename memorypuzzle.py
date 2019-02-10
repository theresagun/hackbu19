#import easygui
import random, pygame, sys
from pygame.locals import *

windowWidth = 430 # size of window's width in pixels
windowHeight = 325 # size of windows' height in pixels
boxSize = 100 # size of box height & width in pixels
gapSize = 10 # size of gap between boxes in pixels
boardWidth = 4 # number of columns of icons
boardHeight = 3 # number of rows of icons
xMargin = int((windowWidth - (boardWidth * (boxSize + gapSize))) / 2)
yMargin = int((windowHeight - (boardHeight * (boxSize + gapSize))) / 2)
LIGHTCORAL = (240, 128, 128)
CRIMSON = (220, 20, 60)
WHITE =(255,255,255)
BGColor = LIGHTCORAL #F08080 or (240, 128, 128)
#LIGHTBGCOLOR
boxColor = CRIMSON #DC143C or (220, 20, 60)
highLightColor = WHITE
heart1 = 'heart.jpg'
heart2 = 'heart2.jpg'
heart3 = 'heart3.jpg'
heart4 = 'heart4.jpg'
heart5 = 'heart5.jpg'
heart6 = 'heart6.jpg'
coverphoto = 'cover.jpg'
allSprites = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, xCoor, yCoor):
        super().__init__()
        pygame.init()
        self.image = pygame.image.load(coverphoto).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xCoor
        self.rect.y = yCoor
        self.revealed = False

    def randomize():
        mylist = [1, 1, 2, 2, 3, 3, 4 , 4, 5, 5, 6, 6]
        random.shuffle(mylist)
        board = []
        revealedImg = coverphoto
        for x in range(4):
            column = []
            for y in range(3):
                if mylist[0] == 1:
                    revealedImg = heart1
                elif mylist[0] == 2:
                    revealedImg = heart2
                elif mylist[0] == 3:
                    revealedImg = heart3
                elif mylist[0] == 4:
                    revealedImg = heart4
                elif mylist[0] == 5:
                    revealedImg = heart5
                else:
                    revealedImg = heart6
                collumb.append(revealedImg)




class Board:
    def __init__(self):
        pygame.init()
        self.width = windowWidth
        self.height = windowHeight
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption("Memory Puzzle")
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.screen.fill(BGColor)
        bg = pygame.Surface(self.screen.get_size()).convert()
        self.screen.blit(pygame.transform.scale(bg, (430,325)), (0,0))
        #images set up
        cover = pygame.image.load(coverphoto).convert_alpha()
        cover = pygame.transform.scale(cover, (100,100))
        #kiss = pygame.image.load(kissPic).convert_alpha()
        #kiss = pygame.transform.scale(kiss, (130,130))
        #draw sprites onto screen

        y = 0
        for row in range(3):
            x = 0
            for col in range(4):
                allSprites.add(Tile(x,y))
                #left = box_x * (boxSize + gapSize) + xMargin
                #top = box_y * (boxSize + gapSize) + yMargin
                x += 110
            y += 110

        allSprites.draw(self.screen)
        #cover.draw(self.screen)
        #kisses.draw(screen)
#        print()
#        allSprites.draw(screen)
#        hearts.blit()
#        kisses.blit()

        pygame.display.flip()
    def getAllSprites():
        return allSprites


#    def drawBoard(board):

         #background set up

def main():
    pygame.init()
    screen = Board()
    #screen.drawBoard()
    #screen = pygame.display.set_mode([600,400])
    cursorx = 0
    cursory = 0
    running = True
    totalClicks = 0
    while running:
        if (totalClicks == 20):
            running = False
            break
            #easygui.msgbox("You're out of time! Your score was " + score, title = "Game Over!")
        else:
            ev = pygame.event.get()
            numClicks = 0
            points = 0
            for event in ev:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    totalClicks += 1
                    numClicks += 1
                    pos = pygame.mouse.get_pos()
                    clicked_sprites = [s for s in allSprites if s.rect.collidepoint(pos)]
                    s = clicked_sprites[0]
                    if numClicks == 1:
                        temp = s
                        posit = pos
                    if numClicks == 2:
                        numClicks = 0
                        if temp == s:
                            points += 1
                            s.revealed = True
                            temp.revealed = True
                            revealedBoxes.add(s)
                            revealedBoxes.add(temp)

main()
