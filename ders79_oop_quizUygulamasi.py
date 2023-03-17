# Question class ı
# Quiz class ı dışardan question ları alıcak
# adlığı sorulara göre sırayla soruları kullanıcıya göstericek
# sorulara cevap vericez skor bilgisi tutcaz en son skoru yazdırcaz

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    # gelen cevapla gerçek cevabı karşılaştırır, true yada false döndürür
    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    # dizinin indexinden nesneyi alır
    def getQuestions(self):
        return self.questions[self.questionIndex]

    # soruyu ve şıkları gösterir
    def displayQuestion(self):
        question = self.getQuestions()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for p in question.choices:
            print('- '+ p)

        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    # cevabı kontrol eder
    def guess(self, answer):
        question = self.getQuestions()
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    # kontrol fonksiyonu
    def loadQuestion(self):
        if self.questionIndex == len(self.questions):
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()    

    # score gösterir
    def showScore(self):
        print(f'score: {self.score}')    

    # yıldızlı başlık
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        if questionNumber > totalQuestion:
            print('quiz bitti')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))


q1 = Question('iclerinden en iyi bilimkurgu kitabi hangisidir?', ['marsli', 'vakif serisi', 'alacakaranlik serisi', 'ince memet serisi'], 'vakif serisi')
q2 = Question('iclerinden en ergen bilimkurgu kitabi hangisidir?', ['marsli', 'vakif serisi', 'alacakaranlik serisi', 'ince memet serisi'], 'vakif serisi')
q3 = Question('iclerinden en son cikan bilimkurgu kitabi hangisidir?', ['marsli', 'vakif serisi', 'alacakaranlik serisi', 'ince memet serisi'], 'vakif serisi')

questions = [q1,q2,q3]
quiz = Quiz(questions)
quiz.loadQuestion()

