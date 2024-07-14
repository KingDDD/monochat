mport asyncio
import websockets
import json

class VimeoLiveChatCollector:
    def __init__(self, websocket_url):
        self.websocket_url = websocket_url
        self.chat_messages = []

    async def connect(self):
        async with websockets.connect(self.websocket_url) as websocket:
            await self.listen_messages(websocket)

    async def listen_messages(self, websocket):
        async for message in websocket:
            data = json.loads(message)
            if 'chat_message' in data:  # Adjust this condition based on the actual data format
                self.chat_messages.append({
                    'user': data['user'],
                    'message': data['message'],
                    'timestamp': data['timestamp']
                })
                print(f"{data['user']}: {data['message']}")

    def start(self):
        asyncio.get_event_loop().run_until_complete(self.connect())

    def get_chat_messages(self):
        return self.chat_messages

# Example usage
if __name__ == "__main__":
    websocket_url = "wss://your_vimeo_livestream_chat_url"  # Replace with the actual WebSocket URL
    collector = VimeoLiveChatCollector(websocket_url)
    try:
        collector.start()
    except KeyboardInterrupt:
        print("Stopped collecting.")
        print(collector.get_chat_messages())

