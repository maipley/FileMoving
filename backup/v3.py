import os

username = os.getlogin()
source = input("Como se llama el archivo que quieres mover? ")
destination = "C:\\Users\\" + username + "\\AppData\\Roaming\\.minecraft\\Lunar Client\\resourcepacks\\" + source

try:
    if os.path.exists(destination):
        print("The destination is already occupied")
    else:
        os.replace(source, destination)
        print(source, "was moved")
except FileNotFoundError:
    print("Error file not found :3")
