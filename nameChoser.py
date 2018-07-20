names = []
running = True
import random

def menu():
    res = ""
    res += "==================\n"
    res += "RANDOM NAME CHOSER\n"
    res += "==================\n"
    res += "1. Pick a Name\n"
    res += "2. Add a Name\n"
    res += "3. List Names\n"
    res += "4. Clear Names\n"
    res += "5. Remove a name\n"
    res += "6. Load Names From File\n"
    res += "7. Quit\n"
    return res

def pickName():
    if len(names)==0:
        print("No names to choose from.")
        return
    print("Chosen Name: " + random.choice(names))

def addName():
    name = input("Enter the name to add: ")
    names.append(name)
    print(name + " Added To List")

def listNames():
    if len(names)==0:
        print("No names in list.")
        return
    print("ALL NAMES:")
    for n in names:
        print("\t" + n)

def clear():
    names.clear()
    print("Cleared Name List")

def removeName():
    toRemove = input("Enter the name to remove: ")
    try:
        names.remove(toRemove)
        print("First occurence of " + toRemove + " has been removed.")
    except ValueError:
        print(toRemove + " is not in name list.")

def loadFile():
    filename = input("Enter the path to the file: ")
    try:
        with open(filename) as lns:
            for l in lns:
                names.append(l.strip())
            print("Loaded names from " + filename)
    except FileNotFoundError:
        print("File not found error!")


while(running):
    print(menu())
    choice = input("=> ")
    if choice == "1":
        pickName()
    elif choice == "2":
        addName()
    elif choice == "3":
        listNames()
    elif choice == "4":
        clear()
    elif choice == "5":
        removeName()
    elif choice == "6":
        loadFile()
    elif choice == "7":
        running = False
    else:
        print("INVALID CHOICE")
