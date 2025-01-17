#Wymagane Libraries w Pythonie. Zgarniesz je używajac pip install. Część z nich jest preinstalled lecz na pewno Socket jest do zgarniecia osobno.
import socket
import threading
import userinfo
import time
import twitchlogo
#Rekomendowane Libraries. Bierz je wszystkie jak chcesz ciagnąć inputy z chatu.
import random
import pyautogui
import keyboard
import mouse

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

            if message.lower() == 'down':
                PressAndHoldKey('down',2)
                return

            if message.lower() == 'left':
                PressAndHoldKey('left',2)
                return

            if message.lower() == 'right':
                PressAndHoldKey('right',2)
                return

            if message.lower() == 'up':
                PressAndHoldKey('up',2)
                return

            if message.lower() == 'a':
                PressAndHoldKey('a',2)
                return
            
            if message.lower() == 'b':
                PressAndHoldKey('b',2)
                return

            if message.lower() == 'x':
                PressAndHoldKey('x',2)
                return

            if message.lower() == 'y':
                PressAndHoldKey('y',2)
                return

            if message.lower() == 'z':
                PressAndHoldKey('z',2)
                return

            if message.lower() == 'dpad_up':
                PressAndHoldKey('t',2)
                return

            if message.lower() == 'dpad_down':
                PressAndHoldKey('g',2)
                return

            if message.lower() == 'dpad_left':
                PressAndHoldKey('f',2)
                return

            if message.lower() == 'dpad_right':
                PressAndHoldKey('h',2)
                return

            if message.lower() == 'stick_up':
                PressAndHoldKey('i',2)
                return

            if message.lower() == 'stick_down':
                PressAndHoldKey('k',2)
                return

            if message.lower() == 'stick_left':
                PressAndHoldKey('j',2)
                return

            if message.lower() == 'stick_right':
                PressAndHoldKey('l',2)
                return
            
            if message.lower() == 'trigger_l':
                PressAndHoldKey('q',2)
                return

            if message.lower() == 'trigger_r':
                PressAndHoldKey('w',2)
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

#you cheeky bastard, widze ze gapisz mi sie na bebech koda