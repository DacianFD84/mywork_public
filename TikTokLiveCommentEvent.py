from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import CommentEvent

# Get the TikTok username from user input
username = input("Enter your TikTok username: ")

# Instantiate the client with the user's username
client = TikTokLiveClient(unique_id="@" + username)

# Define the event handler for comment events
@client.on("comment")
async def on_comment(event: CommentEvent):
    print(f"{event.user.nickname} -> {event.comment}")

if __name__ == '__main__':
    # Run the client and block the main thread
    # await client.start() to run non-blocking
    client.run()
