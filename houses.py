from second import House
import uuid


def house_menu(houses_list, my_house):

    ex = False

    while ex == False:
        input("Press Enter to continue...")
        print("\n__________________________________________________________________________________________\n")
        print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
        print()
        print("[1] - Add a house")
        print("[2] - Delete house")
        print("[3] - Change house info")
        print("[4] - Change the house to work")
        print()
        print("[5] - Display full list of houses")
        print("[6] - Display information about a specific house")
        print("[7] - Display information about houses by communication access")
        print("[8] - Display information about houses by departmental affiliation")
        print("[0] - Go back")
        print("__________________________________________________________________________________________\n")
        action = input("/(o_o)\\  ")

        if action == '0':
            ex = True

        elif action == '1':  # Add a house
            add_new_house(houses_list)

        elif action == '2':  # Delete house
            delete_house(houses_list, my_house)

        elif action == '3':  # Change house info
            change_house_info(houses_list)

        elif action == '4':  # Change the house to work
            my_house = change_house_to_work_with(houses_list)

        elif action == '5':  # Display full list of houses
            full_houses_list(houses_list)

        elif action == '6':  # Display information about a specific house
            display_info_about_specific_house(houses_list)

        elif action == '7':  # Display information about houses by communication access
            print_by_communication_access(houses_list)

        elif action == '8':  # Display information about houses by departmental affiliation
            print_by_departmental_affiliation(houses_list)

        else:
            print("That option is not on the menu!")


def add_new_house(houses_list):
    temp_house = House(0, 0, 0, 0, 0, 0)

    new_house = temp_house.register_new_house(houses_list)
    houses_list.append(new_house)


def delete_house(houses_list, my_house):
    try:

        print("\nChoose house to delete: ")
        full_houses_list(houses_list)

        input("Press Enter to continue...")
        deleted = False

        choice = input("Enter house id: ")
        choice_uuid = uuid.UUID(choice)

        if choice == my_house.ID:
            print("You can't delete a house that's currently in robot. Change the active house to another one and try again!")
            return False

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


def change_house_info(houses_list):
    full_houses_list(houses_list)

    house_to_change_info = input("Enter house ID: ")
    house_to_change_info = uuid.UUID(house_to_change_info)

    info_to_change = input(
        "What do you want to change?\n[1] - House number\n[2] - Address\n[3] - Floors\n[4] - Communication access\n[5] - Departmental affiliation\n")

    for house in houses_list:
        if house.ID == house_to_change_info:
            if info_to_change == '1':  # House number
                new_house_number = input(
                    "Enter new house number (or [exit] to exit): ")
                new_house_number = new_house_number.lower()

                if new_house_number != 'exit':
                    house.house_number = new_house_number

            elif info_to_change == '2':  # Address
                new_house_address = input(
                    "Enter new house address (or [exit] to exit): ")
                new_house_address = new_house_address.lower()

                if new_house_address != 'exit':
                    house.address = new_house_address

            elif info_to_change == '3':  # Floors
                try:
                    new_house_floors = int(input(
                        "Enter new house floors number (or [0] to exit): "))

                    if new_house_floors > 0:
                        house.floors = new_house_floors
                except TypeError:
                    print("It isn't number!")
                    return False
                except Exception as err:
                    print("ERROR: ", err)
                    return False

            elif info_to_change == '4':  # Communication access
                new_house_com_ac = input(
                    "Enter new house number (or [exit] to exit): ")
                new_house_com_ac = new_house_com_ac.lower()

                if new_house_com_ac != 'exit':
                    house.communication_access = new_house_com_ac

            elif info_to_change == '5':  # Departmental affiliation
                new_house_dep_aff = input(
                    "Enter new house number (or [exit] to exit): ")
                new_house_dep_aff = new_house_dep_aff.lower()

                if new_house_dep_aff != 'exit':
                    house.departmental_affiliation = new_house_dep_aff
            else:
                print("That option is not on the menu!")


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
