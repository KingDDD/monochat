import pytchat
import twitch
from termcolor import colored

m_queue = []

# Twitch stuff
client_id = 'bcdc6mhpnl295p0vfqexm5rlbqer2e'
client_secret = 'v43iorkna672udqngnyrmx8qhq9ebh'
helix = twitch.Helix(client_id, client_secret)

# Youtube stuff
chat = pytchat.create(video_id="L7JEMGmB6Bg")
while True:
    if chat.is_alive():
        a=''
        for c in chat.get().sync_items():
            m_queue.append(colored('|YOUTUBE| ', 'yellow', attrs=["bold","underline"]) + colored(f"{c.author.name} ", 'red', attrs=['underline']) + colored(f"{c.message} ", 'cyan'))
        if m_queue:
            print(m_queue[0])
            m_queue=[]
            
    twitch.Chat(channel='#cowsep', nickname='tester', oauth='oauth:j29lpyt2er99i0xg0nkpunljk7j34c').subscribe(lambda message: m_queue.append(colored('|TWITCH| ', 'yellow', attrs=["bold","underline"]) + colored(message.sender, 'red', attrs=["underline"]) + ' ' + colored(message.text, 'cyan')))
    if m_queue:
        print(m_queue[0])
        m_queue=[] 
