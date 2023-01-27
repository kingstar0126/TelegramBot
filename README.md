# Telegram Scraper
This script allows you to scrape messages from Telegram Channels, Groups, or Users using the telethon library.

### Usage
- Replace api_id and api_hash with your own Telegram API ID and Hash. You can obtain these by creating an app on the Telegram website.
- Replace mainGroup with the ID of the group where you want to send the files.
- Run the script and enter the number of chats/groups/channels you want to scrape.
- Enter the ID of each entity one by one.
- Enter the number of files you want to scrape (0 to scrape all files)
- The script will scrape the messages from the specified entities, and if any of the messages include files (e.g. images, videos, etc.), it will send those files to the specified group.

### Install dependencies:
```
pip install -r requirements.txt
```
# EXAMPLE:

https://user-images.githubusercontent.com/100825478/174222224-a490b40d-dd0e-4120-8d96-cd14147ce7ed.mp4

###
Please note that using this script to scrape messages from Telegram entities without their explicit consent may be against Telegram's terms of service and may result in your API credentials being banned. Use this script responsibly and only scrape messages from entities that you have obtained explicit consent from.
###
