import threading
import time
from getch import getch
import os
x=0
words="wordl"
def inmess(words):

	while x<1:
		
		print(2)
		key = getch()
		global charr
		charr=charr+key
		print(key)
		print(charr)
		words=charr
def catcher(words):
	c=0
	word=words

	while x<1:
		
		os.system('clear')
		print(str(c)+charr)
		time.sleep(2)
		c=c+1

out_thread = threading.Thread(target=catcher)

my_thread = threading.Thread(target=inmess)
out_thread.start()
my_thread.start()

