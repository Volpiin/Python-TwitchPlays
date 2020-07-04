import socket
import threading
import userinfo
import os
import time

#Recogmended Libraries
import pynput
import pyautogui
import keyboard


message = ' '
user = ' '

def program():
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
            if message.lower() == '!taco':
                sendMessage(irc, "It's Taco Time!")
                message = ''
                return
            else:
                message = ''
                return

    def gamecontrol():
        global message
        global user
        while True:
            #Minecraft
            if message.lower() == 'forward' or message.lower() == 'w':
                keyboard.press('w')
                time.sleep(5)
                message = ''
                keyboard.release('w')
                return
            if message.lower() == 'back' or message.lower() == 's':
                keyboard.press('s')
                time.sleep(2)
                message = ''
                keyboard.release('s')
                return
            if message.lower() == 'left' or message.lower() == 'port' or message.lower() == 'a':
                keyboard.press('a')
                time.sleep(2)
                message = ''
                keyboard.release('a')
                return
            if message.lower() == 'right' or message.lower() == 'starboard' or message.lower() == 'd':
                keyboard.press('d')
                time.sleep(2)
                message = ''
                keyboard.release('d')
                return
            if message.lower() == 'jump':
                keyboard.press('space')
                time.sleep(1)
                keyboard.release("space")
                message = ''
                return
            if message.lower() == 'crouch':
                keyboard.press('shift')
                time.sleep(2)
                keyboard.release('shift')
                message = ''
                return
            if message.lower() == 'run' or message.lower() == 'sprint':
                keyboard.press('w')
                keyboard.press('control')
                message = ''
                time.sleep(3)
                keyboard.release('w')
                keyboard.release('control')
                return
            if message.lower() == 'turn right':
                pyautogui.moveRel(60, 0, duration = 1) 
                message = ''
                return
            
            else:
                message == ''
                return
            continue
    
    #Connects You to Twitch Servers and starts other groups (i.e Controller and Commands)
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
                print("Bot Succesfuly Connected")
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

        joinchat()
        
        
        while True:
            try:
                readbuffer = irc.recv(1024).decode()
            except:
                readbuffer = ""
            for line in readbuffer.split("\r\n"):
                if line == "":
                    continue
                if "PING :tmi.twitch.tv" in line:
                    print(line)
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
                    


    t1 = threading.Thread(target = twitch)
    t1.start()
    t2 = threading.Thread(target = gamecontrol)
    t2. start()
    t3 = threading.Thread(target = commands)
    t3.start()
