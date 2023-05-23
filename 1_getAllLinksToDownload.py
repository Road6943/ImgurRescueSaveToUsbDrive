# Run with `python3 <filename>`
# This file generates 2 giant .txt files, with all the imgur and cloudinary links respectively 

arrasNewLinksFiles = [
    "../imgur_rescue/newLinks.jsonl",
    "../imgur_rescue_EvenOlder_and_Oldest_Submissions/newLinks.jsonl",
]

diepNewLinksFiles = [
    "../imgur_rescue/diep/DiepWraImgurBackupLinks.jsonl"
]

imgurOutputFile = "1_linksImgur.txt"
cloudinaryOutputFile = "1_linksCloudinary.txt"

# ===============================================

import json


def getImgurLinks():
    with open(imgurOutputFile, 'w') as imgurFile, open(cloudinaryOutputFile, 'w') as cloudFile: 

        for filepath in arrasNewLinksFiles:
            with open(filepath) as file:
                for line in file:
                    hashmap = json.loads(line)
                    imgurFile.write( hashmap['oldImgurLink'] + "\n" )
                    cloudFile.write( hashmap['newLink'] + "\n" )

        for filepath in diepNewLinksFiles:
            with open(filepath) as file:
                for line in file:
                    hashmap = json.loads(line)
                    for imgurLink,cloudinaryLink in hashmap.items():

                        if imgurLink in ['https://imgur.com/a/qhzJj']:
                            continue

                        if cloudinaryLink in ["https://ibb.co/album/NrRw8d?sort=name_asc&page=1"]:
                            continue

                        imgurFile.write( imgurLink + "\n" )
                        cloudFile.write( cloudinaryLink + "\n" )

getImgurLinks()