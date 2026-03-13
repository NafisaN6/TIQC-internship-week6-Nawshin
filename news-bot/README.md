# Slack Daily News Summary Bot

## Project Overview

This project is a Slack bot which  will automatically post a daily summary of verified news articles to a Slack channel (in this case, I had it give it to me in my private dms). The bot retrieves headlines from trusted news organizations, summarizes them, and finally, posts them to Slack with a source link.

The goal of this project is to demonstrate automation, API integration, and basic information verification.

---

## How the Bot Works

1. The script connects to the **NewsAPI** to retrieve top headlines.
2. It filters results to only include **trusted news organizations**.
3. The bot creates a formatted summary message.
4. The message is sent to a specific user (in this case, me) using the **Slack API**.

Each news item includes:

* A headline
* A short description
* A clickable source link

---

## News Sources Used

To ensure credibility, the bot will only pull headlines from these trusted sources:

* BBC News
* Reuters
* Associated Press
* New York Times

These sources were chosen because they are widely recognized news organizations that many trust.

---

## Verification Logic

The bot verifies news credibility by **restricting results to trusted publishers** instead of pulling articles from all possible sources.

This helps prevent:

* Any unverified news
* Any opinion-only content
* All the low credibility websites

By limiting the API's request to well-known outlets, the bot then makes sure that the news summaries come from trusted sources.

---

## Daily Summary Logic

The bot retrieves up to **5 headlines per run** and formats them into a message.

Each article is then summarized using the article description provided by the news API. If the description is unavailable, then a placeholder summary is used.

---

## Security Note

For the Slack Bot Token and NewsAPI key, I had them **removed from the uploaded code before pushing to GitHub**.

Instead, placeholders got used:

```
YOUR_SLACK_BOT_TOKEN
YOUR_NEWS_API_KEY
```

This change was because **GitHub automatically blocks uploads that contain private API keys or tokens**. These tokens should not be shared publicly, so I unable to include them within the Github Code.

To run the bot locally, you should replace the placeholders with your own API keys.

---

## Scheduling the Bot

The script is designed to run once per day. This is allowed using:

* Cron jobs
* Windows Task Scheduler
* GitHub Actions

For this assignments purpose, the bot can also be run by yourself using:

```
python bot.py
```

---

## Technologies Used

* Python
* Slack API (`slack_sdk`)
* NewsAPI
* Requests library

---

## Example Output

When executed, the bot posts a message in Slack containing:

* Headline
* Short summary
* Link to the original article

This allows users in the Slack channel to quickly stay updated with verified news.
