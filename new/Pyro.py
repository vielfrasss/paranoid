from pyrogram import Client
import config
id=config.api_id
hash=config.api_hash
proxy=config.proxy
app = Client(session_name="example" , api_id=id ,api_hash=hash,proxy=proxy)

chatid=config.chatlink
channelid=config.link
messid=130350
app.start() 
#print(app.get_me()) 
#print(app.get_history(chatid,limit=1))
#print(app.get_messages(chatid, messid))
#app.forward_messages(chatid, 'me', message_ids=130350)


def chat(smguser):
    smgtext
    ex=
    while ex!='exit[]'

print('ok')
b=''

while b!=:

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
print("exit")
#__________________________

    