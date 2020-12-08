# duplicord

A bot (that creates webhooks) dedicated to copying messages from one server to another.

**Warning: This bot is in early alpha. It will not function. If you do get it to function, create an issue telling me to update the readme.**

Is your server getting served a DMCA takedown?  
Does your friend abuse their role as owner to get what they want?  
Third thing?

This is the bot for you!

### What does this bot do?

* Copies a list of messages dumped using [this tool](http://example.com/todo/link_the_messages_dumper).
* It does this by creating webhooks with the sender's name and avatar, but unfortunately roles and nicknames aren't carried over.

### What might this bot do in the future? (A.K.A my TODO list)

* Work lol
* Display a nifty progress bar
* Allow you to resume from a certain point on failure
* Allow you to filter out certain users (like bots)
* Pin messages that were pinned before
* Copy attachments
  * Split attachments >8MB into multiple files?
* Copy reactions

### What won't this bot do?

* Allow you to see hidden channels in the original server. The only messages that get dumped, and thus copied over, are channels you
can see and read messages from. This also means you can't copy servers you're banned from, unless you dumped them before you got banned.
* Actually pull from the server. The messages will be exactly how they were when you dumped them. The original server doesn't even have
to exist anymore. 
* Bypass nitro restrictions. If the original server has attachments over 8MB, they will not be copied unless you boost the target server 
to the required level. A message will be sent, however
* Go fast. The ratelimits for webhooks aren't the nicest. There might be something a good dev could do about it, but that's not me.

## Usage instructions

1. Download and install python (>=3.8)
2. `pip install poetry`
3. `git clone http://thecakeisalie25/duplicord.py; cd duplicator`
4. `poetry install --no-dev; poetry shell`
5. `python -m duplicord`
6. Follow the prompts.
