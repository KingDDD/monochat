import twitch
from termcolor import colored

client_id = 'bcdc6mhpnl295p0vfqexm5rlbqer2e'

client_secret = 'v43iorkna672udqngnyrmx8qhq9ebh'

helix = twitch.Helix(client_id, client_secret)

twitch.Chat(channel='#cowsep', nickname='tester', oauth='oauth:j29lpyt2er99i0xg0nkpunljk7j34c').subscribe(
        lambda message: print(colored('|TWITCH|', 'yellow'), colored(message.sender, 'red'), colored(message.text, 'cyan')))
