## tests/wordGame_tests.py
from nose.tools import *
import wordGame

wordGame.main()

def test_wordGame():
	setup_test()
	try:
	  do_test()
	finally:
		cleanup_after_test()


def setup_test():
	pass
		
def do_test():
	assert_true(True,str.isalpha(aGame.letter))
	assert_true(True,aGame.letter.length()==1)
	
def cleanup_after_test():
	pass
	
