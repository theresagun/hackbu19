class Question():
    def __init__(self,q, c, a):
        self.question = q
        self.choices = c
        self.correct = a
    def getQuestion(self):
        return self.question
    def getChoices(self):
        return self.choices
    def getAnswer(self):
        return self.answer
    def checkAnswer(self,choice):
        if(self.choice == question.correct):
            return true
        else:
            return false
