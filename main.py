import datetime
import os
import time

from pyrogram import Client
app = Client(name='Danya', api_id=16491994, api_hash='f25aa8e9cc86c0d630f0722a79462f01')

@app.on_message()
async def serch_war(client, message):
    if message.chat.id > 0:
        print(message.date, message.chat.id, message.chat.first_name)
        try:
            await message.forward(-1001785277422)
        except:
            text = str(message).replace("\n","")
            with open('text-error', 'a', encoding='UTF-8') as f: f.write(f'{text}\n')
            print(text)

app.run()