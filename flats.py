from second import Flat
import uuid


def flat_menu(my_house, houses_list):

    ex = False

    while not ex:

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
        print()
        print("[0] - Go back")
        print("__________________________________________________________________________________________\n")
        action = input("/(o_o)\\  ")

        if action == '0':
            ex = True

        elif action == '1':  # Add an apartment
            my_house = add_an_apartment(my_house)

        elif action == '2':  # Delete an apartment
            my_house = delete_an_apartment(my_house)

        elif action == '3':  # Change apartment info
            my_house = change_apartment_info(my_house)

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

        input("Press any key to continue... ")

    return my_house, houses_list


def add_an_apartment(my_house):
    temp_flat = Flat(0, 0, 0, 0, 0, 0, 0)

    new_flat = temp_flat.register_new_flat(my_house)
    if new_flat != None:
        new_flat.house_ID = my_house.ID
        my_house.attach_flat(new_flat)

    return my_house


def delete_an_apartment(my_house):
    try:
        print("\nChoose flat to delete: ")
        full_list_of_apartments(my_house.flats)

        choice = input("Enter flat id: ")
        choice_uuid = uuid.UUID(choice)

        for flat_number, flat in enumerate(my_house.flats):
            if flat.ID == choice_uuid:
                my_house.flats.pop(flat_number)
                deleted = True

        if deleted is None:
            text = ""
            print(f"{text:.^5} Flat is not found! Try again later! {text:.^5}")
        else:
            text = ""
            print(f"{text:.^5} Flat was successfully deleted! {text:.^5}")
    except Exception as err:
        print("ERROR ---> ", err)
    finally:
        return my_house


def change_apartment_info(my_house):

    full_list_of_apartments(my_house)
    find = False

    flat_to_change_info = input("Enter house ID: ")
    flat_to_change_info = uuid.UUID(flat_to_change_info)

    info_to_change = input(
        "What do you want to change?\n[1] - Flat number\n[2] - Floor\n[3] - Rooms\n[4] - Area\n[0] - Go back\n---> ")

    try:
        for flat in my_house.flats:
            if flat.ID == flat_to_change_info:
                find = True

                if info_to_change == '1':  # Flat number
                    new_info = int(
                        input("Enter new flat number (or [0] to exit): "))
                    found_the_same = None
                    for flat in my_house.flats:
                        if flat.flat_number == new_info:
                            print("This flat is already listed!")
                            found_the_same = True
                    if found_the_same is None:
                        flat.flat_number = new_info

                elif info_to_change == '2':  # Floor
                    new_info = int(
                        input("Enter new flat number (or [0] to exit): "))
                    if new_info == 0:
                        print()
                    elif new_info > my_house.floors:
                        print(
                            f"Wrong floor! There are only {my_house.floors} floors in this building!")
                    else:
                        flat.floor = new_info

                elif info_to_change == '3':  # Rooms
                    new_info = int(
                        input("Enter new flat number (or [0] to exit): "))
                    if new_info != 0:
                        flat.rooms = new_info

                elif info_to_change == '4':  # Area
                    new_info = float(
                        input("Enter new flat number (or [0] to exit): "))

                    if new_info != 0:
                        flat.area = new_info

                elif info_to_change == '0':
                    print()

                else:
                    print("That option is not on the menu!")

        if find == False:
            print("Flat is not found!")

    except TypeError:
        print("It isn't number!")
    except Exception as err:
        print("ERROR: ", err)

    return my_house


def full_list_of_apartments(flats_list):
    find = False
    for flat in flats_list:
        flat.print_short_info()
        find = True

    if find == False:
        print("You haven't any apartments!")


def display_specific_apartment(flats_list):

    full_list_of_apartments(flats_list)
    find = False

    apartment_to_search = input("Enter apartment ID: ")
    apartment_to_search = uuid.UUID(apartment_to_search)

    for flat in flats_list:
        if flat.ID == apartment_to_search:
            flat.print_info()
            find = True

    if find == False:
        print("Flat is not found!")


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
        find = False
        rooms_to_search = int(input("Enter rooms: "))

        for flat in flats_list:
            if flat.rooms == rooms_to_search:
                flat.print_info()
                find = True

        if find == False:
            print("Flat is not found!")

    except Exception as err:
        print("Error! ---> ", err)


def print_by_area(flats_list):
    try:
        find = False

        min_area_to_search = float(input("Enter min area range: "))
        max_area_to_search = float(input("Enter max area range: "))

        for flat in flats_list:
            if min_area_to_search <= flat.area <= max_area_to_search:
                flat.print_short_info()
                find = True

        if find == False:
            print("Flat is not found!")

    except TypeError:
        print("Type Error!")
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
