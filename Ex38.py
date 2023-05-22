# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

from os import path

file_base = "base.txt"
all_data = []
last_id = 0

if not path.exists(file_base):
    with open(file_base, "w", encoding = "utf-8") as _:
    

def read_contact_list():
    global all_data, last_id

    with open(file_base, encoding = "utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split[0])
            return all_data
        return []
    

def show_all():
    if all_data:
        print(*all_data, sep = "\n")
    else:
        print("Base empty!\n")

def main_menu():
    work = True
    while work:
        read_contact_list()

def add_new_contact():
    if all_data:
        print("Enter contact name: ")
    name = input("> ")
    print("Enter phone number: ")
    phone_number = input("> ")
    new_contact = {
        "Name": name,
        "Phone number": phone_number
    }
    print("New contact saved!")


def search_contacts():
        if all_data:
            print("Enter name: ")
        for contact in all_data:
            if contact["name"] == name:
                print(
                    contact["name"],
                    contact["phone"]
                )
        else:
            print("Contact not found...")

def change_contact_details():
    if all_data:
        print("Enter contact: ")
    for contact in all_data:
        if contact["name"] == name:
            print("Edit contact name: ")
            new_contact_name = input("> ")
            print("Edit phone number: ")
            new_phone_number = input("> ")
            update_contact = {
                "name ": new_contact_name
                "phone": new_phone_number}
            contacts[file_base] = change_contact_details
            file_base == -1
    if file_base == -1:
        print("Contact details updated")
    else:
        print("Contact not found...")

def delete_contact():
    print("Enter contact: ")
    for contact in all_data:
        if contact[" "] == name:
            print("Do you really want to delete this contact %s (Yes/No)? "name")
                  name_delete = input("> ")
                  if name_delete == "yes":
                  delete_contact()
                  print("Contact deleted ")
                



answer = input("Phone book: \n"
                       "1. Show all \n"
                       "2. Add new contact \n"
                       "3. Search contacts \n"
                       "4. Change contact details \n"
                       "5. Delete contact \n"
                       "6. Export/import contact \n"
                       "7. Exit \n")
        
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contacts()
            case "4":
                change_contact_details()
            case "5":
                delete_contact()
            case "6":
                pass
            case "7":
                work = False
            case _:
                print("Oops! Something went wrong... Please try again.\n")

main_menu()
                  
                    