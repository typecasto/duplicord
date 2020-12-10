# duplicord

A bot (that creates webhooks) dedicated to copying messages from one server to another.

**Warning: This bot is in early alpha. It will not function. If you do get it to function, create an issue telling me to update the readme.**

Is your server getting served a DMCA takedown?  
Does your friend abuse their role as owner to get what they want?  
Third thing?

This is the bot for you!

### What does this bot do?

* Copies a list of messages dumped using [this tool](https://github.com/Tyrrrz/DiscordChatExporter).
* It does this by creating webhooks with the sender's name and avatar, but unfortunately roles and nicknames aren't carried over.

### What might this bot do in the future? (A.K.A my TODO list)

* Work lol
* Create channels
* Display a nifty progress bar
* Allow you to resume from a certain point on failure
* Allow you to filter out certain users (like bots)
* Pin messages that were pinned before
* Copy attachments
  * Split attachments >8MB into multiple files?
  * Download and reupload attachments live to save on disk space?
* Copy reactions

### What won't this bot do?

* Allow you to see hidden channels in the original server. The only messages that get dumped, and thus copied over, are messages that you
can see yourself. This also means you can't copy servers you're banned from, unless you dumped them before you got banned. Same with deleted
messages, edited messages, etc.
* Actually pull from the server. The messages will be exactly how they were when you dumped them. The original server doesn't even have
to exist anymore. 
* Bypass nitro restrictions. If the original server has attachments over 8MB, they will not be copied unless you boost the target server 
to the required level. A message will be sent, however
* Go fast. The ratelimits for webhooks aren't the nicest. There might be something a good dev could do about it, but that's not me.

## Usage instructions

1. Download and install python (>=3.8)
2. Download [this](https://github.com/Tyrrrz/DiscordChatExporter)
3. Export any channels you want to get copied (use ctrl to select multiple). 
    * Make sure the format is set to JSON, and under the 3 lines menu also make sure that "Download media" is turned on.
4. `pip install poetry`
5. `git clone http://thecakeisalie25/duplicord.py; cd duplicator`
6. `poetry install --no-dev; poetry shell`
7. Copy your folder of exported messages into the (outer) duplicator folder, and rename it to "exported".
8. `python -m duplicord`
9. Follow the prompts.

### Helpful tips

* Avoid copying any channels dedicated to bots, especially music bots. They don't really matter, and can contain TONS of youtube thumbnails.
* You can update a dump by just dumping again to the same folder, and if "reuse downloaded media" is on in the dumper program's settings, it will 
just pull messages and keep the same files.
* Check in the export folder to make sure that there's actually a folder for each channel with all the attachments in it. 
* For public/large servers, maybe go one channel at a time. The memes chat alone on one of my servers was 1.13 GB and there's like 10 people total for <1 year.