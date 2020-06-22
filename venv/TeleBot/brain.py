import telepot as tp
import time
from telepot.loop import MessageLoop
    
def handle(msg):
    
    content_type, chat_type, chat_id = tp.glance(msg)
    print(content_type, chat_type, chat_id)
    
    if content_type == "text":
        bot.sendMessage(chat_id, msg['text'])
        bot.sendMessage(chat_id, "Ciao mio creatore!")
        
bot = tp.Bot(TOKEN_HERE)
MessageLoop(bot, handle).run_as_thread()
print("Listening...")

while True:
    time.sleep(10)
