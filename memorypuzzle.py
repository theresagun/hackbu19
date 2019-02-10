#import easygui
import random, pygame, sys
from pygame.locals import *

windowWidth = 450 # size of window's width in pixels
windowHeight = 390 # size of windows' height in pixels
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
#totalClicks = 0


class Tile(pygame.sprite.Sprite):
    def __init__(self, xCoor, yCoor, screen):
        super().__init__()
        pygame.init()
        self.image = pygame.image.load(coverphoto).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xCoor
        self.rect.y = yCoor
        self.revealed = False
        self.revealedImg = pygame.image.load(heart1).convert_alpha()
        self.isClicked = False
        self.screen = screen
        for spr in allSprites:
            if spr.isClicked:
                spr.reveal(spr)



class Board:
    def __init__(self):
        pygame.init()
        self.width = windowWidth
        self.height = windowHeight
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption("Memory Puzzle")
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background = self.screen.fill(BGColor)
        bg = pygame.Surface(self.screen.get_size()).convert()
        self.screen.blit(pygame.transform.scale(bg, (0,0)), (0,0))
        #images set up
        cover = pygame.image.load(coverphoto).convert_alpha()
        cover = pygame.transform.scale(cover, (100,100))

        self.totalClicks = 0
        self.points = 0
        #kiss = pygame.image.load(kissPic).convert_alpha()
        #kiss = pygame.transform.scale(kiss, (130,130))
        #draw sprites onto screen

        y = 60
        for row in range(3):
            x = 10
            for col in range(4):
                allSprites.add(Tile(x,y, self.screen))
                x += 110
            y += 110

        allSprites.draw(self.screen)
        pygame.display.flip()


    def printClicks(self):
        #self.screen.fill(BGColor)
        Board()
        clicksFont = pygame.font.SysFont("Calibri", 20, True, False)
        clicks = clicksFont.render("Clicks Remaining: ", False, WHITE)
        clickvar = clicksFont.render(str(20- self.totalClicks),False, WHITE)
        self.screen.blit(clicks, (10,10))
        self.screen.blit(clickvar, (10,30))
        pygame.display.flip()

    def printPoints(self):
        Board()
        pointsFont = pygame.fint.SysFont("Calibri", 20, True, False)
        points = pointsFont.render("Points: ", False, WHITE)
        pointsvar = pointsFont.render(str(points), False, WHITE)
        self.screen.blit(points, (200,10))
        self.screen.blit(pointsvar, (200,30))
        pygame.display.flip()

    def getAllSprites(self):
        return allSprites

    def randomize(self):
        mylist = [1, 1, 2, 2, 3, 3, 4 , 4, 5, 5, 6, 6]
        random.shuffle(mylist)
        board = []
        revealedImg = coverphoto
        for spr in allSprites:
            if mylist[0] == 1:
                spr.revealedImg = heart1
            elif mylist[0] == 2:
                spr.revealedImg = heart2
            elif mylist[0] == 3:
                spr.revealedImg = heart3
            elif mylist[0] == 4:
                spr.revealedImg = heart4
            elif mylist[0] == 5:
                spr.revealedImg = heart5
            else:
                spr.revealedImg = heart6
        #    column.append(revealedImg)
            del mylist[0]

    def reveal(self,spr):
        reveal = pygame.image.load(spr.revealedImg).convert_alpha()
        reveal = pygame.transform.scale(reveal, (100,100)).convert_alpha()
        spr.screen.blit(pygame.transform.scale(reveal, (100,100)), (spr.rect.x, spr.rect.y))
        pygame.display.flip()

#    def drawBoard(board):

         #background set up

def main():
    pygame.init()
    screen = Board()
    screen.randomize()
    #screen.drawBoard()
    #screen = pygame.display.set_mode([600,400])
    cursorx = 0
    cursory = 0
    running = True
    #totalClicks = 0
    while running:
        if (screen.totalClicks == 20):
            running = False
            #totalClicks = 0
            break
            #easygui.msgbox("You're out of time! Your score was " + score, title = "Game Over!")
        else:
            ev = pygame.event.get()
            numClicks = 0
            for event in ev:
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    screen.totalClicks += 1
                    screen.printClicks()
                    numClicks += 1
                    pos = pygame.mouse.get_pos()
                    clicked_sprites = [s for s in allSprites if s.rect.collidepoint(pos)]
                    s = clicked_sprites[0]
                    #s.isClicked = True
                    screen.reveal(s)
                    if numClicks == 1:
                        temp = s
                        posit = pos
                    if numClicks == 2:
                        numClicks = 0
                        if temp == s:
                            screen.points += 1
                            s.isClicked = True
                            temp.isClicked = True
                            revealedBoxes.append(s)
                            revealedBoxes.append(temp)
                        else:
                            s.isClicked = False
                            temp.isClicked = False


main()
