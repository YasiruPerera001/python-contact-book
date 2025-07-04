
#contactlist dictionary
contacts = {}

def contactBook():
	loadContacts()

	while True:
		features()
		exit = input("Do you wanna exit?(yes/no) ").lower()
		if exit != "no":
			break

#show the optionlist for the user to continue	
def features():
	print("1. Add a new contact")
	print("2. View all contacts")
	print("3. Search a contact by the name")
	print("4. Delete a contact")
	print()

	try:
		option = int(input("Select your option(1/2/3/4): "))

		while option == 1 or option == 2 or option == 3 or option == 4:
			if option == 1:
				addContact()
				break
			elif option == 2:
				viewAllContact()
				break
			elif option == 3:
				searchContact()
				break
			elif option == 4:
				deleteContact()
				break
			else:
				print("Sorry!! Wrong input")
	except ValueError as e:
		print("Sorry invalid input", e)

#add a new contact to the contactlist
def addContact():
    try:
        name_input = input("Add the contact's name: ").lower()
        number_input = int(input("Add your contact number: "))

        if name_input not in contacts:
            contacts[name_input] = f"{number_input}"
            print(f"The contact is \"{name_input}: {number_input}\"")

            # Save to file
            with open("contacts.txt", "a") as file:
                file.write(f"{name_input}:{number_input}\n")
        else:
            print("Sorry!! You have already added this contact!!")
    except ValueError as e:
        print("Sorry invalid input", e)

#View all contacts of contactlist
def viewAllContact():
	print("Your contacts: ")
	
	for key,value in contacts.items():
		print("  " + f"{key}: {value}")

#search a contact from contactlist
def searchContact():
	search_input = input("Search the contact by the name: ").lower()

	if search_input in contacts:
		print(f"{search_input}: {contacts[search_input]}")
	else:
		print("Sorry!! this contact name cannot found in your contact list")

#delete a contact from contactlist
def deleteContact():
    del_input = input("Add the contact name you wanna delete: ").lower()

    if del_input in contacts:
        del contacts[del_input]
        print(f"{del_input} has been deleted from your contact list")

        # Overwrite file with current contacts
        with open("contacts.txt", "w") as file:
            for name, number in contacts.items():
                file.write(f"{name}:{number}\n")
    else:
        print("Sorry!! you may have entered a wrong name. please check and try again...")

def loadContacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                if ':' in line:
                    name, number = line.strip().split(":")
                    contacts[name] = number
    except FileNotFoundError:
        # First run, no file yet
        pass

contactBook()