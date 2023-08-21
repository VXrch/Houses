from second import Flat
import uuid


def flat_menu(houses_list, my_house):

    ex = False

    while ex == False:
        input("Press Enter to continue...")
        print("\n__________________________________________________________________________________________\n")
        print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
        print()

        print("[1] - Add an apartment")
        print("[2] - Delete an apartment")
        print("[3] - Change apartment info")
        print()
        print("Display only in this house: ")
        print("[4] - Display the full list of apartments")
        print("[5] - Display information about a specific apartment")
        print("[6] - Display information about apartments on a particular floor")
        print("[7] - Display information about apartments of the same type")
        print("[8] - Display information about apartments by area")
        print()
        print("Display in all houses: ")
        print("[9] - Display the full list of apartments")
        print("[10] - Display information about a specific apartment")
        print("[11] - Display information about apartments on a particular floor")
        print("[12] - Display information about apartments of the same type")
        print("[13] - Display information about apartments by area")
        print("[0] - Go back")
        print("__________________________________________________________________________________________\n")
        action = input("/(o_o)\\  ")

        if action == '0':
            ex = True

        elif action == '1':  # Add an apartment
            add_an_apartment(my_house)

        elif action == '2':  # Delete an apartment
            delete_an_apartment(my_house)

        elif action == '3':  # Change apartment info
            change_apartment_info(my_house)

        elif action == '4':  # Display the full list of apartments
            flats_list = flats_in_this_house(my_house)
            full_list_of_apartments(flats_list)

        elif action == '5':  # Display information about a specific apartment
            flats_list = flats_in_this_house(my_house)
            display_specific_apartment(flats_list)

        elif action == '6':  # Display information about apartments on a particular floor
            flats_list = flats_in_this_house(my_house)
            print_by_floor(flats_list)

        elif action == '7':  # Display information about apartments of the same type
            flats_list = flats_in_this_house(my_house)
            print_the_same_type(flats_list)

        elif action == '8':  # Display information about apartments by area
            flats_list = flats_in_this_house(my_house)
            print_by_area(flats_list)

        # (ALL HOUSES) Display the full list of apartments (ALL HOUSES)
        elif action == '9':
            flats_list = flats_in_all_houses(houses_list)
            full_list_of_apartments(houses_list)

        # (ALL HOUSES) Display information about a specific apartment
        elif action == '10':
            flats_list = flats_in_all_houses(houses_list)
            display_specific_apartment(flats_list)

        # (ALL HOUSES) Display information about apartments on a particular floor
        elif action == '11':
            flats_list = flats_in_all_houses(houses_list)
            print_by_floor(flats_list)

        # (ALL HOUSES) Display information about apartments of the same type
        elif action == '12':
            flats_list = flats_in_all_houses(houses_list)
            print_the_same_type(flats_list)

        # (ALL HOUSES) Display information about apartments by area
        elif action == '13':
            flats_list = flats_in_all_houses(houses_list)
            print_by_area(flats_list)

        else:
            print("That option is not on the menu!")


def add_an_apartment(my_house):
    temp_flat = Flat(0, 0, 0, 0, 0, 0, 0)

    new_flat = temp_flat.register_new_flat(my_house)
    if new_flat != False:
        new_flat.house_ID = my_house.ID
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


def change_apartment_info(my_house):

    full_list_of_apartments(my_house)

    flat_to_change_info = input("Enter house ID: ")
    flat_to_change_info = uuid.UUID(flat_to_change_info)

    info_to_change = input(
        "What do you want to change?\n[1] - Flat number\n[2] - Floor\n[3] - Rooms\n[4] - Area\n")

    for flat in my_house.flats:

        try:
            if flat.ID == flat_to_change_info:
                if info_to_change == '1':  # Flat number

                    new_flat_number = int(
                        input("Enter new flat number (or [exit] to exit): "))

                    for flat in my_house.flats:
                        if flat.flat_number == new_flat_number:
                            print("This flat is already listed!")
                            return False

                    flat.flat_number = new_flat_number

                elif info_to_change == '2':  # Floor

                    new_flat_floor = int(
                        input("Enter new flat number (or [exit] to exit): "))

                    if 0 > new_flat_floor > my_house.floors:
                        print(
                            f"Wrong floor! There are only {my_house.floors} floors in this building!")
                        return False

                    flat.floor = new_flat_floor

                elif info_to_change == '3':  # Rooms

                    new_flat_rooms = int(
                        input("Enter new flat number (or [exit] to exit): "))

                    if new_flat_rooms <= 0:
                        print("An apartment cannot have less than 1 room!")
                        return False

                    flat.rooms = new_flat_rooms

                elif info_to_change == '4':  # Area

                    new_flat_area = float(
                        input("Enter new flat number (or [exit] to exit): "))

                    if new_flat_area <= 0:
                        print("The apartment cannot be less than 1 square meter!")
                        return False

                    flat.area = new_flat_area
                else:
                    print("That option is not on the menu!")

        except TypeError:
            print("It isn't number!")
            return False
        except Exception as err:
            print("ERROR: ", err)
            return False


def full_list_of_apartments(flats_list):
    print("__________________________________________________________________________________________\n")
    for flat in flats_list:
        flat.print_short_info()


def display_specific_apartment(flats_list):

    full_list_of_apartments(flats_list)

    print("__________________________________________________________________________________________\n")
    apartment_to_search = input("Enter apartment ID: ")
    apartment_to_search = uuid.UUID(apartment_to_search)

    for flat in flats_list:
        if flat.ID == apartment_to_search:
            flat.print_info()


def print_by_floor(flats_list):

    floor_to_search = int(input(
        "Enter the floor: "))

    find = False

    for flat in flats_list:
        if flat.floor == floor_to_search:
            flat.print_short_info()
            find = True

    if find == False:
        print("Flat is not found!")


def print_the_same_type(flats_list):
    try:
        rooms_to_search = int(input("Enter rooms: "))

        for flat in flats_list:
            if flat.rooms == rooms_to_search:
                flat.print_info()

    except Exception as err:
        print("Error! ---> ", err)


def print_by_area(flats_list):
    try:

        full_list_of_apartments(flats_list)

        min_area_to_search = int(input("Enter min area range: "))
        max_area_to_search = int(input("Enter max area range: "))

        for flat in flats_list:
            if min_area_to_search <= flat.area <= max_area_to_search:
                flat.print_short_info()

    except TypeError:
        print("It isn't number!")
        return False
    except Exception as err:
        print("ERROR: ", err)
        return False


def flats_in_this_house(my_house):
    flats_list = []

    for flat in my_house.flats:
        flats_list.append(flat)

    return flats_list


def flats_in_all_houses(houses_list):

    flats_list = []

    for house in houses_list:
        for flat in house.flats:
            flats_list.append(flat)

    return flats_list
