import os

username = os.getlogin()
source = "prueba1"
destination = "C:\\Users\\" + username + "\\Desktop\\prueba1"

try:
    if os.path.exists(destination):
        print("The destination is already occupied")
    else:
        os.replace(source, destination)
        print(source, "was moved")
except FileNotFoundError:
    print("Error file not found :3")
