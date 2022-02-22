# duplicord

A bot (that creates webhooks) dedicated to copying messages from one server to another.

Is your server getting deleted, for some reason or another?  
Does your friend abuse their role as owner to get what they want?  
Third thing?

This is the bot for you!

### What does this bot do?

* Copies a list of messages dumped using [this tool](https://github.com/Tyrrrz/DiscordChatExporter) to a target server using a bot.
* It does this by creating webhooks with the sender's name and avatar, and sending the original message through the webhook.
* Displays a nifty progress bar, using the alive-progress library.
* Pins messages that were pinned before.
* Copies attachments, like images, videos, and files.

### What might this bot do in the future? (A.K.A my TODO list)

* Create channels
* Detect multiple webhooks for different channels
* Move the webhooks to different channels
* Seperate messages with a different timestamp
  * Do this with some unicode trickery, insert a 0-width space into author name to make it seperate from author above if timestamp different by ~20min
* ~~Display a nifty progress bar~~ *Added in v0.2.0*
* Allow you to resume from a certain point on failure
* Allow you to filter out certain users (like bots)
* ~~Pin messages that were pinned before~~ *Added in v0.2.0*
* ~~Copy attachments~~ *Added in v0.4.0*
  * Split attachments >8MB into multiple files?
  * Download and reupload attachments live to save on disk space?
* Copy reactions
* Be dockerized, for easier running.

### What won't this bot do?

* Allow you to see hidden channels in the original server. The only messages that get dumped, and thus copied over, are messages that you
can see yourself. This also means you can't copy servers you're banned from, unless you dumped them before you got banned. Same with deleted
messages, edited messages, etc.
* Actually pull from the server. The messages will be exactly how they were when you dumped them. The original server doesn't even have
to exist anymore. 
* Bypass nitro restrictions. If the original server has attachments over 8MB, they will not be copied unless you boost the target server 
to the required level. A message will be sent, however
* Go fast. The ratelimits for webhooks aren't the nicest. 

## Usage instructions

1. Download and install python (>=3.8)
2. `pip install poetry`
3. `git clone http://thecakeisalie25/duplicord.py; cd duplicord`
5. `poetry install --no-dev; poetry shell`
6. (If you want to use duplicord again in the future, come back to this directory and run `poetry shell` again, then start from here.)
7. Download [this](https://github.com/Tyrrrz/DiscordChatExporter)
8. Export any channels you want to get copied (use ctrl to select multiple). 
    * Make sure the format is set to JSON, and under the 3 lines menu also make sure that "Download media" is turned on.
9. Copy your folder of exported messages into the (outer) duplicator folder, and rename it to "exported".
10. Create a bot [here](https://discord.com/developers/applications) and copy it's token.
11. `python -m duplicord`
12. Follow the prompts.

### Helpful tips

* Avoid copying any channels dedicated to bots, especially music bots. They don't really matter, and can contain TONS of youtube thumbnails.
* You can update a dump by just dumping again to the same folder, and if "reuse downloaded media" is on in the dumper program's settings, it will just pull messages and keep the same files.
* Check in the export folder to make sure that there's actually a folder for each channel with all the attachments in it. 
* Don't get concerned if it stops. Usually, the bot will be ratelimited once every 31 or so messages. Give it 3 minutes or so, if it's worse than that, raise an issue.

## Changelog

```changelog
v0.4.0
    Attachments
v0.3.0
    Avatars working
v0.2.0
    Pin messages that were pinned
    Progress bar
v0.1.0
    Basic functionality
