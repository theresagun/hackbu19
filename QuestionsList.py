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
    def main():
        list = makeQuestions
        Question q1 = random.choice(list)
        list.remove(q1)
        Question q2 = random.choice(list)
        list.remove(q2)
        Question q3 = random.choice(list)
        list.remove(q3)
