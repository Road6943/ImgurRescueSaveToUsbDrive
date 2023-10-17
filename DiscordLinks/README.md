The parent folder is for imgur links, and instructions there are for imgur link stuff. This readme in the DiscordLinks child folder will tell you how to extract discord links into a file. After running the stuff in this folder (from this folder's location in the terminal) and creating said file, you will need to change the input file path variable in the download images and download videos scripts in the parent (imgur) folder and then run them from the **parent folder level** in terminal.


Steps:
- Go to https://docs.google.com/spreadsheets/d/1nFbWgW8WCT9Xsgj-SVQ1s2jjKDIs1qfWLCjtQYbAdVg/edit#gid=895734689
- Make a copy of that spreadsheet
- In the copy, go to "Extensions > Apps Script"
- Make a new Apps Script and copy the contents of export_csv_..... into the new apps script file
- Run the Apps Script file, then go to google drive and locate the resulting folder
- Download said folder and expand it to get a folder of csv files
- Move that folder into this DiscordLinks folder, and rename it to "csv_files"
- Make sure the variable in extractDiscordLinks.py is also "csv_files"
- Run extractDiscordLinks.py to create the new text files of links
- Switch terminal to parent folder
- In downloadImages.py, switch input file variable path, but keep the download folder name the same at ImgurBackups
- Run downloadImages, and maybe downloadVideos too, from the parent folder level in terminal (aka the same as downloading imgur stuff)
- Look over the failedLinks.html file to make sure the links are actually broken and not salvageable
- Copy the imgdl.log file in this directory to your usb drive