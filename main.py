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

def start():
    number = input("Enter number(in international format): ")

    i = 0
    while i < len(Base):
        requests.get(Base[i].format(number))
        i += 1

def update():
    print("In development")

print(logo)

print("Internet connection... ", end="")
#TODO: MAKE CHECK INTERNET CONNECTION
print("OK!")

print("Initialization base... ", end="")

file = open("base.txt", "r")

i = 0
while True:
    line = file.readline()
    if line == "":
        break
    else:
        Base[i] = line
    i += 1

print("OK!")

print("\nWelcome to the bomber!\n")

while True:
    print("1. Start bombing!\n2. Update base\n3. About\n4. Exit")
    action = input("Choose the action: ")

    if action == "1":
        start()
        continue
    elif action == "2":
        update()
        continue
    elif action == "3":
        print(about)
        continue
    elif action == "4":
        answer = input("Are you sure(y/n): ")
        answer.lower()
        if answer == "y" or answer == "yes":
            break
        else:
            continue
    else:
        print("Unknown command: " + action)
        continue