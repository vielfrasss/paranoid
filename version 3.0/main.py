from pyrogram import Client
from pyrogram.api import functions
import config

id=config.api_id
hash=config.api_hash
proxy=config.proxy
app = Client(session_name="example" , api_id=id ,api_hash=hash,proxy=proxy)
from getch import getch, pause
import os
forever=0
global words
words=""
global word
word=""
print ('набираемое сообщение:')
def catcher(us):
	global words
	os.system('clear')
	print ('набираемое сообщение:', words)

	key = getch()

	if ord(key) == 13:
		print( "enter")
		app.send_message(us,words) 
		words = ""
	elif ord(key) == 127:
		
		words=words[:-1]
		print ('набираемое сообщение:', words)
	else :
		
		words =word+ key
		print ('набираемое сообщение:', words)
	
	


app.start() 
#_____sendmessage_______
smsuser=input("username/1351754478: ")
if smsuser=='me':
	smguser= 'me'
if smsuser[:1]=='@':
	smguser=smsuser[1:]
else :
    smguser=int(smsuser)  
print(app.get_history(smguser,0,1))
#print(app.get_chat(smguser))
print(smguser)

while forever < 1 :
	word=words
	us=smguser
	catcher(us)
    #smgtext=input("message: ")
    #print(smgtext)
    #app.send_message(smguser,smgtext)
    #b=int(input("b не больше 3="))
