# downloads the mp4's that the image downloader can't handle

inputFile = "1_linksImgur.txt"
outputFile = "3_videosFinishedDownloading.txt"

# this is on a usb drive
# keep the b prefix for os.path.join
# DONT CHANGE THIS EVEN FOR DISCORD IMAGES
storagePath = b"../../../../../../../Volumes/THKAILAR/ImgurBackups"

# ================================

import requests
import json
import os
from base64 import b64encode


TOTAL_MP4_LINKS = -1
NUM_MP4_LINKS_ALREADY_DOWNLOADED = 0

def getMp4UrlsToDownload():
    links = []
    with open(inputFile) as inFile:
        links = inFile.readlines()

    # set conversion will remove many duplicate links
    links = {link.strip() for link in links}
    mp4Links = {link for link in links if link.endswith('.mp4')}

    global TOTAL_MP4_LINKS
    TOTAL_MP4_LINKS = len(mp4Links)

    # remove previously downloaded links
    alreadyDownloadedLinks = set()
    with open(outputFile, 'r+') as outfile:
        for line in outfile:
            # each line of file is { url: filepath }
            url = list(json.loads(line).keys())[0].strip()
            alreadyDownloadedLinks.add(url)
    
    global NUM_MP4_LINKS_ALREADY_DOWNLOADED
    NUM_MP4_LINKS_ALREADY_DOWNLOADED = len(alreadyDownloadedLinks)
    
    return mp4Links.difference(alreadyDownloadedLinks)



def downloadMp4s(links):
    failedLinks = []
    numDownloaded = NUM_MP4_LINKS_ALREADY_DOWNLOADED

    with open(outputFile, 'a+') as outfile:
        for link in links:
            videoFilename = b64encode(bytes(link, 'ascii')) + b'.mp4'
            videoFilepath = os.path.join(storagePath, videoFilename)
            videoFilepath = videoFilepath.decode('ascii')
            
            try:
                resp = requests.get(link)
                resp.raise_for_status()

                # https://stackoverflow.com/a/71804501
                with open(videoFilepath, "wb") as f: # opening a file handler to create new file 
                    f.write(resp.content) # writing content to file

                if not os.path.isfile(videoFilepath):
                    print(f"FAILED 1: {link}")
                    failedLinks.append(link)

                newLine = json.dumps({ link: videoFilepath }) + '\n'
                outfile.write( newLine )
                numDownloaded += 1
                print(f"downloaded mp4 {numDownloaded} of {TOTAL_MP4_LINKS} - {link}")

            except:
                print(f"FAILED 2: {link}")
                failedLinks.append(link)            

    print(f"There were {len(failedLinks)} failed links:")
    for link in failedLinks:
        print(link)


def main():
    mp4Links = getMp4UrlsToDownload()
    downloadMp4s(mp4Links)


main()