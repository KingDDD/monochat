mport instaloader
import time

class InstagramLiveChatCollector:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.chat_messages = []
        self.loader = instaloader.Instaloader()
        self.login()

    def login(self):
        self.loader.login(self.username, self.password)

    def get_livestream_comments(self, livestream_id):
        comments = []
        # Hypothetical method to fetch livestream comments
        # In reality, you would need to use the appropriate method or API call
        # to fetch comments from a livestream
        livestream_comments = self.loader.get_livestream_comments(livestream_id)
        for comment in livestream_comments:
            comments.append({
                'user': comment.user,
                'message': comment.message,
                'timestamp': comment.timestamp
            })
        return comments

    def start_collecting(self, livestream_id, poll_interval=5):
        while True:
            new_comments = self.get_livestream_comments(livestream_id)
            for comment in new_comments:
                self.chat_messages.append(comment)
                print(f"{comment['user']}: {comment['message']}")
            time.sleep(poll_interval)

    def get_chat_messages(self):
        return self.chat_messages

# Example usage
if __name__ == "__main__":
    username = "your_instagram_username"
    password = "your_instagram_password"
    livestream_id = "your_instagram_livestream_id"
    collector = InstagramLiveChatCollector(username, password)
    try:
        collector.start_collecting(livestream_id)
    except KeyboardInterrupt:
        print("Stopped collecting.")
        print(collector.get_chat_messages())

