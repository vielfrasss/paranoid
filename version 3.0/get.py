from getch import getch, pause
import os
forever=0
#global word
words=""
print ('набираемое сообщение:')
def catcher():
	global words
	os.system('clear')
	print ('набираемое сообщение:', words)

	key = getch()

	if ord(key) == 13:
		print( "enter") 
		words = ""
	elif ord(key) == 127:
		
		words=words[:-1]
		print ('набираемое сообщение:', words)
	else :
		
		words =word+ key
		print ('набираемое сообщение:', words)
word=""		
while forever < 1 :
	word=words
	
	catcher()
	
