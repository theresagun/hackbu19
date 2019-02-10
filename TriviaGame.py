import pygame,sys,pygbutton,random
from pygame.locals import *
import Question

#setting up the background_position
pygame.init()
screen = pygame.display.set_mode([1048,800])
pygame.display.set_caption('Trivia Game')
background = pygame.image.load("heartBackground.png").convert()
background_position = [0,0]
screen.blit(background,background_position)
pygame.display.flip()

#make questions
import Question
class QuestionsList:
    def makeQuestions():
        Question[] quest = new Question[14]
        file = open('text.txt', 'r')
        i = 0
        while(file.hasNext()):
            q = file.readline()
            String[] c = new String[4]
            c[0] = file.readline()
            c[1] = file.readline()
            c[2] = file.readline()
            c[3] = file.readline()
            a = file.readline()
            quest[i] = new Question(q,c,a)
            i++
        return quest
    def tester():
        score = 0
        list = makeQuestions()
        Question[] qs;
        qs[0]= random.choice(list)
        list.remove(qs[0])
        qs[2] = random.choice(list)
        list.remove(qs[2])
        Question qs[3] = random.choice(list)
        list.remove(qs[3])
        for(int i = 0; i < qs.length(); i++):
            question = pygbutton.PygButton((100,40,200,30),qs[i].getQuestion())
            tester2 = pygbutton.PygButton((100,70,200,30),'Click Here')
            choice1 = pygbutton.PygButton((100,110,200,30),(qs[i].getChoices()).get(0))
            choice2 = pygbutton.PygButton((100,150,200,30),(qs[i].getChoices()).get(1))
            choice3 = pygbutton.PygButton((100,190,200,30),(qs[i].getChoices()).get(2))
            choice4 = pygbutton.PygButton((100,230,200,30),(qs[i].getChoices()).get(3))

            question.draw(screen)
            tester2.draw(screen)
            choice1.draw(screen)
            choice2.draw(screen)
            choice3.draw(screen)
            choice4.draw(screen)
            buttonEvent = choice1.handleEvent(event)
            buttonEvent2= choice2.handleEvent(event)
            buttonEvent3= choice3.handleEvent(event)
            buttonEvent4= choice4.handleEvent(event)

            if('click' in buttonEvent):
                if(choice1 == qs[i].getAnswer()):
                    winner = pygbutton.PygButton((500,190,200,30),'Good Job')
                    score = score+1
                else:
                     winner = pygbutton.PygButton((500,190,200,30),'Nope')
                winner.draw(screen)
            if 'click' in buttonEvent2 :
                if(choice2 == qs[i].getAnswer()):
                    winner = pygbutton.PygButton((500,190,200,30),'Good Job')
                    score = score+1
                    winner.draw(screen)
                else:
                     winner = pygbutton.PygButton((500,190,200,30),'Nope')
                     winner.draw(screen)
        if 'click' in buttonEvent3 :
                if(choice3 == qs[i].getAnswer()):
                    winner = pygbutton.PygButton((500,190,200,30),'Good Job')
                    score = score+1
                    winner.draw(screen)
                else:
                     winner = pygbutton.PygButton((500,190,200,30),'Nope')
                     winner.draw(screen)
        if 'click' in buttonEvent4 :
                if(choice4 == qs[i].getAnswer()):
                    winner = pygbutton.PygButton((500,190,200,30),'Good Job')
                    score = score+1
                    winner.draw(screen)
                else:
                     winner = pygbutton.PygButton((500,190,200,30),'Nope')
                     winner.draw(screen)

        question.draw(screen)
        tester2.draw(screen)
        choice1.draw(screen)
        choice2.draw(screen)
        choice3.draw(screen)
        choice4.draw(screen)

    def main():
        while True:
        for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

    tester_Function()

    pygame.display.update()
