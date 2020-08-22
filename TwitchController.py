#Required Libraries
import socket
import threading
import userinfo
import time
import twitchlogo
#Recogmended Libraries
import random
import pynput
import pyautogui
import keyboard
import mouse

global special_char
global capital_char
special_char = ['!','@',"#","$","%","^","&","*","(",")","?",]
capital_char = ['A',"B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

message = ' '
user = ' '

def program():
    twitchlogo.print_twitch_logo()
    SERVER = "irc.twitch.tv"
    PORT = 6667


    PASS = userinfo.PASS


    BOT = userinfo.BOT


    CHANNEL = userinfo.CHANNEL


    OWNER = userinfo.OWNER


    irc = socket.socket()

    irc.connect((SERVER, PORT))
    irc.send((	"PASS " + PASS + "\n" +
                "NICK " + BOT + "\n" +
                "JOIN #" + CHANNEL + "\n").encode())



    #Example of Twitch Bot Commands Setup
    def commands():
        global message
        global user
        while True:

            def UniqueChar(char):
                keyboard.press('shift')
                keyboard.press(char)
                keyboard.release(char)
                keyboard.release('shift')


            if message.lower() == '!taco':
                sendMessage(irc, "It's Taco Time!")
                message = ''
                return
            
            #used if typying somthign like a story otherwise just delete it.    
            if message.lower() == 'new paragraph':
                attempt = random.randint(1,2)
                if attempt == 2:
                    keyboard.press('enter')
                    keyboard.release('enter')
                    keyboard.press('enter')
                    keyboard.release('enter')
                    keyboard.press('tab')
                    keyboard.release('tab')
                    message=''
                    return
                else:
                    message=''
                    return
            #Types a Message Using Keyboard based on twitch input
                #Currently types everything but working on getting it to only type words after the word type!
            try:
                if 'type' in message.lower():
                    #message = message.lower()
                    new_msg = message.split('type')
                    new_msg = message.split(' ')
                    #Used to check number of words in message string
                    constructor = []
                    #Used to create finalized constructor list
                    final = []
                    #used to create final string
                    string = []
                    #Checks for bad windows Characters
                    apas_builder = []
                    for scentence in new_msg:           
                        constructor.append(scentence)
                    #Limits Max number of words allowed to be typed, It is num - 2.
                    # Ex.) If >=7 then 5 words can be typed.
                    if len(constructor) >= 22000:
                        message=''
                        return
                    else:
                        for word in constructor:
                            final.append(word)
                        final_place = final.index('type')
                        for word in final[final_place+1:]:
                            #This is an apple character that can't be used on windows machines. 
                            #If you want to get rid of another puncuation or find a punctuation that causes an error, add it here with a or statement
                            # ex(if "’" in word or if "symbol" in word:)
                            if "’" in word:
                                for letter in word:
                                    if letter == "’":
                                        continue
                                    else:
                                        apas_builder.append(letter)
                                word = ''.join(apas_builder)
                                apas_builder = []
                            string.append(word)
                    for word in constructor:
                        #Checks if word is longer than 15 characters if it is the message doesn't send.
                        if len(word) >=15000:
                            print(word)
                            message=''
                            return
                    #For Minecraft Un-Comment
                    #PressAndHoldKey('t',0.1)
                    for word in string:
                        #If a character such as ! is in message, checks and makes sure the correct button is caitalized 
                        for char in word:
                            if char in capital_char:
                                char = char.lower()
                                UniqueChar(char)
                                continue
                            if char in special_char:
                                UniqueChar(char)
                            else:
                                keyboard.press(char)
                                keyboard.release(char)
                        keyboard.press('space')
                        keyboard.release('space')
                    #For Minecraft Un-Comment
                    #PressAndHoldKey('enter',0.1)
                return
            except:
                message=''
                return

            
            else:
                return
    def gamecontrol():
        global message
        global user

        global PressAndHoldKey
        def PressAndHoldKey(key, seconds):
            keyboard.press(key)
            time.sleep(seconds)
            keyboard.release(key)

        def PressAndHold2Key(key1,key2,seconds): #If You Need More Keys Just continue The pattern, create another def add key3
            keyboard.press(key1)
            keyboard.press(key2)
            time.sleep(seconds)
            keyboard.release(key1)
            keyboard.release(key2)

        def HoldKey(key):
            keyboard.press(key)

        def ReleaseKey(key):
            keyboard.press(key)

        def MouseClick(key,seconds):#key means left or right for this one
            mouse.press(button = key)
            #Mouse has a timer otherwise left click may not get registerd in some games it can be 0.1 seconds
            time.sleep(seconds)
            mouse.release(button = key)

        def MouseTurn(x,y,seconds):
            pyautogui.moveRel(x, y, duration = seconds) 
        
        #Chance That Twitch Command Will Run Needs two number x = smaller number y = larger number
        def ActionChance(x,y):
            chance = random.randint(x,y)
            return chance

        while True:
            #Minecraft

            
        

            #left click is what people would type in chat to make this command happen
            #MouseClick calls the function up above to make it happen. it required two inputs, the button (left or right) to be pressed, and the time to be pressed. 
            if message.lower() == 'left click':
                chance = ActionChance(1,2)
                if chance == 2:
                    break
                MouseClick('left',2)
                message = ''
                return
            
            #Twitch chat would need to type forward or w to make this command happen 
            #PressAndHoldKey calls the function up above to make it happen, it required two inputs, the key to press and the time to be pressed.
            if message.lower() == 'forward' or message.lower() == 'w':
                #50% chance Command will run. Runs on Odd Numbers 
                if ActionChance(1,10) % 2 == 0:
                    break
                PressAndHoldKey('w',5)
                message=''
                return

            if message.lower() == 'back' or message.lower() == 's':
                #10% Chance command will run
                if ActionChance(1,10) != 5:
                    break
                PressAndHoldKey('s',2)
                message = ''
                return

            if message.lower() == 'left' or message.lower() == 'port' or message.lower() == 'a':
                PressAndHoldKey('a',2)
                message = ''
                return

            if message.lower() == 'right' or message.lower() == 'starboard' or message.lower() == 'd':
                PressAndHoldKey('d',2)
                message = ''
                return

            if message.lower() == 'jump':
                PressAndHoldKey('space',2)
                message = ''
                return

            if message.lower() == 'crouch':
                PressAndHoldKey('shift',2)
                message = ''
                return

            if message.lower() == 'run' or message.lower() == 'sprint': 
                if ActionChance(1,2) == 2:
                    break
                HoldKey('control')
                PressAndHoldKey('w',2)
                ReleaseKey('control')
                message = ''
                return

            #You may need to experiment with turning angels and time. This turns you about 90° to the right in MC
            if message.lower() == 'turn right':
                MouseTurn(60,0,1)
                message = ''
                return
            
            else:
                return

    #Connects You to Twitch Servers and starts other groups (i.e Controller and Commands)
    #You Should Not Need to Change Anything in the Twitch Section
    def twitch():
        
        global user
        global message

        def joinchat():
            Loading = True
            while Loading:
                readbuffer_join = irc.recv(1024)
                readbuffer_join = readbuffer_join.decode()                
                for line in readbuffer_join.split("\n")[0:-1]:                    
                    Loading = loadingComplete(line)
        def loadingComplete(line):
            if("End of /NAMES list" in line):
                #sendMessage(irc, "Hello World!")
                return False
            else:
                return True
        global sendMessage
        def sendMessage(irc, message):
            messageTemp = "PRIVMSG #" + CHANNEL + " :" + message
            irc.send((messageTemp + "\n").encode())
        def getUser(line):
            global user
            colons = line.count(":")
            colonless = colons-1
            separate = line.split(":", colons)
            user = separate[colonless].split("!", 1)[0]
            return user
        def getMessage(line):
            global message
            try:
                colons = line.count(":")
                message = (line.split(":", colons))[colons]
            except:
                message = ""
            return message
        def console(line):
            if "PRIVMSG" in line:
                return False
            else:
                return True
        while True:
            try:
                readbuffer = irc.recv(1024).decode()
            except:
                readbuffer = ""
            for line in readbuffer.split("\r\n"):
                if line == "":
                    continue
                if "PING :tmi.twitch.tv" in line:
                    
                    msgg = "PONG :tmi.twitch.tv\r\n".encode()
                    irc.send(msgg)
                    continue
                else:
                    
                    global user
                    
                    user = getUser(line)
                    message = getMessage(line)
                    print(user + " : " + message)
                    gamecontrol()
                    commands()
                    message=''
                    
        
        joinchat()
        
        
        
                    
                    


    t1 = threading.Thread(target = twitch)
    t1.start()
    t2 = threading.Thread(target = gamecontrol)
    t2. start()
    t3 = threading.Thread(target = commands)
    t3.start()
