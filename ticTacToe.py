import pygame
import sys
import random

#WHITE = (255, 255, 255)
PLAYER_WIN = 1
NPC_WIN = 0
TIE = 0

class Heart(pygame.sprite.Sprite):
    '''
    This class represents the hearts in the tic tac toe board.
    Derives from the Sprite class in Pygame.
    '''
    def __init__(self, xCoor, yCoor, image):
        '''
        Constructor. Pass in x, y, image file name.
        '''
        #parent constructor
        super().__init__()
        #create image
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (130,130)).convert_alpha()
        #get rectangle object
        self.rect = self.image.get_rect()
        #set coordinates
        self.rect.x = xCoor
        self.rect.y = yCoor

class Kiss(pygame.sprite.Sprite):
    '''
    This class represents the kisses in the tic tac toe board.
    Derives from the Sprite class in Pygame.
    '''
    def __init__(self, xCoor, yCoor, image):
        '''
        Constructor. Pass in x, y, image file name.
        '''
        #parent constructor
        super().__init__()
        #create image
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (130,130)).convert_alpha()
        #get rectangle object
        self.rect = self.image.get_rect()
        #set coordinates
        self.rect.x = xCoor
        self.rect.y = yCoor

class Background(pygame.sprite.Sprite):
    '''
    This class represents the background.
    Derives from the Sprite class in Pygame.
    '''
    def __init__(self, imageFile, loc):
        '''
        Constructor. Pass in name of image file and location.
        '''
        #parent constructor
        super().__init__()
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def main():
    #initialize pygame lib
    pygame.init()
    #create 400x400 screen
    screen = pygame.display.set_mode([400,400])
    #create surface
    bg = pygame.Surface(screen.get_size()).convert()

    #load images
    heartPic = 'pinkHeart.png'
    kissPic = 'lips.png'


    #create sprite groups
    hearts = pygame.sprite.Group()
    kisses = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()

    #make kiss sprites for comp to use
    kissNPC = pygame.sprite.Group()

    #create hearts and kisses
    y = 0
    for row in range(3):
        x = 0
        for col in range(3):
            allSprites.add(Heart(x,y,heartPic))
            kissy = Kiss(x,y,kissPic)
            allSprites.add(kissy)
            kissNPC.add(kissy)

            x += 133
        y += 133

    heartsTurn = True
    end = -1
    #main loop
    while end == -1:
        #set background to white
        screen.fill([255,255,255])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                #get position of mouse, clicked = list of all sprites under cursor
                pos = pygame.mouse.get_pos()
                clicked = [s for s in allSprites if s.rect.collidepoint(pos)]
                #check if spot already clicked by either hearts or kisses
                hCol = []
                kCol = []
                for s in clicked:
                    hCol.append(pygame.sprite.spritecollide(s,hearts,dokill=False))
                    kCol.append(pygame.sprite.spritecollide(s,kisses,dokill=False))
                #if not clicked
                if(hCol == [[],[]] and kCol == [[],[]]):
                    #find heart sprite and add to group
                    for s in clicked:
                        if type(s) == Heart:
                            hearts.add(s)
                            s.onScreen = True
                heartsTurn = False

            elif event.type == pygame.MOUSEMOTION:
                if not heartsTurn:
                    kissList = kissNPC.sprites()
                    while not heartsTurn:
                        kissSpr = kissList[random.randint(0,len(kissList)-1)]
                        collisions = pygame.sprite.spritecollide(kissSpr,hearts,dokill=False)
                        if(collisions == []):
                            #add kiss to group
                            kisses.add(kissSpr)
                            kissNPC.remove(kissSpr)
                            heartsTurn = True


        #check when there are three kisses in a row/diagonal/column
        kissList = kisses.sprites()
        posListK = []
        for k in kissList:
            posListK.append((k.rect.x,k.rect.y))
        if((((0,0) in posListK) and ((0,133) in posListK) and ((0,266) in posListK)) or \
        (((0,0) in posListK) and ((133,0) in posListK) and ((266,0) in posListK)) or \
        (((133,0) in posListK) and ((133,133) in posListK) and ((133,266) in posListK)) or \
        (((0,133) in posListK) and ((133,133) in posListK) and ((266,133) in posListK)) or \
        (((266,0) in posListK) and ((266,133) in posListK) and ((266,266) in posListK)) or\
        (((0,266) in posListK) and ((133,266) in posListK) and ((266,266) in posListK)) or\
        (((0,0) in posListK) and ((133,133) in posListK) and ((266,266) in posListK)) or\
        (((0,266) in posListK) and ((133,133) in posListK) and ((266,0) in posListK))):
#            return NPC_WIN
            end = NPC_WIN


        #check when there are three hearts in a row/diagonal/column
        heartList = hearts.sprites()
        posListH = []
        for h in heartList:
            posListH.append((h.rect.x,h.rect.y))
        if((((0,0) in posListH) and ((0,133) in posListH) and ((0,266) in posListH)) or\
        (((0,0) in posListH) and ((133,0) in posListH) and ((266,0) in posListH)) or\
        (((133,0) in posListH) and ((133,133) in posListH) and ((133,266) in posListH)) or\
        (((0,133) in posListH) and ((133,133) in posListH) and ((266,133) in posListH)) or\
        (((266,0) in posListH) and ((266,133) in posListH) and ((266,266) in posListH)) or\
        (((0,266) in posListH) and ((133,266) in posListH) and ((266,266) in posListH)) or\
        (((0,0) in posListH) and ((133,133) in posListH) and ((266,266) in posListH)) or\
        (((0,266) in posListH) and ((133,133) in posListH) and ((266,0) in posListH))):
#            return PLAYER_WIN
            end = PLAYER_WIN

        #check if all tiles filled
        if(((0,0) in posListH or (0,0) in posListK) and ((0,133) in posListH or (0,133) in posListK) and\
        ((0,266) in posListH or (0,266) in posListK) and ((133,0) in posListH or (133,0) in posListK) and\
        ((133,133) in posListH or (133,133) in posListK) and ((133,266) in posListH or (133,266) in posListK) and\
        ((266,0) in posListH or (266,0) in posListK) and ((266,133) in posListH or (266,133) in posListK) and\
        ((266,266) in posListH or (266,266) in posListK)):
#            return TIE
            end = TIE

        #background set up
        bg = pygame.Surface(screen.get_size()).convert()
        bg = pygame.image.load('ticTacToeBoard.png')
        screen.blit(pygame.transform.scale(bg, (400,400)), (0,0))
        #images set up
        heart = pygame.image.load(heartPic).convert_alpha()
        heart = pygame.transform.scale(heart, (130,130))
        kiss = pygame.image.load(kissPic).convert_alpha()
        kiss = pygame.transform.scale(kiss, (130,130))
        #draw sprites onto screen
        hearts.draw(screen)
        kisses.draw(screen)

        pygame.display.flip()
    kateSmells = True
    while(kateSmells):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kateSmells = False
        #make screen
        screen = pygame.display.set_mode([400,400])
        screen.fill([255,105,180])

        #words!
        endFont = pygame.font.SysFont('Calibri',40,True,False)
        if end == PLAYER_WIN:
            endFont = endFont.render('YOU WON', False, (255,255,255))
        elif end == NPC_WIN:
            endFont = endFont.render('YOU LOST', False, (255,255,255))
        else:
            endFont = endFont.render('TIE GAME', False, (255,255,255))
        #put on screen
        width = endFont.get_width()
        wCoor = (400 - width) / 2
        height = endFont.get_height()
        hCoor = (400 - height) / 2
        screen.blit(endFont, (wCoor,hCoor))

        pygame.display.flip()

main()
