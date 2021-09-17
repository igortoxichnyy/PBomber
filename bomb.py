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
	#i dont know how to correct this bug
	pass