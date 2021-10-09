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
    print("1. Start bombing!\n2. Update base\n3. Change language/Сменить язык\n4. About\n5. Exit")
    action = input("Choose the action: ")

    if action == "1":
        num = ""
        delay = 0

        while True:
            num = input("Enter phone number(In international format): ")
            if num.startswith("+") and num[1:-1].isdigit():
                break
            else:
                print("Incorrect number")
                continue

        while True:
            try:
                delay = int(input("Enter delay(in seconds): "))
                break
            except ValueError:
                print("Enter ONLY numbers")
                continue

        try:
            bomb.start(num, delay)
        except bomb.requests.exceptions.ConnectionError:
            bomb.InternetError()

        continue
    elif action == "2":
        try:
            bomb.update()
        except bomb.requests.exceptions.ConnectionError:
            bomb.InternetError()
        continue
    elif action == "3":
        bomb.changeLang()
    elif action == "4":
        print("\n" + bomb.about)
        input()
        continue
    elif action == "5":
        answer = str(input("Are you sure(y/n): "))
        answer.lower()
        if answer == "y" or answer == "yes":
            break
        else:
            continue
    else:
        print("Unknown command: " + action)
        continue
