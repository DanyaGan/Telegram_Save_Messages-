import traceback
from pyrogram import Client

class telegram:
    def __init__(self, Name, id, hash, id_chat):
        self.id_chat = id_chat
        self.app = Client(name=Name, api_id=id, api_hash=hash)

    def start(self):
        @self.app.on_message()
        async def serch(client, message):
            print(message.date, message.chat.id, message.chat.first_name)
            try:
                await message.forward(self.id_chat)
            except Exception as e:
                traceback_str = str(traceback.format_exc())
                with open('ErrorSaveMassage', 'a', encoding='UTF-8') as f:
                    f.write(f'Error occurred: {traceback_str}\n')

        self.app.run()