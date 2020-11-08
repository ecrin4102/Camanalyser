import os
import sys
from datetime import datetime
from discord_webhook import DiscordWebhook


f = os.open(__file__+"\config.txt", os.O_RDONLY)
url =f.readline()
url=url[3:]


url=os.environ.get("DISCORD_WEBHOOK_CAMERA")
print(url)
webhook = DiscordWebhook(url=url)

videoFile=sys.argv[1]
filename=os.path.basename(videoFile)

with open(videoFile, "rb") as f:
    webhook.add_file(file=f.read(), filename=filename)

response = webhook.execute()



