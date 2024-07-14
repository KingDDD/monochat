import pytchat
from termcolor import colored

chat = pytchat.create(video_id="iyOq8DhaMYw")
while chat.is_alive():
        for c in chat.get().sync_items():
                    print(colored('|YOUTUBE|', 'yellow'), colored(f"{c.author.name}", 'red'), colored(f"{c.message}", 'cyan'))
