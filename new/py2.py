
from pyrogram import Client

app = Client( session_name="example",api_id=299527, api_hash='27fb778154da0c8b9f37b80eecfed58b', proxy=dict( hostname="us.defy.pro", port=666, username="defy", password="slojnopizdec" ))
app.start()