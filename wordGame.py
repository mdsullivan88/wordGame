## wordGame.py

import string
import random


class WordGame():

	def __init__(self):
		self.initVars()
		self.playGame()
		
	def initVars(self):
		self.letter = ''
		self.answer = ''
		self.keepPlaying = True
		self.correctAnswer = False
		self.quitNow = False
		self.numCorrect = 0
		self.numAttempted = 0
		self.score = 0.0
		
	def resetVars(self):
		self.letter = ''
		self.answer = ''
		self.correctAnswer = False
		
	def playGame(self):
		while self.keepPlaying:
			self.resetVars()
			self.pickLetter()
			while (not self.correctAnswer) and (not self.quitNow):
				self.askQuestion()
				self.checkAnswer()
				self.updateScore()
		self.calculateScore()
		self.printExitMessage()
		
	def pickLetter(self):
		self.letter = random.choice(string.ascii_lowercase);
	
	def askQuestion(self):
		self.answer = raw_input(self.genQuestion()+"\t >> ").strip().lower()
					 
	def checkAnswer(self):
		if self.answer=="xx":
			self.quitGame()
			return
		try:
		  if not self.firstLetterCorrect():
			  self.ansNotCorrect()
		  elif self.checkWordFile():
			  self.ansIsCorrect()
		  else:
			  self.ansNotCorrect()
		except IndexError:
		  print(self.genTypeSomethingError())
			
	def quitGame(self):
		self.quitNow = True
		self.keepPlaying = False

	def firstLetterCorrect(self):
		return self.answer[0]==self.letter
		
	def ansIsCorrect(self):
		self.correctAnswer = True
		print(self.genCorrectMsg())
		
	def ansNotCorrect(self):
		if not self.firstLetterCorrect():
			print(self.genFirstLetterError())
		else:
			print(self.genNotWordError())
##
	def genQuestion(self):
		return "\n\tBig "+self.letter.upper()+\
					 " little "+self.letter+\
					 ", what begins with "+self.letter+"?\r\n"
					 
	def genFirstLetterError(self):
		return "\n\t"+string.capwords(self.answer)+\
					 " doesn't begin with "+self.letter.upper()+"!"
	
	def genCorrectMsg(self):
		return "\n\tCorrect! Great job :)"
	
	def genNotWordError(self):
		return "\n\t"+string.capwords(self.answer)+\
					 " is not a word!"
					 
	def genTypeSomethingError(self):
		return "\n\tType something!"
##				 
	def checkWordFile(self):
		wordFileName = "words/lf/"+self.letter.upper()+" Words.txt"
		with open(wordFileName) as wordFile:
			words = wordFile.read().splitlines()
			for word in words:
				if self.answer==word.lower():
					return True
		return False
					 
	def updateScore(self):
		self.numAttempted = self.numAttempted + 1
		if self.correctAnswer:
			self.numCorrect = self.numCorrect + 1
			return
					 
	def calculateScore(self):
		if self.numAttempted==0:
			return
		else:
			self.score = float(self.numCorrect)/float(self.numAttempted)
					 
	def printExitMessage(self):
		print(self.genScoreMessage())
		print(self.genExitMessage())
		
	def genScoreMessage(self):
		return
	
	def genExitMessage(self):
		return
		
## run game					 
aGame = WordGame()
##