# TwitchController-v1.3 aka Twitch Plays Bot

***NEWEST VERSION*** 
The newest update made on 10/2/2020 makes the program run much more effiecntly doing multiple and all commands at once instead of doing one then waiting. 

Used to allow your computer to receive your twitch chat, to control your keyboard or to create your own twitch bot!


Make Sure You Add Your Info to userinfo.py

Download Sockets.py library
<br/>
Download recommended & required libaries which can be found at the top of the TwitchController.py file!

Everything else should work. 


If You Have Already Downloaded this Porject. I recogmend just Taking the New Parts of Updates That You Like

Known Errors: Did You Find an Error? Report it Here -> https://forms.gle/B5hKGd3sT6qGgrrB9

Check Changelogs for resolved errors.

Changelogs: Check Here for Updates
- 7/9/2020
  - Added a "type" command that allows twitch chat users to type a maximum of 8 words (this can be changed in the type section, in the group Commands)
  - Added a "Click" command that allows twitch chat users to click the left mouse button (You can change this in Click section, in the group Game Control)
  - Fixed Type Error, where the ' key would break the program. (This is an apple Uni-code symbol that does not exist on windows)
    - Current Resolution: Delete ' from re-typing. 
       - ToDo: Have symbol get changed to default ' key for windows usage

- 7/10/2020
  - Added an incomplete special Chars Library for typing command that allows users to type characters such as !,?,# etc...
  - Add to the library by adding ,"key" to the end of the speical_chars list.
  - ToDo: Move Commands to Seperate python file and call them from main file to make future updates easier.
  - Added comments to differnt aspects to add clarification.
  - Add limits to type command that can be changed. i.e) Max Number of Words Allowed and Max Number of Letters Allowed in a Word
    - This can be changed in the Commands typing section where they are marked with comments. 
  - Fixed Error where if user used type command with capital letters it would not input properly.
  - Fixed Error where some capital letters would break in typing command.
    - Current Solution turn message into lowercase from the start of program, this shouldnt have any negative effects on commands if they search for lowercase, otherwise you may need to change. 
  - Added a Paragraph command that creates a new paragraph. It has a 50% chance of working but can be changed to be 100% if required.
    - Ex) All you have to do is type "new paragraph"
<br />
<br />
- 7/12/2020
  - Created keyboard and mouse functions to make reading better and make coding easier for non-coders. 
  - Fixed Capitilizations Errors with Type command
<br />
<br />
- 7/14/2020
  - Added Twitch Controller Logo at Start of Console at Launch
<br />
<br />
- 8/28/2020
  - Production is currently halted.
  - This is open source feel free to download and edit it as much as you want!  
<br />
<br />
- If You Want to Demonstrate this Code in a Video Please Give Me Proper Creds :) that would be nice of you!
<br/>
- If You Appreciate This Consider Following me on Twitch: https://www.twitch.tv/henryfundenberger




