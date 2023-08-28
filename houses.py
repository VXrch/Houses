from second import House
import uuid


def house_menu(my_house, houses_list, my_city):

    ex = False

    while not ex:

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
        print("[8] - Display house to work")
        print("[0] - Go back")
        print("__________________________________________________________________________________________\n")
        action = input("/(o_o)\\  ")

        if action == '0':
            ex = True

        elif action == '1':  # Add a house
            houses_list = add_new_house(houses_list, my_city)

        elif action == '2':  # Delete house
            houses_list = delete_house(houses_list, my_house)

        elif action == '3':  # Change house info
            houses_list = change_house_info(houses_list)

        elif action == '4':  # Change the house to work
            my_new_house = change_house_to_work_with(houses_list)
            my_house = my_new_house
            my_house.print_info()

        elif action == '5':  # Display full list of houses
            full_houses_list(houses_list)

        elif action == '6':  # Display information about a specific house
            display_info_about_specific_house(houses_list)

        elif action == '7':  # Display information about houses by communication access
            print_by_communication_access(houses_list)

        elif action == '8':  # Display information about houses by departmental affiliation
            print_by_departmental_affiliation(houses_list)

        elif action == '9':  # Display my house
            my_house.print_info()

        else:
            print("That option is not on the menu!")

    return my_house, houses_list


def add_new_house(houses_list, my_city):
    temp_house = House(0, 0, 0, 0, 0, 0, 0, 0)

    new_house = temp_house.register_new_house(houses_list, my_city)
    houses_list.append(new_house)

    return houses_list


def delete_house(houses_list, my_house):
    try:

        print("\nChoose house to delete: ")
        full_houses_list(houses_list)

        choice = input("Enter house id: ")
        choice_uuid = uuid.UUID(choice)

        if choice == my_house.ID:
            print("You can't delete a house that's currently in robot. Change the active house to another one and try again!")
        else:
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

    except TypeError:
        print("Wrong type!")
    except Exception as err:
        print("ERROR ---> ", err)
    finally:
        return houses_list


def change_house_info(houses_list):
    full_houses_list(houses_list)

    house_to_change_info = input("Enter house ID: ")
    house_to_change_info = uuid.UUID(house_to_change_info)

    info_to_change = input(
        "What do you want to change?\n[1] - House number\n[2] - Address\n[3] - Floors\n[4] - Communication access\n[5] - Departmental affiliation\n[0] - Go back")

    try:
        for house in houses_list:
            if house.ID == house_to_change_info:

                if info_to_change == '1':  # House number
                    new_info = input(
                        "Enter new house number (or [exit] to exit): ")
                    if new_info != 'exit':
                        house.house_number = new_info

                elif info_to_change == '2':  # Address
                    new_info = input(
                        "Enter new house address (or [exit] to exit): ")
                    if new_info != 'exit':
                        house.address = new_info

                elif info_to_change == '3':  # Floors
                    new_info = int(input(
                        "Enter new house floors number (or [0] to exit): "))
                    if new_info > 0:
                        house.floors = new_info

                elif info_to_change == '4':  # Communication access
                    new_info = input(
                        "Enter new house number (or [exit] to exit): ")
                    if new_info != 'exit':
                        house.communication_access = new_info

                elif info_to_change == '5':  # Departmental affiliation
                    new_info = input(
                        "Enter new house number (or [exit] to exit): ")
                    if new_info != 'exit':
                        house.departmental_affiliation = new_info

                elif info_to_change == '0':
                    print()

                else:
                    print("That option is not on the menu!")

    except TypeError:
        print("Wrong type! You must enter a number!")
    except Exception as err:
        print("ERROR: ", err)

    return houses_list


def choose_house_to_work_with(houses_list):

    ext = False

    while not ext:

        full_houses_list(houses_list)
        print("")
        print("|-_-_-_-_-_-_-_---|> Welcome <|---_-_-_-_-_-_-_-|")
        print("")

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
            print("House was found!")
            return house

    print("House is not found!")


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
    for house in houses_list:
        house.print_short_info()


def display_info_about_specific_house(houses_list):

    full_houses_list(houses_list)

    house_to_display = input("Enter house ID to search full info: ")
    house_to_display = uuid.UUID(house_to_display)

    for house in houses_list:
        if house.ID == house_to_display:
            house.print_info()


def choose_house_or_create_a_new_one(houses_list):

    ext = False
    temp_house = House(0, 0, 0, 0, 0, 0, 0, 0)

    while ext == False:

        full_houses_list(houses_list)

        print(
            "Do you want to continue working with what we already have or create a new one?")
        move_on = input("[1] - Continue\n[2] - Create a new one")

        if move_on == '1':
            my_house = choose_house_to_work_with(houses_list)

        elif move_on == '2':
            new_house = temp_house.register_new_house(houses_list)
            houses_list.append(new_house)

            move_on = input(
                "The house is registered! Start working with this one?\n [Y][N]")
            move_on = move_on.lower()

            if move_on == 'y':
                my_house = new_house
                ext = True
            else:
                print("Ok! Then let's create a new one!")
        else:
            print("Wrong choice!")

    return my_house, houses_list
