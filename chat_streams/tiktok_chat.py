
from TikTokLive import TikTokLiveClient
from TikTokLive.types import ChatMessage

class TikTokChatCollector:
    def __init__(self, username):
        self.username = username
        self.chat_messages = []
        self.client = TikTokLiveClient(unique_id=username)
        self.client.add_listener("chat", self.on_chat)

    def on_chat(self, event: ChatMessage):
        self.chat_messages.append({
            'user': event.user.unique_id,
            'message': event.content,
            'timestamp': event.created_at
        })
        print(f"{event.user.unique_id}: {event.content}")

    def start(self):
        self.client.start()

    def stop(self):
        self.client.stop()

    def get_chat_messages(self):
        return self.chat_messages

# Example usage
if __name__ == "__main__":
    username = "your_tiktok_username"
    collector = TikTokChatCollector(username)
    collector.start()

