import requests
from slack_sdk import WebClient

SLACK_TOKEN = "YOUR_SLACK_BOT_TOKEN"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

CHANNEL = "U0ABP82M6R2"

client = WebClient(token=SLACK_TOKEN)

SOURCES = "bbc-news,reuters,associated-press,the-new-york-times"

url = f"https://newsapi.org/v2/top-headlines?sources={SOURCES}&apiKey={NEWS_API_KEY}"

response = requests.get(url)
data = response.json()

articles = data["articles"][:5]

message = "*Daily Verified News Summary*\n\n"

for article in articles:
    title = article["title"]
    description = article["description"]
    link = article["url"]

    if description is None:
        description = "Short update from a trusted news source."

    message += f"*{title}*\n"
    message += f"{description}\n"
    message += f"{link}\n\n"

client.chat_postMessage(
    channel=CHANNEL,
    text=message
)

print("News posted to Slack!")