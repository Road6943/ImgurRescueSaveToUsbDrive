# https://github.com/felipeam86/imagedownloader

## IMPORTANT --->>> imgdl.log maps the original image url to its new path!!!
## It also tells you how many image downloads failed in the last line!

# Only fails are .mp4 files, edit this script to tackle those too
# the log file shows all failures
# log appends each run but doesnt redownload sucesful prior dl's

inputFile = "DiscordLinks/1_linksDiscord.txt"

# this is on a usb drive
# DONT CHANGE THIS, even for DISCORD IMAGES
storagePath = "../../../../../../../Volumes/THKAILAR/ImgurBackups"

# =================================

import imgdl, json

def getUrlsToDownload():
    links = []
    with open(inputFile) as inFile:
        links = inFile.readlines()
    
    # set conversion will remove many duplicate links
    links = {link.strip() for link in links}

    imageLinks = {link for link in links if not link.endswith('.mp4')}

    return imageLinks

def downloadImages(imageLinks):
    # handle image links
    # the .log file stores all the link->path mappings and failed downloads anyways
    # so don't bother saving on my own
    paths = imgdl.download(
        imageLinks, 
        store_path=storagePath,
        n_workers=50
    )

# parse log file to see which imgur link downloads failed
def checkForFailures(imageLinks: set[str]):
    successfulDownloads = set()

    with open("imgdl.log") as logFile:
        for line in logFile:
            obj = json.loads(line)
            if obj.get("success", False):
                successfulDownloads.add(obj.get("url", ""))
    
    failedDownloads = imageLinks.difference(successfulDownloads)
    print(f"THERE WERE {len(failedDownloads)} FAILED DOWNLOADS:")
    for link in failedDownloads:
        print(link)
    print(f"^^ THERE WERE {len(failedDownloads)} FAILED DOWNLOADS ^^")
    # make a clickable link html file of all failed downloads:
    with open("4_failedLinks.html", "w+") as failedLinksFile:
        failedLinksFile.write('<html><head></head><body><ol>')
        for link in failedDownloads:
            failedLinksFile.write(f'<li><a href={link}>{link}</a></li>')
        failedLinksFile.write('</ol></body></html>')



def main():
    imageLinks = getUrlsToDownload()
    # keep downloadImages commented out until you actually need it
    # to avoid making imgdl.log too big (bc it expands with every run)
    #   --- it won't redownload already done images, but the log will list them again
    #downloadImages(imageLinks)
    checkForFailures(imageLinks) # this often shows broken links

main()