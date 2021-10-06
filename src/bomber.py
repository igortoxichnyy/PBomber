import bomb

print(bomb.logo)

#Check internet connection
print("Internet connection... ", end="")

try:
    bomb.checkInternet()
except bomb.requests.exceptions.ConnectionError:
    bomb.InternetError()

print("OK!")

#Initialize base from baset.txt
print("Initialization base... ", end="")

if bomb.os.stat(bomb.filename).st_size == 0:
    bomb.update()

i = 0
while True:
    line = bomb.basefile.readline()
    if line == "":
        break
    else:
       bomb.Base[i] = line
    i += 1

print("OK!")

print("\nWelcome to the bomber!\n")

#Menu
while True:
    print("1. Start bombing!\n2. Update base\n3. About\n4. Exit")
    action = input("Choose the action: ")

    if action == "1":
        while True:
            num = input("Enter phone number(In international format): ")
            if num.startswith("+") and num[1:-1].isdigit():
                try:
                    bomb.start(num)
                except bomb.requests.exceptions.ConnectionError:
                    bomb.InternetError()
                break
            else:
                print("Incorrect number")
                continue
        continue
    elif action == "2":
        try:
            bomb.update()
        except bomb.requests.exceptions.ConnectionError:
            bomb.InternetError()
        continue
    elif action == "3":
        print("\n" + bomb.about)
        input()
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
