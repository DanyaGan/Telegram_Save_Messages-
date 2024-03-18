import traceback
import os
from pyrogram import Client


def check_or_create_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        os.chdir(directory_path)
    else:
        os.chdir(directory_path)

def check_or_create_file(file_path, data):
    if not os.path.exists(file_path):
        with open(file_path, 'w'): pass
    else:
        with open(file_path, 'a', encoding='UTF-8') as f:
            f.write(data)
            
class telegram:
    def __init__(self, Name, id, hash, id_chat):
        self.app = Client(name=Name, api_id=id, api_hash=hash)

    def messages_group(self, id_chat):
        @self.app.on_message()
        async def serch(client, message):
            print(message.date, message.chat.id, message.chat.first_name)
            try:
                await message.forward(id_chat)
            except Exception as e:
                traceback_str = str(traceback.format_exc())
                with open('ErrorSaveMassage', 'a', encoding='UTF-8') as f:
                    f.write(f'Error occurred: {traceback_str}\n')

        self.app.run()
    
    def messages_file(self):
        check_or_create_directory('users')
        @self.app.on_message()
        async def serch(client, message):
            check_or_create_directory(str(message.chat.id))
            check_or_create_file('text.json', str(message).replace('\n', ''))
            print(message.date, message.chat.id, message.chat.first_name)
            os.chdir('../')

        self.app.run()

    