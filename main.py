from second import House, Resident, Flat
import uuid


def choose_house_to_work_with(houses_list):

    print("|-_-_-_-_-_-_-_---|> Welcome <|---_-_-_-_-_-_-_-|")

    full_houses_list(houses_list)

    house_to_work = input("Enter house id to work with: ")
    house_to_work = uuid.UUID(house_to_work)
    return house_to_work


def change_house_to_work_with(houses_list):

    full_houses_list(houses_list)

    house_to_work = input("Enter house id to work with: ")
    house_to_work = uuid.UUID(house_to_work)
    return house_to_work


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


def add_an_apartment(my_house):

    new_flat = temp_flat.register_new_flat(my_house)
    if new_flat != False:
        flats_list.append(new_flat)
        my_house.attach_flat(new_flat)


def delete_an_apartment(my_house):
    try:
        print("\nChoose flat to delete: ")
        full_list_of_apartments(my_house.flats_list)

        input("Press Enter to continue...")
        deleted = False

        choice = input("Enter flat id: ")
        choice_uuid = uuid.UUID(choice)

        for flat_number, flat in enumerate(flats_list):
            if flat.ID == choice_uuid:
                flats_list.pop(flat_number)
                deleted = True

        if not deleted:
            text = ""
            print(f"{text:.^5} Flat is not found! Try again later! {text:.^5}")
        else:
            text = ""
            print(f"{text:.^5} Flat was successfully deleted! {text:.^5}")
    except Exception as err:
        print("ERROR ---> ", err)


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


def full_list_of_apartments(flats_list):
    print("__________________________________________________________________________________________\n")
    for flat in flats_list:
        flat.print_short_info()


def full_houses_list(houses_list):
    print("__________________________________________________________________________________________\n")
    for house in houses_list:
        house.print_short_info()


def display_specific_apartment(flats_list):

    full_list_of_apartments(flats_list)

    print("__________________________________________________________________________________________\n")
    apartment_to_search = input("Enter apartment ID: ")
    apartment_to_search = uuid.UUID(apartment_to_search)

    for flat in flats_list:
        if flat.ID == apartment_to_search:
            flat.print_info()


def display_apartments_on_the_floor(flats_list):

    search_on_the_floor = int(input("Display flats on the floor: "))
    print("__________________________________________________________________________________________\n")

    for flat in flats_list:
        if flat.floors == search_on_the_floor:
            flat.print_short_info()


def house_the_same_type(flats_list):
    action = input(
        "[1] - Communication access\n[2] - Departmental affiliation\n[0] - Exit")

    if action == '1':
        print_by_communication_access(flats_list)
    elif action == '2':
        print_by_departmental_affiliation(flats_list)
    elif action == '0':
        return
    else:
        print("Wrong number!")


def flats_the_same_type(my_house):

    rooms_to_search = input("Enter rooms: ")

    for flat in my_house:
        if flat.rooms == rooms_to_search:
            flat.print_info()


def print_by_communication_access(flats_list):
    com_access = input("Enter what communication access to search for: ")
    com_access = com_access.lower()

    find = False

    for flat in flats_list:
        if flat.communication_access == com_access:
            flat.print_short_info()

    if find == False:
        print("Flat is not found!")


def print_by_floor(my_house, flats_list):

    floor_to_search = int(input(
        "Enter what departmental affiliation to search for: "))

    find = False

    for flat in my_house.flats:
        if flat.floor == floor_to_search:
            flat.print_short_info()
            find = True

    if find == False:
        print("Flat is not found!")


temp_house = House(0, 0, 0, 0, 0, 0)
temp_flat = Flat(0, 0, 0, 0, 0, 0)
temp_resident = Resident(0, 0, 0, 0, 0, 0, 0, 0)

houses_list = []
flats_list = []
residents_list = []

ex = False
first_iteration = True
while not ex:

    my_house = choose_house_to_work_with(houses_list)

    if first_iteration == False:
        input("Press Enter to continue...")

    menu = input("[1] - house menu\n[2] - flats menu\n[0] - Exit")

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
            print("")

        elif action == '6':  # Display information about houses of the same type
            print("")

    elif menu == '2':
        action = flat_menu()

        if action == '0':
            print("Bye-bye!")
            ex = True

        elif action == '1':  # Add an apartment
            add_an_apartment(my_house, flats_list)

        elif action == '2':  # Delete an apartment
            delete_an_apartment(my_house, flats_list)

        elif action == '3':  # Add a resident
            print("")

        elif action == '4':  # Remove a resident
            print("")

        elif action == '5':  # Save information to a file
            print("")

        elif action == '6':  # Uploading information from a file
            print("")

        elif action == '7':  # Display the full list of apartments
            full_list_of_apartments(my_house, flats_list)

        elif action == '8':  # Display information about a specific apartment
            display_specific_apartment(my_house, flats_list)

        elif action == '9':  # Display information about apartments on a particular floor
            display_apartments_on_the_floor(my_house, flats_list)

        elif action == '10':  # Display information about apartments of the same type
            apartments_of_the_same_type(my_house, flats_list)

    elif menu == '0':
        print("Bye-bye!")
        ex = True
    else:
        print("Wrong choice!")

    first_iteration = False
