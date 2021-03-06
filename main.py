import pygame
import character
import time
import ticTacToe
import memorypuzzle


BLACK    = (0, 0, 0)
WHITE    = (255,255,255)
PINK = (255,105,180)

class Controller:
    def __init__(self, width=800, height=600):
        pygame.init()
        pygame.mixer.init()
        self.width=width
        self.height=height
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.caption=pygame.display.set_caption("MATCH MADE IN PYTHON")
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.girlPic="girl2.png"
        self.girl=pygame.image.load(self.girlPic).convert_alpha()
        self.boyPic="boy2.png"
        self.boy=pygame.image.load(self.boyPic).convert_alpha()
        self.character=character.Character(0, 0, self.girlPic, 0)
        self.score=0
        self.play=False
        self.lover="yourself"
        self.loverPic="zac.jpg"



    def startMenu(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end=False
                if event.type == pygame.KEYDOWN:
                    self.goToStory()
                    #self.endScreen()

            #set up background
            self.background = pygame.image.load("startScreen1.jpe")
            self.screen.blit(pygame.transform.scale(self.background, (800, 600)), (0,0))
            titleFont=pygame.font.SysFont("Calibri", 50, True, False)
            #title
            title=titleFont.render("MATCH MADE IN PYTHON", False, WHITE)
            self.screen.blit(title, (120,385))
            #go to story
            directionFont=pygame.font.SysFont("Calibri", 30)
            directions=directionFont.render("PRESS ANY KEY TO START!", False, WHITE)
            self.screen.blit(directions, (220,530))


            pygame.display.flip()

        pygame.quit()



    def goToStory(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end=False
                if event.type == pygame.KEYDOWN:
                    self.goToCharChoosing()
            self.background = pygame.Surface(self.screen.get_size()).convert()
            ##self.background=pygame.image.load("storyBackground1.jpg")
            self.screen.blit(pygame.transform.scale(self.background, (800, 600)), (0,0))
            #self.background.fill((0, 0, 0))

            file=open("story.txt", "r+")
            storyFont=pygame.font.SysFont("Lucida Handwriting", 23)
            storyFont1=pygame.font.SysFont("Calibri", 30)
            line1=storyFont.render(file.readline().strip(), False, WHITE)
            line2=storyFont.render(file.readline().strip(), False, WHITE)
            line3=storyFont.render(file.readline().strip(), False, WHITE)
            line4=storyFont.render(file.readline().strip(), False, WHITE)
            line5=storyFont.render(file.readline().strip(), False, WHITE)
            line6=storyFont1.render("PRESS ANY KEY TO TRY TO END YOUR LONELINESS", False, WHITE)

            self.screen.blit(line1, (0,10))
            self.screen.blit(line2, (120,100))
            self.screen.blit(line3, (0,190))
            self.screen.blit(line4, (580,280))
            self.screen.blit(line5, (0,370))
            self.screen.blit(line6, (85,500))

            self.background=pygame.image.load("deadRose.jpg")
            self.screen.blit(pygame.transform.scale(self.background, (100, 100)), (500,0))
            self.background=pygame.image.load("alone.png")
            self.screen.blit(pygame.transform.scale(self.background, (100, 100)), (0,70))
            self.background=pygame.image.load("appleEye.jpg")
            self.screen.blit(pygame.transform.scale(self.background, (150, 130)), (200,230))
            self.background=pygame.image.load("smallHeart.png")
            self.screen.blit(pygame.transform.scale(self.background, (50, 50)), (20,490))
            self.screen.blit(pygame.transform.scale(self.background, (50, 50)), (710,490))


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
                        self.character=character.Character(450, 70, self.girlPic, 0)
                        self.goToBoard()
                    if event.key==pygame.K_b:
                        self.character=character.Character(450,70, self.boyPic, 1)
                        self.goToBoard()

            #background set up
                self.background = pygame.Surface(self.screen.get_size()).convert()
                self.background=pygame.image.load("greyBack.jpg")
                self.screen.blit(pygame.transform.scale(self.background, (800, 600)), (0,0))


                #images to be used
                #self.girl=pygame.image.load(self.girlPic).convert_alpha()
                self.girl=pygame.transform.scale(self.girl, (150, 300))
                #self.boy=pygame.image.load(self.boyPic).convert_alpha()
                self.boy=pygame.transform.scale(self.boy, (150, 300))


                #blit images
                self.screen.blit(self.girl, (150,250))
                self.screen.blit(self.boy, (450,250))

                #fonts
                chooseFont=pygame.font.SysFont("Calibri", 65, True, False)
                charChoose=chooseFont.render("CHOOSE YOUR", False, BLACK)
                charChoose1=chooseFont.render("LONELY CHARACTER", False, BLACK)

                genderFont=pygame.font.SysFont("Calibri", 35, True, False)
                genderChooseg=genderFont.render("PRESS 'G' FOR ME!", False, BLACK)
                genderChooseb=genderFont.render("PRESS 'B' FOR ME!", False, BLACK)

                self.screen.blit(charChoose, (185,60))
                self.screen.blit(charChoose1, (125,150))
                self.screen.blit(genderChooseg, (95,560))
                self.screen.blit(genderChooseb, (410,560))


                pygame.display.flip()

        pygame.quit()



    def goToBoard(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    end=False
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.play=True

            self.screen=pygame.display.set_mode((1000, 700))

            white=pygame.image.load("white.jpg")
            white=pygame.transform.scale(white, (1000, 1000))
            self.screen.blit(white, (0,0))

            self.background=pygame.image.load(self.character.bgPic)
            self.screen.blit(pygame.transform.scale(self.background, (800, 550)), (100,75))

            #character
            self.characterIMG=pygame.transform.scale(self.character.image, (60, 90))
            self.screen.blit(self.characterIMG, (self.character.rect.x, self.character.rect.y))

            #Mystery pics & ranges
            if(self.character.gender==1):
                mysteryPeople=[ "mw2.jpg","mw1.jpg", "mw3.jpg"]
            else:
                mysteryPeople=["mm1.jpg", "mm2.jpg", "mm3.jpg"]

            mp1=pygame.image.load(mysteryPeople[0])
            mp2=pygame.image.load(mysteryPeople[1])
            mp3=pygame.image.load(mysteryPeople[2])
            self.screen.blit(pygame.transform.scale(mp1, (130, 100)), (250, 300))
            self.screen.blit(pygame.transform.scale(mp2, (150, 110)), (415, 300))
            self.screen.blit(pygame.transform.scale(mp3, (160, 100)), (610, 300))


            rangeFont=pygame.font.SysFont("Calibri", 25, True, False)
            rangeChoose1=rangeFont.render("0-2 points", False, BLACK)
            rangeChoose2=rangeFont.render("2-4 points", False, BLACK)
            rangeChoose3=rangeFont.render("4-6 points", False, BLACK)
            self.screen.blit(rangeChoose1, (270, 410))
            self.screen.blit(rangeChoose2, (445, 410))
            self.screen.blit(rangeChoose3, (630, 410))

            #score
            rangeFont1=pygame.font.SysFont("Calibri", 40, True, False)
            score=rangeFont1.render("Score: ", False, BLACK)
            scoreN=rangeFont1.render(str(self.score), False, PINK)
            self.screen.blit(score, (20, 20))
            self.screen.blit(scoreN, (135, 20))
            pressPlay=rangeFont.render("PRESS SPACE TO PLAY THE MINIGAME", False, BLACK)
            self.screen.blit(pressPlay, (300, 250))

            #flowers
            rose1=pygame.image.load("roses2.png")
            rose2=pygame.image.load("roses21.png")
            self.screen.blit(pygame.transform.scale(rose1, (230, 190)), (10, 500))
            self.screen.blit(pygame.transform.scale(rose2, (230, 190)), (760, 500))

            if(self.play==True and (self.character.position==0 or self.character.position==3)):
                self.character.position+=1
                self.score+=ticTacToe.main()
            elif(self.play==True and self.character.position==1):
                self.character.position+=1
                self.score+=memorypuzzle.main()
            elif(self.play==True and (self.character.position==2 or self.character.position==5 or self.character.position==4)):
                self.character.position+=1
                self.score+=ticTacToe.main()
            self.character.moveAhead()
            self.play=False

            if(self.score>=0 and self.score<=1):
                if(self.character.gender==0):
                    self.lover="Shrek"
                    self.loverPic="shrek.jpg"
                else:
                    self.lover="Fiona"
                    self.loverPic="fiona.jpg"
            elif(self.score>2 and self.score<=4):
                if(self.character.gender==0):
                    self.lover="Ed Sheeran"
                    self.loverPic="ed.jpg"
                else:
                    self.lover="Katy Perry"
                    self.loverPic="katy.jpg"
            elif(self.score>4 and self.score<=5):
                if(self.character.gender==0):
                    self.lover="Zac Efron"
                    self.loverPic="zac.jpg"
                else:
                    self.lover="Blake Lively"
                    self.loverPic="blake.jpg"


            if(self.character.position==5):
                self.endScreen()

            pygame.display.flip()

        pygame.quit()

    def endScreen(self):
        end=True
        while(end==True):
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    end=False
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.reset()
                        self.goToBoard()
            self.screen=pygame.display.set_mode((self.width, self.height-50))
            self.background=pygame.image.load("endScreen.jpg")
            self.screen.blit(pygame.transform.scale(self.background, (self.width, self.height-50)), (0,0))

            finalFont=pygame.font.SysFont("Calibri", 30, True, False)
            finalFont1=pygame.font.SysFont("Calibri", 20, True, False)
            ended=finalFont.render("You ended up with: ", False, BLACK)
            ended2=finalFont.render("Congrats, You cured your loneliness!", False, BLACK)
            ended1=finalFont.render(self.lover, False, BLACK)
            unhappy=finalFont1.render("If you're unhappy with your lover, press SPACE to try to find a better one", False, BLACK)
            disclaimer=finalFont1.render("Disclaimer: We are not responsible for any legal fees regarding divorce", False, BLACK)
            self.screen.blit(ended, (25,10))
            self.screen.blit(ended1, (275,10))
            self.screen.blit(ended2, (25,35))
            self.screen.blit(unhappy, (75, 355))
            self.screen.blit(disclaimer, (75, 380))
            lover=pygame.image.load(self.loverPic)
            self.screen.blit(pygame.transform.scale(lover, (230,250)), (440,100))
            self.screen.blit(pygame.transform.scale(self.character.image, (230,250)), (100,100))

            pygame.display.flip()

        pygame.quit()


    def reset(self):
        self.score=0
        self.character.position=0





def main():
    main_window=Controller()
    main_window.startMenu()

main()
