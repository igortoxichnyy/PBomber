import requests
import urllib

logo = """
=======      =====    ||\\     /||  =======    =======  ======= 
||     ||  ||     ||  || |   | ||  ||     ||  ||       ||     ||
||     ||  ||     ||  || \\   / ||  ||     ||  ||       ||     ||
||=====    ||     ||  ||  | |  ||  ||=====    ||=====  ||===== 
||     ||  ||     ||  ||  \\ /  ||  ||     ||  ||       ||     ||
||     ||  ||     ||  ||   -   ||  ||     ||  ||       ||     ||
=======      =====    ||       ||  =======    =======  ||     ||
"""

about = "PBomber - SMS Bomber, written on Python. Created By IgorToxichnyy."

Base = {}

def start(num):
	i = 0
	while i < len(Base):
		requests.get(Base[0].format(num))
		i += 1

def update():
	print(requests.get("https://raw.githubusercontent.com/igortoxichnyy/PBomber/main/bomb.py").content)

if __name__ == '__main__':
	update()