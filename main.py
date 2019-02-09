import pygame
import character

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

class Controller:
    def __init__(self, width=800, height=600):
        pygame.init()
        pygame.mixer.init()
        self.width=width
        self.height=height
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.caption=pygame.display.set_caption("MATCH MADE IN PYTHON")
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.girlPic="girl1.png"
        self.boyPic="boy1.png"
        self.character=character.Character(400, 100, self.girlPic, 0)



    def startMenu(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end=False
                if event.type == pygame.KEYDOWN:
                    self.goToStory()

            #set up background
            self.background = pygame.image.load("startScreen1.jpe")
            self.screen.blit(pygame.transform.scale(self.background, (800, 600)), (0,0))
            titleFont=pygame.font.SysFont("Calibri", 50, True, False)
            #title
            title=titleFont.render("MATCH MADE IN PYTHON", False, WHITE)
            self.screen.blit(title, (80,385))
            #go to story
            directionFont=pygame.font.SysFont("Calibri", 30)
            directions=directionFont.render("PRESS ANY KEY TO START!", False, WHITE)
            self.screen.blit(directions, (200,530))


            pygame.display.flip()

        pygame.quit()



    def goToStory(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.goToCharChoosing()
            self.background = pygame.Surface(self.screen.get_size()).convert()
            self.background=pygame.image.load("storyBackground1.jpg")
            self.screen.blit(pygame.transform.scale(self.background, (800, 600)), (0,0))
            self.background.fill((0, 0, 0))
            pygame.display.flip()

        pygame.quit()


    def goToCharChoosing(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        self.girl
                        self.character=character.Character(400, 100, self.girlPic, 0)
                        self.goToBoard()
                    if event.key==pygame.K_b:
                        self.character=character.Character(400,100, self.boyPic, 1)
                        self.goToBoard()


            #background set up
                self.background = pygame.Surface(self.screen.get_size()).convert()
                self.background=pygame.image.load("greyBack.jpg")
                self.screen.blit(pygame.transform.scale(self.background, (800, 600)), (0,0))


                #images to be used
                self.girl=pygame.image.load(self.girlPic).convert_alpha()
                self.girl=pygame.transform.scale(self.girl, (150, 300))
                self.boy=pygame.image.load(self.boyPic).convert_alpha()
                self.boy=pygame.transform.scale(self.boy, (150, 300))

                #blit images
                self.screen.blit(self.girl, (150,250))
                self.screen.blit(self.boy, (450,250))

                #fonts
                chooseFont=pygame.font.SysFont("Calibri", 65, True, False)
                charChoose=chooseFont.render("CHOOSE YOUR", False, BLACK)
                charChoose1=chooseFont.render("LONELY CHARACTER", False, BLACK)
                self.screen.blit(charChoose, (200,60))
                self.screen.blit(charChoose1, (125,150))



                pygame.display.flip()



        pygame.quit()



    def goToBoard(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    end=False
            self.background=pygame.image.load("heart.gif")
            self.screen.blit(pygame.transform.scale(self.background, (800, 600)), (0,0))
            self.background.fill((0, 0, 0))
            pygame.display.flip()

        pygame.quit()



def main():
    main_window=Controller()
    main_window.startMenu()

main()
