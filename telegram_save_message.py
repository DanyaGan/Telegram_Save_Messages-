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
    def __init__(self, Name, id, hash, acknowledge=[], consider=[]):
        self.app = Client(name=Name, api_id=id, api_hash=hash)
        self.acknowledge = acknowledge
        self.consider = consider

    def messages_group(self, id_chat):
        async def forward(message):
            print(message.date, message.chat.id, message.chat.first_name)
            try:
                await message.forward(id_chat)
            except Exception as e:
                traceback_str = str(traceback.format_exc())
                with open('ErrorSaveMassage', 'a', encoding='UTF-8') as f:
                    f.write(f'Error occurred: {traceback_str}\n')

        if self.acknowledge or self.consider:
            @self.app.on_message()
            async def serch(client, message):
                if message.chat.id in self.consider:
                    forward(message)

                elif message.chat.id not in self.acknowledge:
                    forward(message)

            self.app.run()  

    def messages_file(self):
        def save_file(message, file_name=None, type_file=None, file=None):
            check_or_create_directory(str(message.chat.id))
            check_or_create_file('text.json', str(message).replace('\n', ''))

            if file_name:
                with open(f'{file_name}.{type_file}', 'w') as f:
                    f.write(file)

            os.chdir('../')
        
        if self.acknowledge or self.consider:
            check_or_create_directory('users')
            @self.app.on_message()
            async def serch(client, message):
                if message.chat.id in self.consider or message.chat.id not in self.acknowledge:
                    print('save')
                    if message.photo:
                        file = await self.app.download_media(message.photo.file_id)
                        file_name = str(message.photo.date).replace(':', '-')
                        save_file(message, file_name, 'png', file)

                    elif message.video:
                        file = await self.app.download_media(message.video.file_id)
                        file_name = str(message.video.date).replace(':', '-')
                        save_file(message, file_name, 'mp4', file)

                    elif message.voice:
                        file = await self.app.download_media(message.voice.file_id)
                        file_name = str(message.voice.date).replace(':', '-')
                        save_file(message, file_name, 'mp3', file)
                    
                    else:
                        save_file(message)

                    print(message.date, message.chat.id, message.chat.first_name)
                    
            self.app.run()

    