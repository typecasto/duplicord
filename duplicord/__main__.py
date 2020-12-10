from typing import Dict, List, Optional, Tuple
import discord
import os
import pprint as prettyprinter
import re
import json
from alive_progress import alive_bar, config_handler
config_handler.set_global(unknown = "dots_waves2")

pp = prettyprinter.PrettyPrinter(indent=4)
pprint = pp.pprint

# TODO Error handling

channelsToImport: List[Tuple[str, str, str, bool]] = []
if __name__ == "__main__":
    # Handle files and enumerate channels
    # File structure looks like this
    #
    # duplicord/
    #   exported/
    #       Server name - Category name - Channel name [103957...].json
    #       Server name - Category name - Channel name [103957...].json_Files/
    #           whatever.jpg, etc (all the attachments)
    #   duplicord/
    #       actual python stuff
    #
    if not os.path.exists("./exported/"):
        raise FileNotFoundError("Couldn't find a directory named 'exported'")

    yestoall: bool = False

    # [(Filename, category, channelname, hasfiles)]

    for loc in os.listdir("./exported/"):
        if loc.endswith(".json"):  # Find all the channels exported
            matches: re.Match = re.match("(.+) - (.+) - (.+) \\[\d+\\]\\.json", loc)
            hasfiles: bool = False
            print(
                f'Found channel "{matches.group(3)}" in category "{matches.group(2)}"'
            )  # Print out channel name

            if os.path.exists("./exported/" + matches.group(0) + "_Files/"):
                print("...With local attachments.")
                hasfiles = True

            # Prompt if they want to import this channel
            answer: Optional[str] = None
            if not yestoall:
                while not (
                    answer := input("Import it? [Y]es / [N]o / [A]ll > ").upper()
                ) in [
                    "N",
                    "Y",
                    "A",
                ]:  # nya ~uwu~
                    pass  # keep prompting until we get a valid answer
                if answer == "A":
                    yestoall = True

            if yestoall or answer == "Y":
                channelsToImport.append(
                    (matches.group(0), matches.group(2), matches.group(3), hasfiles)
                )

    print(f"\nAll in all, we got {len(channelsToImport)} channels ready to import.")

print("Ready to set up the bot. All we need is a token. Let's go, chief.")
token = input("token> ")
print("Give it a minute to come online.")
client = discord.Client()



@client.event
async def on_ready():
    print("We're online.")
    print("If it stops sending messages, stay calm. It's getting ratelimited.")
    print("Give it 3 minutes at max, then kill it and raise an issue.")
    # Assure single guild
    while len(client.guilds) != 1:
        input(
            "Please make sure the bot is in EXACTLY 1 guild. Press enter to continue."
        )
    target_guild: discord.Guild = client.guilds[0]
    # Get a webhook
    webhook: Optional[discord.Webhook] = None
    while webhook is None:
        for x in await target_guild.webhooks():  # x: discord.Webhook
            if "duplicord" in x.name.lower():
                webhook = x
                break
        if webhook is None:
            input(
                "Please create a webhook and name it duplicord. Press enter to continue."
            )
    for filename, category, channel, hasfiles in channelsToImport:
        input(f"Please change the webhook to {channel}. Press enter to continue.")
        with open("./exported/" + filename) as file:
            loaded = json.load(file)
        messages: List[dict] = loaded["messages"]
        messages_post_processed: List[dict] = []
        # Post processed message structure:
        # message = {
        #     "id": 1024,
        #     "webhook": True or False,
        #     "content": "message here" or None,
        #     "attachments": ["./exported/whatever.json_Files/whatever.jpg"] or None,
        #     "is_pinned": True or False,
        #     "author": {
        #         "name": "typecasto",
        #         "avatarUrl": "./exported/whatever.json"
        #     },
        #     "reactions": [(1024, "middletonmoment"),(None, "🤡")]
        # }
        # TODO Change webhook to match channel
        with alive_bar(
            len(messages), title="Sending messages..."
        ) as bar:
            for message in messages:
                # Find any content in the messages
                if message["type"] == "Default" and message["content"]:
                    sent: discord.Message = await webhook.send(
                        content = message["content"],
                        wait = True,
                        username=message["author"]["name"],
                    )
                else:
                    sent = None
                if message["isPinned"] == True:
                    await sent.pin()
                bar()
                

client.run(token)