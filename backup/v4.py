import os

username = os.getlogin()
source = input("Como se llama el archivo que quieres mover? ")
file_name = input("Como quieres que se llame el archivo? (Dejar en blanco si el nombre sera el mismo)")

try:
    if len(file_name.strip()) > 0:
        print("this will be " + file_name + ".")
    else:
        print("no")
finally:
    print("done")



#destination = "C:\\Users\\" + username + "\\AppData\\Roaming\\.minecraft\\Lunar Client\\resourcepacks\\" + file_name


#try:
#    if os.path.exists(destination):
#        print("The destination is already occupied")
#    else:
#        os.replace(source, destination)
#        print(source, "was moved")
#except FileNotFoundError:
#    print("Error file not found :3")
