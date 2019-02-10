import pygame
import sys

white = (255, 255, 255)

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
        #create image w/ width and height
#        self.height = 130
#        self.width = 130
#        self.image = pygame.Surface([self.width,self.height])
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (130,130)).convert_alpha()
        #get rectangle object
        self.rect = self.image.get_rect()
        #set coordinates
        self.rect.x = xCoor
        self.rect.y = yCoor
        #put image on screen
#        pygame.Surface.blit('pinkHeart.png',screen,self.rect)
        #change to true when blit
        self.onScreen = False

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
        #create image w/ width and height
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (130,130)).convert_alpha()

#        self.image = pygame.Surface(130,130)
        #get rectangle object
        self.rect = self.image.get_rect()
        #set coordinates
        self.rect.x = xCoor
        self.rect.y = yCoor
        #put image on screen
#        pygame.Surface.blit('lips.png',screen,self.rect)
        #change to true when blit
        self.onScreen = False


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
#    background = pygame.Surface(screen.get_size())
    #load image
    #bg = Background('ticTacToeBoard.png', [0,0])
    bg = pygame.Surface(screen.get_size()).convert()
    ###potentially next two lines go in while loop
    #set background to white
#    screen.fill([255,255,255])
    #blit background
#    screen.blit(bg.image, bg.rect)

    #load images
    heartPic = 'pinkHeart.png'
    kissPic = 'lips.png'


    #create sprite lists
    hearts = pygame.sprite.Group()
    kisses = pygame.sprite.Group()
    allSprites = pygame.sprite.Group()
#    sprites.add(hearts)
#    sprites.add(kisses)

    #make kiss sprites for comp to use
    kissNPC = pygame.sprite.Group()
    #create hearts and kisses
#    heart1 = Heart(130,0,screen,heartPic)
#    x = 0
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
    #game outcomes
    gameOver = False
    playerWin = False
    computerWin = False
    tie = False

    #whose turn - update this at end of loop
    heartsTurn = True

    #main loop
    while True:
        #set background to white
        screen.fill([255,255,255])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #if not player's turn
            if not heartsTurn:
                #TODO make npc
                print("not ur turn")
                print(kissNPC.sprites())
                heartsTurn = True
            #if player's turn
            elif event.type == pygame.MOUSEBUTTONUP:
                #get position of mouse, clicked = list of all sprites under cursor
                pos = pygame.mouse.get_pos()
                clicked = [s for s in allSprites if s.rect.collidepoint(pos)]
                #check if spot already clicked by either hearts or kisses
                print(clicked)
                hCol = []
                kCol = []
                for s in clicked:
#                    print("in for loop")
                    hCol.append(pygame.sprite.spritecollide(s,hearts,dokill=False))
#                    print(hCol)
                    kCol.append(pygame.sprite.spritecollide(s,kisses,dokill=False))
#                    print(kCol)
                #if not clicked
                if(hCol == [[],[]] and kCol == [[],[]]):
#                    print("in if")
                    #if hearts turn - might not need this, can check earlier if hearts
#                    if heartsTurn:
                    #find heart sprite and add to group
                    for s in clicked:
                        if type(s) == Heart:
                            hearts.add(s)
                            s.onScreen = True
                heartsTurn = False
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
#        print()
#        allSprites.draw(screen)
#        hearts.blit()
#        kisses.blit()

        pygame.display.flip()

main()
