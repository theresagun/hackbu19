import pygame,sys,pygbutton,random
from pygame.locals import *
from Question import Question
import os

#setting up the background
class TriviaGame:
	def __init__(self):
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
		i = 0
		while(i < 83):
			q = file.readline()
			c = []
			c.append(file.readline())
			c.append(file.readline())
			c.append(file.readline())
			c.append(file.readline())
			a = file.readline()
			quest.append(Question(q,c,a))
			i += 1
		return quest
	def tester(self, event1):
		#pygame.init()
		end = True
		while(end==True):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end=False
				if event.type == pygame.MOUSEBUTTONUP:
					self.goToScore()
					self.play = True
			self.screen=pygame.display.set_mode((1000, 700))

			background=pygame.Surface(self.screen.get_size())
			background=pygame.image.load("heartBackground.png")
			self.background=pygame.transform.scale(background, (1000, 1000))
			self.screen.blit(self.background, (0,0))

			list = self.makeQuestions()
			qs = [];
			qs.append(random.choice(list))
			list.remove(qs[0])
			qs.append(random.choice(list))
			list.remove(qs[1])
			qs.append(random.choice(list))
			list.remove(qs[2])
			for x in qs:
				print(x.getChoices()[0])
				#question = pygbutton.PygButton((100,40,700,30),x.getQuestion())
				choice1 = pygbutton.PygButton((100,110,400,30),x.getChoices()[0])
				choice2 = pygbutton.PygButton((100,150,400,30),x.getChoices()[1])
				choice3 = pygbutton.PygButton((100,190,400,30),x.getChoices()[2])
				choice4 = pygbutton.PygButton((100,230,400,30),x.getChoices()[3])

				#question.draw(self.screen)
				questionFont = pygame.font.SysFont("Calibri", 25, True, False)
				question = questionFont.render(x.getQuestion(), False, (255,255,255))
				self.screen.blit(question, (700, 30))
				choice1.draw(self.screen)
				choice2.draw(self.screen)
				choice3.draw(self.screen)
				choice4.draw(self.screen)
				buttonEvent = choice1.handleEvent(event1)
				buttonEvent2= choice2.handleEvent(event1)
				buttonEvent3= choice3.handleEvent(event1)
				buttonEvent4= choice4.handleEvent(event1)
			pygame.quit()

		def	goToScore(self):
			end = True
			while(end==True):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						end=False
					if event.type == pygame.MOUSEBUTTONUP:
						if (self.answered < 3):
							self.tester()
							self.play = True
						else:
							self.play = False
							self.endScreen()
				self.screen=pygame.display.set_mode((1000, 700))
				winner = pygbutton.PygButton((500,190,200,30),'')
				if('click' in buttonEvent):
					if(choice1 == x.getAnswer()):
						winner = pygbutton.PygButton((500,190,200,30),'Good Job')
						self.score = self.score+1
						winner.draw(self.screen)
					else:
						winner = pygbutton.PygButton((500,190,200,30),'Nope')
						winner.draw(self.screen)
				elif 'click' in buttonEvent2 :
					if(choice2 == x.getAnswer()):
						winner = pygbutton.PygButton((500,190,200,30),'Good Job')
						self.score = self.score+1
						winner.draw(self.screen)
					else:
						winner = pygbutton.PygButton((500,190,200,30),'Nope')
						winner.draw(self.screen)
				elif 'click' in buttonEvent3 :
					if(choice3 == x.getAnswer()):
						winner = pygbutton.PygButton((500,190,200,30),'Good Job')
						self.score = self.score+1
						winner.draw(self.screen)
					else:
						winner = pygbutton.PygButton((500,190,200,30),'Nope')
						winner.draw(self.screen)
				elif 'click' in buttonEvent4 :
					if(choice4 == x.getAnswer()):
						winner = pygbutton.PygButton((500,190,200,30),'Good Job')
						self.score = self.score+1
						winner.draw(self.screen)
					else:
						winner = pygbutton.PygButton((500,190,200,30),'Nope')
						winner.draw(self.screen)
				winner.draw(self.screen)
				titleFont=pygame.font.SysFont("Calibri", 50, True, False)
				title=titleFont.render("Valentine's Day Trivia", False, (255,255,255))
				self.screen.blit(title, (300,300))
			pygame.display.flip()
		pygame.quit()


def main():
	main_window = TriviaGame()
	main_window.startMenu()
	#sys.exit()
main()
