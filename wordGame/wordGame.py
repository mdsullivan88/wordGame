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
		self.isAnswerCorrect = False
		self.quitNow = False
		self.numCorrect = 0
		self.numAttempted = 0
		self.score = 0.0
		
	def playGame(self):
		while self.keepPlaying:
			self.resetVars()
			self.letter = self.pickLetter()
			while (not self.isAnswerCorrect) and (not self.quitNow):
				self.answer = self.askQuestion(self.letter)
				self.isAnswerCorrect = self.checkAnswer(self.letter,self.answer)
				self.numCorrect,self.numAttempted = self.updateScore(self.answer,
																														 self.isAnswerCorrect,
																														 self.numCorrect,
																														 self.numAttempted)
		self.score = self.calculateScore(self.numCorrect,self.numAttempted)
		self.printExitMessage(self.numCorrect,self.numAttempted,self.score)
		
	def resetVars(self):
		self.letter = ''
		self.answer = ''
		self.isAnswerCorrect = False
		
	def pickLetter(self):
		return random.choice(string.ascii_lowercase);
	
	def askQuestion(self,letter):
		return raw_input(self.genQuestion(letter)+"\t >> ").strip().lower()
					 
	def checkAnswer(self,letter,answer):
		if answer=="xx":
			self.quitGame()
			return
		try:
			if not answer[0]==letter:
				print(self.genFirstLetterError(answer))
				return False
			elif self.checkWordFile(letter,answer):
				print(self.genCorrectMsg())
				return True
			else:
				print(self.genNotWordError(answer))
				return False
		except IndexError:
		  print(self.genTypeSomethingError())
			
	def quitGame(self):
		self.quitNow = True
		self.keepPlaying = False
##
	def genQuestion(self,letter):
		return "\n\tBig "+letter.upper()+\
					 " little "+letter+\
					 ", what begins with "+letter+"?\r\n"
					 
	def genFirstLetterError(self,answer):
		return "\n\t"+string.capwords(str(answer))+\
					 " doesn't begin with "+self.letter.upper()+"!"
	
	def genCorrectMsg(self):
		return "\n\tCorrect! Great job :)"
	
	def genNotWordError(self,answer):
		return "\n\t"+string.capwords(str(answer))+\
					 " is not a word!"
					 
	def genTypeSomethingError(self):
		return "\n\tType something!"
##				 
	def checkWordFile(self,letter,answer):
		wordFileName = "words/lf/"+letter.upper()+" Words.txt"
		with open(wordFileName) as wordFile:
			words = wordFile.read().splitlines()
			for word in words:
				if answer==word.lower():
					return True
		return False
					 
	def updateScore(self,answer,isAnswerCorrect,correct,attempted):
		if answer=='xx':
			return correct, attempted
		else:
			attempted = attempted + 1
		if isAnswerCorrect:
			correct = correct + 1
		return attempted, correct
					 
	def calculateScore(self,correct,attempted):
		if self.numAttempted==0:
			return 0.0
		else:
			return float(correct)/float(attempted)
					 
	def printExitMessage(self,correct,attempted,score):
		print(self.genScoreMessage(correct,attempted,score))
		print(self.genExitMessage())
		
	def genScoreMessage(self,correct,attempted,score):
		return "\n\tYour score: {0:d}/{1:d} ({2:03.2f}%)".format(correct,
																														 attempted,
																														 score*100.0)
	
	def genExitMessage(self):
		return "\tGreat job! :)\n"

		
## run game
def main():
	aGame = WordGame()
##
if __name__=='__main__':			 
	main()
##