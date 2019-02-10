import pygame,sys,pygbutton,random
from pygame.locals import *
from Question import Question
import os

#setting up the background
class TriviaGame(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((1048,800))
		self.caption = pygame.display.set_caption('Trivia Game')
		self.background = pygame.image.load("heartBackground.png")
		self.score = 0
		self.play = False
		self.answered = 0
		background_position = [0,0]
		self.screen.blit(self.background,background_position)
		pygame.display.flip()

	def startMenu(self):
		end = True
		while(end == True):
			for event in pygame.event.get():
				if(event.type == pygame.QUIT):
					end = False
				if(event.type == pygame.MOUSEBUTTONUP):
					self.tester(event)

			self.screen.blit(pygame.transform.scale(self.background, (1048, 800)), (0,0))
			titleFont=pygame.font.SysFont("Calibri", 50, True, False)
			title=titleFont.render("Valentine's Day Trivia", False, (255,255,255))
			self.screen.blit(title, (300,300))
			directionFont=pygame.font.SysFont("Calibri", 30)
			directions=directionFont.render("CLICK HERE TO START!", False, (255,255,255))
			self.screen.blit(directions, (400,400))
			pygame.display.flip()
		pygame.quit()

	def makeQuestions(self):
		quest = []
		try:
			file = open('text.txt', 'r')
		except FileNotFoundException :
			print("file not found!")
			exit()
		q = file.readline()
		c = []
		c.append(file.readline())
		c.append(file.readline())
		c.append(file.readline())
		c.append(file.readline())
		a = file.readline()
		quest.append(Question(q,c,a))
		q = file.readline()
		c = []
		c.append(file.readline())
		c.append(file.readline())
		c.append(file.readline())
		c.append(file.readline())
		a = file.readline()
		quest.append(Question(q,c,a))
		q = file.readline()
		c = []
		c.append(file.readline())
		c.append(file.readline())
		c.append(file.readline())
		c.append(file.readline())
		a = file.readline()
		quest.append(Question(q,c,a))
		return quest
	def tester(self, event1):
		#pygame.init()

			self.screen=pygame.display.set_mode((1000, 700))

			#background=pygame.Surface(self.screen.get_size())
			background=pygame.image.load("heartBackground.png")
			background=pygame.transform.scale(background, (1000,700))
			self.screen.blit(background, (0,0))
			print("HEY IM IN HERE")

			qs = self.makeQuestions()
			for x in qs:
				end = True
				while(end==True):
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							exit()
						if event.type == pygame.MOUSEBUTTONUP:
							if (self.answered < 3):
								self.play = True
							else:
								self.play = False
								self.endScreen()
					choice1 = pygbutton.PygButton((300,110,400,30),x.getChoices()[0])
					choice2 = pygbutton.PygButton((300,150,400,30),x.getChoices()[1])
					choice3 = pygbutton.PygButton((300,190,400,30),x.getChoices()[2])
					choice4 = pygbutton.PygButton((300,230,400,30),x.getChoices()[3])
					winner = pygbutton.PygButton((500,190,200,30),'')

					questionFont = pygame.font.SysFont("Calibri", 25, True, False)
					question = questionFont.render(x.getQuestion(), False, (0,0,0))
					self.screen.blit(question, (100, 30))
					choice1.draw(self.screen)
					choice2.draw(self.screen)
					choice3.draw(self.screen)
					choice4.draw(self.screen)
					buttonEvent = choice1.handleEvent(event1)
					buttonEvent2= choice2.handleEvent(event1)
					buttonEvent3= choice3.handleEvent(event1)
					buttonEvent4= choice4.handleEvent(event1)
					if('click' in buttonEvent):
						if(choice1 == x.getAnswer()):
							winner = pygbutton.PygButton((500,190,200,30),'Good Job')
							self.score = self.score+1
							winner.draw(self.screen)
							self.answered +=1;

						else:
							winner = pygbutton.PygButton((500,190,200,30),'Nope')
							winner.draw(self.screen)
					elif 'click' in buttonEvent2 :
						if(choice2 == x.getAnswer()):
							winner = pygbutton.PygButton((500,190,200,30),'Good Job')
							self.score = self.score+1
							winner.draw(self.screen)
							self.answered +=1;

						else:
							winner = pygbutton.PygButton((500,190,200,30),'Nope')
							winner.draw(self.screen)
					elif 'click' in buttonEvent3 :
						if(choice3 == x.getAnswer()):
							winner = pygbutton.PygButton((500,190,200,30),'Good Job')
							self.score = self.score+1
							winner.draw(self.screen)
							self.answered +=1;

						else:
							winner = pygbutton.PygButton((500,190,200,30),'Nope')
							winner.draw(self.screen)
					elif 'click' in buttonEvent4 :
						if(choice4 == x.getAnswer()):
							winner = pygbutton.PygButton((500,190,200,30),'Good Job')
							self.score = self.score+1
							winner.draw(self.screen)
							self.answered +=1;

						else:
							winner = pygbutton.PygButton((500,190,200,30),'Nope')
							winner.draw(self.screen)
					#winner.draw(self.screen)
					pygame.display.flip()



	def endScreen(self):
		end=True
		while(end==True):
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					exit()

			self.screen=pygame.display.set_mode((1000, 700))
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




def main():
	main_window = TriviaGame()
	main_window.startMenu()
	#sys.exit()
main()
