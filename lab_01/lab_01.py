list = [
    {"name": "Bob", "phone": "0631234567", "address": "Shevchenko St., 5", "date": "11.06.2003"},
    {"name": "Emma", "phone": "0638888888", "address": "Vesniana St., 45a", "date": "16.03.2002"},
    {"name": "Jon", "phone": "0635555555", "address": "Pivchna St., 4", "date": "29.01.2004"},
    {"name": "Zak", "phone": "0630000000", "address": "Musical St., 167b", "date": "24.07.2003"}
]


def printAllList():
    for elem in list:
         print(f"{elem['name']}, {elem['phone']}, {elem['address']}, {elem['date']}")

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    address = input("Please enter student address: ")
    date = input("Please enter student date of birth: ")
    newS = {"name": name, "phone": phone, "address": address, "date": date}

    pos = 0
    for elem in list:
        if name > elem["name"]:
            pos += 1
        else:
            break
    list.insert(pos, newS)
    print("Added")

def deleteElement():
    name = input("Please enter name to be delated: ")
    for elem in list:
        if elem["name"] == name:
            list.remove(elem)
            print("Deleted")
            return
    print("Student not found")

def updateElement():
    name = input("Please enter name to be updated: ")
    for elem in list:
        if elem["name"] == name:
            elem["name"] = input("New name: ")
            elem["phone"] = input("New phone: ")
            elem["address"] = input("New address: ")
            elem["date"] = input("New date of birth: ")

            list.sort(key=lambda x: x["name"])
            print("Updated")
            return
    print("Student not found")

def main():
    while True:
        choice = input("\nPlease specify the action [ C create, U update, D delete, P print,  X exit ] ").lower()

        if choice == "c":
            addNewElement()
        elif choice == "u":
            updateElement()
        elif choice == "d":
            deleteElement()
        elif choice == "p":
            printAllList()
        elif choice == "x":
            print("Exit.")
            break
        else:
            print("Wrong choice!")

main()