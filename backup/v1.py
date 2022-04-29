import os

username = os.getlogin()
source = "juan.txt"
destination = "C:\\Users\\" + username + "\\Desktop\\mariano.txt"

try:
    if os.path.exists(destination):
        with open('juan.txt', 'w') as f:
            f.write('Create a new text file!')
        os.remove(destination)
    else:
        os.replace(source, destination)
        print(source, "was moved")
except FileNotFoundError:
    with open('juan.txt', 'w') as f:
        f.write('Create a new text file!')