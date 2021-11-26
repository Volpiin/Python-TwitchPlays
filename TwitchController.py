#Wymagane Libraries w Pythonie. Zgarniesz je używajac pip install. Część z nich jest preinstalled lecz na pewno Socket jest do zgarniecia osobno.
import socket
import threading
import userinfo
import time
import twitchlogo
#Rekomendowane Libraries. Bierz je wszystkie jak chcesz ciagnąć inputy z chatu.
import random
import pynput
import pyautogui
import keyboard
import mouse
import pydirectinput

global special_char
global capital_char
global command_cooldown
command_cooldown = []
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


    
    #Przykładowe komendy, wzoruj sie na nich jak chcesz coś zaimplementować.
    
    def gamecontrol():
        global message
        global user
       
        def PressAndHoldKey(key, seconds):
            keyboard.press(key)
            time.sleep(seconds)
            keyboard.release(key)

        def PressAndHold2Key(key1,key2,seconds): #Jak potrzebujesz więcej przycisków - trzymaj sie patternu widocznego tutaj - def add key3 etc.
            keyboard.press(key1)
            keyboard.press(key2)
            time.sleep(seconds)
            keyboard.release(key1)
            keyboard.release(key2)

        def HoldKey(key):
            keyboard.press(key)

        def ReleaseKey(key):
            keyboard.release(key)

        def MouseClick(key,seconds): #key = left bądź right w tym przypadku
            mouse.press(button = key)
            #Przyciski myszy MUSZĄ mieć timer inaczej nie zostaną zarejestrowane. Zazwyczaj 0.1 sekundy w niektórych grach, kwestia tweakowania i testów.
            time.sleep(seconds)
            mouse.release(button = key)

        def MouseTurn(x,y,seconds):
            pyautogui.moveRel(x,y,seconds)
            return
            
        
        #TODO: przetestuj to gówno - Chance That Twitch Command Will Run Needs two number x = smaller number y = larger number
        def ActionChance(x,y):
            chance = random.randint(x,y)
            return chance
        
        while True:
            #Przykład pod Minecrafta



            #"left click" na chacie sprawi że ta komenda sie aktywuje
            #MouseClick odwołuje sie do funkcji wpisanej wyżej by to zadziałało.
            #Wymagane dwa inputy 0 przycisk oraz czas do naciśniecia
            if message.lower() == 'left click':

                MouseClick('left',2)
                return
            
            #Czat musi wpisac "forward" bądź "w" by ta komenda zadziałała
            #PressAndHoldKey odwołuje sie do funkcji wpisanej wyżej by to zadziałało.
            #Wymagane dwa inputy - przycisk oraz czas do naciśniecia
            if message.lower() == 'forward' or message.lower() == 'w':
                #50% szansy że komenda sie odpali. Działa na liczbach nieparzystych.
                if ActionChance(1,10) % 2 == 0:
                    break
                PressAndHoldKey('w',5)
                return

            if message.lower() == 'back' or message.lower() == 's':
                #10% szansy że komenda sie odpali
                if ActionChance(4,5) != 5:
                    break
                PressAndHoldKey('s',2)
                return

            if message.lower() == 'left' or message.lower() == 'port' or message.lower() == 'a':
                PressAndHoldKey('a',10)
                return

            if message.lower() == 'right' or message.lower() == 'starboard' or message.lower() == 'd':
                PressAndHoldKey('d',2)
                return

            if message.lower() == 'jump':
                PressAndHoldKey('space',2)
                return

            if message.lower() == 'crouch':
                PressAndHoldKey('shift',2)
                return

            if message.lower() == 'run' or message.lower() == 'sprint': 
                if ActionChance(1,2) == 2:
                    break
                HoldKey('control')
                PressAndHoldKey('w',2)
                ReleaseKey('control')
                
                return
#********************************************************************
            #Wpływ na obrót kamery ma sens myszki w grze. To powinno na domyślnym MC obrócić kamere o 90 stopni. Wymaga eksperymentowania z kątem i czasem.
            if message.lower() == 'turn right':
                MouseTurn(60,0,1)
                
                return
            
            else:
                message == ''
                return
            message=''  
            return

        
    #kod łaczący z Twitchem i startujacym reszte kodu.
    #Nie ruszamy tutaj nic w sekcji kodu Twitchowego, not worth i nic to nie da
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
                    t2 = threading.Thread(target = gamecontrol)
                    t2. start()       
        joinchat()
    t1 = threading.Thread(target = twitch)
    t1.start()
