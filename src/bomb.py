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

about = "PBomber - SMS Bomber, written on Python. Created By IgorToxichnyy."

Base = {}

def check_internet():
    requests.get("https://www.google.com/")

def start(num, delay):
    i = 0
    while i < len(Base):
        requests.get(Base[i].format(num))
        print(Base[i].format(num))
        time.sleep(delay)
        i += 1

def update():
    pass

#       url=list(str(requests.get("https://raw.githubusercontent.com/igortoxichnyy/PBomber/main/base.txt").content))
#
#   del url[0]
#
#   i = 0
#   while i < len(url):
#       if url[i] == "'":
#           del url[i]
#           i+=1
#       elif url[i] == "\\":
#           if url[i+1] == "r":
#               del url[i]
#               del url[i]
#           elif url[i+1] == "n":
#               del url[i]
#               url[i] = "\n"
#               i+=1
#           elif url[i+1] == "\\":
#               i+=2
#       else:
#           i+=1
#
#   #TODO: MAKE WRITE ON FILE, AFTER CLEAN FILE
#   #TODO: MAKE TRY...EXCEPT, FOR CATCHING INTERNET CONNECTION EXCEPTIONS

if __name__ == '__main__':
    update()
