# run in terminal with:
# python3 0.2_extractDiscordLinks.py

# I didn't bother renaming a lot of the vars/comments from imgur to discord
# don't bother doing it, you might mess something up

SHEETS_FOLDER_NAME = "csv_files"

####################################
import os, csv, json
from typing import Dict, Set

# The set contains all discord links found across all CSV Files
# I do it like this instead of organizing by sheet because many sheets have common files
# so this reduces how much downloading/uploading of images is needed
discordLinks = set()

# open every csv file in the folder
filesToSkip = [
    # I'm not gonna skip any for this one
]

# links I've come across that break stuff
invalidLinks = set([
    'https://discord.gg/ttwgxcp6t3',
    # technically the '.discord' removes this above anyways, but I'm putting it
    #   here to call attention to the possibility of invite links like this 
    #   maybe passing the filter

    'https://cdn.discordapp.com/attachments/1113513104467304488/1120044335300366376/wa2w9sy_d.webp',
    # the webp link above is broken, and the only webp link as of oct 16 2023, so I'm just gonna not bother with it
])

for csvFilename in os.listdir(SHEETS_FOLDER_NAME):
    if csvFilename in filesToSkip:
        continue

    csvFilepath = os.path.join(SHEETS_FOLDER_NAME, csvFilename)
    with open(csvFilepath, 'r') as file:
        # iterate across the current csv file, and if '.discord' is in a cell,
        # then add that cell's contents to the discordLinks set
        csvreader = csv.reader(file)
        for row in csvreader:
            for cell in row:
                cell = cell.strip()

                # remove the query params from end of url
                if '?' in cell:
                    cell = cell.split('?')[0]
                
                cell = cell.lower()

                # get all .discord links
                if '.discord' in cell and cell not in invalidLinks:

                    # Enable this branch if you want to look for potential
                    # other link formats that might be slipping through
                    # Make sure to also change '.discord' to just 'discord' above
                    # but also make sure to turn it back when testing is done
                    if 'cdn.discordapp.com' in cell or 'media.discordapp.net' in cell:
                        #continue
                        pass

                    # Enable this branch to test for other file types
                    # i.e. there was 1 webp image as of Oct 16 2023
                    if '.png' in cell or '.jpg' in cell or '.jpeg' in cell:
                        #continue
                        pass
                    
                    # this is usually multiple links in one cell
                    # this would be a pain to replace anyways
                    # and also I think most of these were rejected and told
                    # to resubmit with only 1 link anyways
                    if "\n" in cell:
                        #continue
                        pass

                    # (( Left over from the imgur download version bc I thought it was interesting )) example:
                    # https://images-ext-1.discordapp.net/external/4ZoqDGJBBnMUJcQ2so0tn63rQfRBZSgiON6-UbJw23s/https/i.imgur.com/m3iuxUAh.jpg

                    discordLinks.add(cell)

# dump discordLinks dict into a text file
OUTPUT_FILE_NAME = "1_linksDiscord.txt"
with open(OUTPUT_FILE_NAME, 'w') as outputFile:
    for line in list(discordLinks):
        outputFile.write(line + "\n")

