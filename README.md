# File_Management_Automation

Script to automate the organization of files and folders on my computer. 

Files in user-selected folder move to the appropriate folder based on their **file type**, after automatically **renaming** files if they contain spaces.

The appropriate folders are these:
* Documents: pdf, docx, xlsx, csv, ppt
* Music: mp3, aac, ogg, flac, wav
* Pictures: svg, png, jpg, jpeg, 
* Videos: mp4, mkv

If the file type matches none of the above, it stores it in **Documents\Extras** folder.

All transfers are logged.

The source folder can easily be changed by passing a command line argument.
The file types for the destination folders can also be changed.