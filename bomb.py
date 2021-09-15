import requests

logo = """
██████    █████   ██     ██  ██████   ███████  ██████ 
█     █  █     █  █ █   █ █  █     █  █        █     █
█     █  █     █  █ █   █ █  █     █  █        █     █
██████   █     █  █  █ █  █  ██████   ███████  ██████ 
█     █  █     █  █  █ █  █  █     █  █        █     █
█     █  █     █  █   █   █  █     █  █        █     █
██████    █████   █       █  ██████   ███████  █     █
"""

about = """About""" #TODO: ADD INFO

Base = {}

def start(num):
	i = 0
	while i < len(Base):
		requests.get(Base[0].format(num))
		i += 1

def update():
	print("In development")