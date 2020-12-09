from typing import List, Tuple
import discord
import os
import pprint as prettyprinter
import re

pp = prettyprinter.PrettyPrinter(indent=4)
pprint = pp.pprint

# TODO Error handling

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

    # [(Filename, category, channelname)]
    channelsToImport: List[Tuple(str, str, str, bool)] = []

    for loc in os.listdir("./exported/"):
        if loc.endswith(".json"):  # Find all the channels exported
            matches: re.Match = re.match("(.+) - (.+) - (.+) \\[\d+\\]\\.json", loc)
            hasfiles: bool = False
            print(
                f'Found channel "{matches.group(3)}" in category "{matches.group(2)}"'
            )  # Print out channel name

            if os.path.exists(matches.group(0) + "_Files"):
                print("...With local attachments.")
                hasfiles = True

            if not yestoall:  # Prompt if they want to import this channel
                while (
                    answer := input("[Y]es / [N]o / [A]ll of them").upper()
                ) not in "NYA":  # i hate myself
                    pass  # wait until the user stops messing it up
                if answer == "":
                    answer = "Y"  # user managed to sneak one by
                if answer == "A":
                    yestoall = True
                    answer = "Y"
                if answer == "Y":
                    channelsToImport.append(
                        (matches.group(0), matches.group(2), matches.group(3), hasfiles)
                    )
