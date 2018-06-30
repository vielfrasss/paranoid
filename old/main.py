from pyrogram import Client
from pyrogram.api import functions
import time
import sys
import setting
app = Client( session_name="new_my_account_covach", api_id=299527, api_hash='27fb778154da0c8b9f37b80eecfed58b' )
# my_account_covach
#or
#my_account_vielfrass
app.start() 
#print(app.get_me()) 
#g=int(input("lol : "))
x=0
print(app.get_users('me'))
#while x<g:
	#app.join_chat('t.me/joinchat/Hl0rgBG-KSsumYlURb9uWQ')
#	app.leave_chat(1351754478,False)
#	time.sleep(4)	
#app.join_chat('t.me/joinchat/Hl0rgBG-KSsumYlURb9uWQ')
#app.get_messages
#app.leave_chat('t.me/joinchat/Hl0rgBG-KSsumYlURb9uWQ',False)
#
x=str(app.send(   functions.messages.CheckChatInvite('Hl0rgBG-KSsumYlURb9uWQ')))
#print(x)
s=str.split(x,'id": ')
print(s[1])
#app.send(1351754478,x)
b=0



while b<3:

#_____sendmessage_______
    smsuser=input("username/1351754478: ")
    if smsuser=='me':
    	smguser= 'me'
    if smsuser[:1]=='@':
    	smguser=smsuser[1:]
    else:
    	smguser=int(smsuser)  
    print(app.get_history(smguser,0,1))
    print(app.get_chat(smguser))
    print(smguser)
    smgtext=input("message: ")
    print(smgtext)
    app.send_message(smguser,smgtext)
    b=int(input("b не больше 3="))
#__________________________

    
    
    
    
    
#app.leave_chat(1351754478,False)