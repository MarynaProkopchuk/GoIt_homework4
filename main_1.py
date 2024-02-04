def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        name = name.capitalize()
        if name.isalpha()== True and phone.isdigit() == True:
            contacts[name] = phone
            return f"Contact {name} - {phone} added."
        else:
            return "Please write command 'add' => 'name' in letters => 'phone' in numbers'"    
    except ValueError:
        return "Please write command 'add => name => phone'"
   

def change_number(args, contacts):
    try:
        name, phone = args
        name = name.capitalize()
        if "".join(name) in contacts and phone.isdigit() == True:
            contacts.update({name: phone})
            return f"Contact {name} changed to {phone}"
        elif phone.isdigit() == False:
            return "Please write command 'change' => 'name' in letters => 'phone' in numbers'"
        else:
            return f"There is no contact with name {"".join(name)}, if you want to add it please write command - 'add => username => phone'"
    except ValueError:
        return "Please write command 'change => name => phone'"

def phone_username(args, contacts):
    name = args
    name = "".join(name).capitalize()
    try:
        if name in contacts:
            return f"Contact with name {name} - {contacts.get(name)}"
        else:
            return f"Contact with {name} name is not found"
    except ValueError:
        return "Please write command 'phone => name'"

def show_all_conacts(contacts):
    contacts_list = ""
    for name, phone in contacts.items():
        contacts_list += name + " - " + phone + "\n"
    return f"{contacts_list}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
            print(add_contact(args, contacts))
        elif command == "change":
            change_number(args, contacts)
            print(change_number(args, contacts))
        elif command == "phone":
            phone_username(args, contacts)
            print(phone_username(args, contacts))
        elif command == "all":
            print("Your contacts list:")
            show_all_conacts(contacts)
            print(show_all_conacts(contacts))
        else:
            print("Invalid command.") 
    return contacts       
               

if __name__ == "__main__":
    main()
    

