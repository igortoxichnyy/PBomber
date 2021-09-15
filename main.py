import bomb

print(bomb.logo)

#Check internet connection
print("Internet connection... ", end="")

#TODO: MAKE CHECK INTERNET CONNECTION

print("OK!")

#Initialize base from baset.txt
print("Initialization base... ", end="")

file = open("base.txt", "r")

i = 0
while True:
    line = file.readline()
    if line == "":
        break
    else:
        bomb.Base[i] = line
    i += 1

print("OK!")

print("\nWelcome to the bomber!\n")

while True:
    print("1. Start bombing!\n2. Update base\n3. About\n4. Exit")
    action = input("Choose the action: ")

    if action == "1":
        num = input("Enter phone number(In international format): ")
        bomb.start(num)
        continue
    elif action == "2":
        bomb.update()
        continue
    elif action == "3":
        print(bomb.about)
        continue
    elif action == "4":
        answer = str(input("Are you sure(y/n): "))
        answer.lower()
        if answer == "y" or answer == "yes":
            break
        else:
            continue
    else:
        print("Unknown command: " + action)
        continue