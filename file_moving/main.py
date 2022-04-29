import os

username = os.getlogin()
actualdir = os.getcwd()
file_name = input("Como se llama el archivo que quieres mover? ")
tempdir = actualdir[:-11] + file_name
source = tempdir.replace('\\', '\\\\')
new_file_name = input("Como quieres que se llame el archivo? (Dejar en blanco si el nombre sera el mismo) ")
destination = "C:\\Users\\" + username + "\\AppData\\Roaming\\.minecraft\\Lunar Client\\resourcepacks\\"
destpath = 0


try:
    if len(new_file_name.strip()) > 0:  # It checks if the new name lenght is greater than 0
        destpath = destination + new_file_name  # Defines the destpath variable value
        try:
            if os.path.exists(destpath):  # Checks if a file with the same name already exists in the destination
                print("The destination is already occupied")
            else:
                os.replace(source, destpath)  # Moves the file
                print(file_name, "was moved and the new name is", new_file_name)
        except FileNotFoundError:  # Error result, this acts if all the above goes wrong
            print("Error file not found c:")
    else:
        destpath = destination + file_name  # Defines the destpath variable value
        try:
            if os.path.exists(destpath):
                print("The destination is already occupied")
            else:
                os.replace(source, destpath)
                print(file_name, "was moved")
        except FileNotFoundError:
            print("Error file not found c:")
except FileNotFoundError:
    print("Task failed idk why")
