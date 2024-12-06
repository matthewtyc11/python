import hashlib
import secrets

data = {}
while True:
    WhatToDo = input("What to do \n1 = Make account \n2 = Login \n3 = Get all data \n")
    if WhatToDo == "1":
        UserName = input("account name ")
        UserPassword = input("password ")
        Random = secrets.token_hex(32)
        data[UserName] = {
            "Name": UserName,
            "Password": hashlib.sha1((UserPassword + Random).encode(encoding='UTF-8')).hexdigest(),
            "Random": Random
        }
    elif WhatToDo == "2":
        InputUserName = input("account name ")
        try:
            UserSavedData = data[InputUserName]
        except KeyError:
            print("This user does not exist!")
            continue  # Go back to the beginning of the loop
        else:
            while True:
                InputUserPassword = input("password ")
                Random = UserSavedData["Random"]
                HashedPassword = hashlib.sha1((InputUserPassword + Random).encode(encoding='UTF-8')).hexdigest()
                
                if HashedPassword == UserSavedData["Password"]:
                    print("Logged in")
                else:
                    print("Wrong password")
                    # Ask if they want to try again
                    retry = input("Do you want to try again? (yes/no) ").strip().lower()
                    if retry != "yes":
                        break  # Exit the password loop, go back to main menu
    elif WhatToDo == "3":
        print(data)