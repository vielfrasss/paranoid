from pyrogram import Client
from pyrogram.api import functions
import config
from get import chates
id=config.api_id
hash=config.api_hash
proxy=config.proxy
app = Client(session_name="example" , api_id=id ,api_hash=hash,proxy=proxy)
app.start() 
#_____sendmessage_______
smsuser=input("username/1351754478: ")
if smsuser=='me':
	smguser= 'me'
if smsuser[:1]=='@':
	smguser=smsuser[1:]
else:
    smguser=int(smsuser)  
print(app.get_history(smguser,0,1))
#print(app.get_chat(smguser))
print(smguser)
get.chates(smguser)
    #smgtext=input("message: ")
    #print(smgtext)
    #app.send_message(smguser,smgtext)
    #b=int(input("b не больше 3="))
