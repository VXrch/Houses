from second import House, Resident, Flat
import uuid
import json


def house_menu():
    print("\n__________________________________________________________________________________________\n")
    print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
    print()
    print("[1] - Add a house")
    print("[2] - Delete house")
    print("[3] - Change house")
    print("[4] - Display full list of houses")
    print("[5] - Display information about a specific house")
    print("[6] - Display information about houses of the same type")
    print("[0] - Exit")
    print("__________________________________________________________________________________________\n")
    action = input("/(o_o)\\  ")
    return action


def flat_menu():
    print("\n__________________________________________________________________________________________\n")
    print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
    print()

    print("[1] - Add an apartment")
    print("[2] - Delete an apartment")
    print("[3] - Add a resident")
    print("[4] - Remove a resident")
    print("[5] - Save information to a file")
    print("[6] - Uploading information from a file")
    print()
    print("[7] - Display the full list of apartments")
    print("[8] - Display information about a specific apartment")
    print("[9] - Display information about apartments on a particular floor")
    print("[10] - Display information about apartments of the same type")
    print("[0] - exit")
    print("__________________________________________________________________________________________\n")
    action = input("/(o_o)\\  ")
    return action


# HOUSES --------------------------------------------------------------------------------------------------------------------------------------------------------
# HOUSES --------------------------------------------------------------------------------------------------------------------------------------------------------
# HOUSES --------------------------------------------------------------------------------------------------------------------------------------------------------

def choose_house_to_work_with(houses_list):

    ext = False

    while not ext:

        print("|-_-_-_-_-_-_-_---|> Welcome <|---_-_-_-_-_-_-_-|")

        full_houses_list(houses_list)

        house_to_work = input("Enter house id to work with: ")
        house_to_work = uuid.UUID(house_to_work)

        for house in houses_list:
            if house.ID == house_to_work:
                return house

        print("Wrong ID! Try again!")
        input("")


def change_house_to_work_with(houses_list):

    full_houses_list(houses_list)

    house_to_work = input("Enter house id to work with: ")
    house_to_work = uuid.UUID(house_to_work)

    for house in houses_list:
        if house.ID == house_to_work:
            return house


def delete_house(houses_list):
    try:
        print("\nChoose house to delete: ")
        full_houses_list(houses_list)

        input("Press Enter to continue...")
        deleted = False

        choice = input("Enter house id: ")
        choice_uuid = uuid.UUID(choice)

        for house_number, house in enumerate(houses_list):
            if house.ID == choice_uuid:
                houses_list.pop(house_number)
                deleted = True

        if not deleted:
            text = ""
            print(f"{text:.^5} House is not found! Try again later! {text:.^5}")
        else:
            text = ""
            print(f"{text:.^5} House was successfully deleted! {text:.^5}")
    except Exception as err:
        print("ERROR ---> ", err)


def house_the_same_type(houses_list):
    action = input(
        "[1] - Communication access\n[2] - Departmental affiliation\n[0] - Exit")

    if action == '1':
        print_by_communication_access(houses_list)
    elif action == '2':
        print_by_departmental_affiliation(houses_list)
    elif action == '0':
        return
    else:
        print("Wrong number!")


def print_by_departmental_affiliation(houses_list):

    dep_acc = input("Enter what communication access to search for: ")
    dep_acc = dep_acc.lower()

    find = False

    for house in houses_list:
        if house.departmental_affiliation == dep_acc:
            house.print_short_info()

    if find == False:
        print("House is not found!")


def print_by_communication_access(houses_list):

    com_access = input("Enter what communication access to search for: ")
    com_access = com_access.lower()

    find = False

    for house in houses_list:
        if house.communication_access == com_access:
            house.print_short_info()

    if find == False:
        print("House is not found!")


def full_houses_list(houses_list):
    print("__________________________________________________________________________________________\n")
    for house in houses_list:
        house.print_short_info()


def display_info_about_specific_house(houses_list):

    full_houses_list(houses_list)

    house_to_display = input("Enter house ID to search full info: ")
    house_to_display = uuid.UUID(house_to_display)

    for house in houses_list:
        if house.ID == house_to_display:
            house.print_info()


# FLATS --------------------------------------------------------------------------------------------------------------------------------------------------------
# FLATS --------------------------------------------------------------------------------------------------------------------------------------------------------
# FLATS --------------------------------------------------------------------------------------------------------------------------------------------------------


def add_an_apartment(my_house):

    new_flat = temp_flat.register_new_flat(my_house)
    if new_flat != False:
        my_house.attach_flat(new_flat)


def delete_an_apartment(my_house):
    try:
        print("\nChoose flat to delete: ")
        full_list_of_apartments(my_house.flats)

        input("Press Enter to continue...")
        deleted = False

        choice = input("Enter flat id: ")
        choice_uuid = uuid.UUID(choice)

        for flat_number, flat in enumerate(my_house.flats):
            if flat.ID == choice_uuid:
                my_house.flats.pop(flat_number)
                deleted = True

        if not deleted:
            text = ""
            print(f"{text:.^5} Flat is not found! Try again later! {text:.^5}")
        else:
            text = ""
            print(f"{text:.^5} Flat was successfully deleted! {text:.^5}")
    except Exception as err:
        print("ERROR ---> ", err)


def full_list_of_apartments(my_house):
    print("__________________________________________________________________________________________\n")
    for flat in my_house.flats:
        flat.print_short_info()


def display_specific_apartment(my_house):

    full_list_of_apartments(my_house)

    print("__________________________________________________________________________________________\n")
    apartment_to_search = input("Enter apartment ID: ")
    apartment_to_search = uuid.UUID(apartment_to_search)

    for flat in my_house.flats:
        if flat.ID == apartment_to_search:
            flat.print_info()


def print_by_floor(my_house):

    floor_to_search = int(input(
        "Enter the floor: "))

    find = False

    for flat in my_house.flats:
        if flat.floor == floor_to_search:
            flat.print_short_info()
            find = True

    if find == False:
        print("Flat is not found!")


def print_the_same_type(my_house):
    try:
        rooms_to_search = int(input("Enter rooms: "))

        for flat in my_house:
            if flat.rooms == rooms_to_search:
                flat.print_info()

    except Exception as err:
        print("Error! ---> ", err)


# RESIDENTS --------------------------------------------------------------------------------------------------------------------------------------------------------
# RESIDENTS --------------------------------------------------------------------------------------------------------------------------------------------------------
# RESIDENTS --------------------------------------------------------------------------------------------------------------------------------------------------------


def add_new_resident(my_house, temp_resident):

    for flat in my_house.flats:
        flat.print_short_info()

    flat_to_add = input(
        "Enter the ID of the apartment to which the new tenant will be added: ")
    flat_to_add = uuid.UUID(flat_to_add)

    for flat in my_house.flats:
        if flat.ID == flat_to_add:
            new_resident = temp_resident.register_new_resident(
                flat.flat_number)
            flat.attach_resident(new_resident)


def delete_resident(my_house):
    try:
        print("Select the apartment from which you want to remove the tenant: ")
        for flat in my_house.flats:
            flat.print_short_info()

        flat_to_delete_resident_id = input("Enter apartment ID: ")
        flat_to_delete_resident_id = uuid.UUID(flat_to_delete_resident_id)

        deleted_flat = None

        for flat in my_house.flats:
            if flat.ID == flat_to_delete_resident_id:
                deleted_flat = flat
                break

        if deleted_flat is None:
            print("Flat is not found!")
            return

        print("\nChoose resident to delete: ")
        for resident in deleted_flat.residents:
            resident.print_info()

        input("Press Enter to continue...")
        deleted_resident = None

        resident_id = input("Enter resident id: ")
        resident_id = uuid.UUID(resident_id)

        for resident in deleted_flat.residents:
            if resident.ID == resident_id:
                deleted_flat.residents.remove(resident)
                deleted_resident = resident
                break

        if deleted_resident is None:
            text = ""
            print(f"{text:.^5} Resident is not found! Try again later! {text:.^5}")
        else:
            text = ""
            print(f"{text:.^5} Resident was successfully deleted! {text:.^5}")
    except Exception as err:
        print("ERROR ---> ", err)


# FILES --------------------------------------------------------------------------------------------------------------------------------------------------------
# FILES --------------------------------------------------------------------------------------------------------------------------------------------------------
# FILES --------------------------------------------------------------------------------------------------------------------------------------------------------


def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_data_from_file():
    print("WILL BE SOON")

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------------
# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------------
# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------------


temp_house = House(0, 0, 0, 0, 0, 0)
temp_flat = Flat(0, 0, 0, 0, 0, 0)
temp_resident = Resident(0, 0, 0, 0, 0, 0, 0, 0)

houses_file = 'houses.json'
residents_file = 'residents.json'

houses_list = []

my_house = House(0, 0, 0, 0, 0, 0)

ex = False
first_iteration = True
while not ex:

    if first_iteration == False:
        input("Press Enter to continue...")
    else:
        if len(houses_list) != 0:
            my_house = choose_house_to_work_with(houses_list)
        else:
            print(
                "You don't have finished homes yet! To start working with the program, register a new house!")
            new_house = temp_house.register_new_house(houses_list)
            houses_list.append(new_house)
            my_house = choose_house_to_work_with(houses_list)

    menu = input("[1] - house menu\n[2] - flats menu\n[0] - Exit\n")

    if menu == '1':
        action = house_menu()

        if action == '0':
            print("Bye-bye!")
            ex = True

        elif action == '1':  # Add a house
            new_house = temp_house.register_new_house(houses_list)
            houses_list.append(new_house)

        elif action == '2':  # Delete house
            delete_house(houses_list)

        elif action == '3':  # Change house
            change_house_to_work_with(houses_list)

        elif action == '4':  # Display full list of houses
            full_houses_list(houses_list)

        elif action == '5':  # Display information about a specific house
            display_info_about_specific_house(houses_list)

        elif action == '6':  # Display information about houses of the same type
            house_the_same_type(houses_list)

    elif menu == '2':
        action = flat_menu()

        if action == '0':
            print("Bye-bye!")
            ex = True

        elif action == '1':  # Add an apartment
            add_an_apartment(my_house)

        elif action == '2':  # Delete an apartment
            delete_an_apartment(my_house)

        elif action == '3':  # Add a resident
            add_new_resident(my_house, temp_resident)

        elif action == '4':  # Remove a resident
            delete_resident(my_house)

        elif action == '5':  # Save information to a file
            save_data_to_file(houses_list, houses_file)

        elif action == '6':  # Uploading information from a file
            load_data_from_file()

        elif action == '7':  # Display the full list of apartments
            full_list_of_apartments(my_house)

        elif action == '8':  # Display information about a specific apartment
            display_specific_apartment(my_house)

        elif action == '9':  # Display information about apartments on a particular floor
            print_by_floor(my_house)

        elif action == '10':  # Display information about apartments of the same type
            print_the_same_type(my_house)

    elif menu == '0':
        print("Bye-bye!")
        ex = True
    else:
        print("Wrong choice!")

    first_iteration = False
