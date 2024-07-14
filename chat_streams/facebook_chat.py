mport requests
import time

class FacebookLiveChatCollector:
    def __init__(self, access_token, video_id):
        self.access_token = access_token
        self.video_id = video_id
        self.chat_messages = []
        self.base_url = "https://graph.facebook.com/v15.0"
    
    def get_comments(self, after=None):
        url = f"{self.base_url}/{self.video_id}/comments"
        params = {
            "access_token": self.access_token,
            "fields": "from,message,created_time",
            "live_filter": "stream",
            "filter": "toplevel",
            "order": "chronological",
        }
        if after:
            params["after"] = after
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Error fetching comments: {response.status_code} - {response.text}")
            return None
    
    def start_collecting(self, poll_interval=5):
        after = None
        while True:
            comments_data = self.get_comments(after)
            if comments_data:
                comments = comments_data.get('data', [])
                for comment in comments:
                    self.chat_messages.append({
                        'user': comment['from']['name'],
                        'message': comment['message'],
                        'timestamp': comment['created_time']
                    })
                    print(f"{comment['from']['name']}: {comment['message']}")
                after = comments_data.get('paging', {}).get('cursors', {}).get('after')
            time.sleep(poll_interval)
    
    def get_chat_messages(self):
        return self.chat_messages

# Example usage
if __name__ == "__main__":
    access_token = "your_facebook_access_token"
    video_id = "your_facebook_video_id"
    collector = FacebookLiveChatCollector(access_token, video_id)
    try:
        collector.start_collecting()
    except KeyboardInterrupt:
        print("Stopped collecting.")
        print(collector.get_chat_messages())

