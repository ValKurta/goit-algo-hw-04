def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args
    except ValueError:
        return None, []

def add_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("\033[91mError:\033[Invalid number of arguments!\033[0m")
        
        name, phone = args
        if phone in contacts.values():
            raise ValueError("\033[93mWarning:\033[0m Contact with this phone number already exists.\033[0m")

        if name in contacts:
            print("\033[93mWarning:\033[0m Contact with this name already exists. Proceeding to create it anyway.\033[0m")
        
                
        contacts[name] = phone
        return "Contact added."
    except ValueError as e:
        return str(e)
    

def change_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("\033[91mError:\033[Invalid number of arguments!\033[0m")
        
        name, phone = args
        if name not in contacts:
            raise ValueError("\033[91mError:\033[Contact does not exist!\033[0m")
        
        contacts[name] = phone
        return "Contact updated."
    except ValueError as e:
        return str(e)

def get_all_contacts(contacts):
    if not contacts:
        return "\033[91mError:\033[No contacts found!\033[0m"
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def get_phone(args, contacts):
    try:
        if len(args) != 1:
            raise ValueError("\033[91mError:\033[Invalid number of arguments!\033[0m")
        
        name = args[0]
        if name not in contacts:
            raise ValueError("\033[91mError:\033[Contact does not exist!\033[0m")
        
        return contacts[name]
    except ValueError as e:
        return str(e)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
