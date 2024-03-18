# Telegram Save Messages

## About the project
The "Telegram Save Messages" project was developed to automate the saving of new messages to specified
groups in the Telegram messenger. Its main task is to ensure the safety of information, preventing
loss of important messages if they are deleted from a chat or channel.

## Why is it useful?
This project provides valuable assistance to users by allowing them to save and store content,
which they receive. Thanks to the "Telegram Save Messages" functionality, users
can be confident that information that has been removed from the original chat or channel
will be saved in the specified group, providing access to it at any convenient time. Thus the project
significantly improves the efficiency of data management in Telegram and provides more reliable storage
messages.

## To work with the project
Есть два способа сохранения сообщений `tsm.messages_group(id_group)` сохраняет в группу указаною, или `tsm.messages_file()` сохраняет на ваше устройство.
```python
import telegram_save_message as tsm

tsm = tsm.telegram(
  Name = 'Your name',
  id = 'Your account ID',
  hash = 'Hash of your account'
)
tsm.messages_group(id_chat = 'Group ID')
```
