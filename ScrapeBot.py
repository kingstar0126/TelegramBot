from telethon import TelegramClient, events, sync, utils
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (PeerChannel, MessageEmpty, InputUserSelf)
import time

api_id = 
api_hash = ''
client = TelegramClient('anon', api_id, api_hash).start()

a=0
arrChannels=[]
arrFiles=[]

offset_id = 0
offset_date = 0
total_messages = 0
messages = []
entities = {}
arrChannels=[]

quantity=int(input("How many Chat/Group/Channels do you wanna scrape?: "))
for e in range(1, quantity+1):
    arrChannels+=[int(input(f"Enter ID of entity {e}: "))]

quan=int(input("How many files do you want to scrape? 0 to scrape all: "))
if quan==0:
    limit=None
    limit = float('inf') if limit is None else int(limit)
else:
    limit=quan+1
for channel in arrChannels:
    chat=client.get_entity(channel)
    try:
        while len(messages) < limit:
            messages=[]
            real_limit = min(limit - len(messages), 100)
            history= client(GetHistoryRequest(peer=chat, offset_id=offset_id, offset_date=offset_date, add_offset=0, limit=real_limit, max_id=0, min_id=0, hash=0))
            messages.extend(
                m for m in history.messages if not isinstance(m, MessageEmpty)
            )
            
            if len(history.messages) < real_limit:
                break

            offset_id = history.messages[-1].id
            offset_date = history.messages[-1].date
            total_messages = len(messages)

            if limit > 3000:
                time.sleep(1) 

        for message in messages:
            if message.media:
                client.send_file(-278164674, message.media)
    except:
        print("The channel/user/group are incorrect or there are an error")
        input("Press ENTER to exit")