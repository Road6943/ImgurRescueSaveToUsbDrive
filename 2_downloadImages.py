# https://github.com/felipeam86/imagedownloader

## IMPORTANT --->>> imgdl.log maps the original image url to its new path!!!
## It also tells you how many image downloads failed in the last line!

# Only fails are .mp4 files, edit this script to tackle those too
# the log file shows all failures
# log appends each run but doesnt redownload sucesful prior dl's

inputFile = "1_linksImgur.txt"

# this is on a usb drive
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



def main():
    imageLinks = getUrlsToDownload()
    #downloadImages(imageLinks)
    checkForFailures(imageLinks)

main()