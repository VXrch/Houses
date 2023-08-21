from second import Resident
import uuid


def resident_menu(my_house, houses_list):
    input("Press Enter to continue...")
    print("\n__________________________________________________________________________________________\n")
    print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
    print()
    print("[1] - Add new resident")
    print("[2] - Remove a resident")
    print("[3] - Change resident info")
    print()
    print("Display only in this house: ")
    print("[4] - Display all residents")
    print("[5] - Display residents in one floor")
    print("[6] - Displat residents by age")
    print("[7] - Displat residents by age in range")
    print("[8] - Displat a specific resident")
    print()
    print("Display in all houses: ")
    print("[9] - Display all residents")
    print("[10] - Display residents in one floor")
    print("[11] - Displat residents by age")
    print("[12] - Displat residents by age in range")
    print("[13] - Displat a specific resident")
    print("[0] - Go back")

    print("__________________________________________________________________________________________\n")
    action = input("/(o_o)\\  ")

    if action == '0':
        ex = True

    elif action == '1':  # Add new resident
        add_new_resident(my_house)

    elif action == '2':  # Remove a resident
        delete_resident(my_house)

    elif action == '3':  # Change resident info
        change_resident_info(my_house)

    elif action == '4':  # Display all residents
        residents_list = residents_in_one_house(my_house)
        display_full_residents_list(residents_list)

    elif action == '5':  # Display residents in one floor
        residents_list = residents_in_one_house(my_house)
        display_residents_by_floor(residents_list)

    elif action == '6':  # Displat residents by age
        residents_list = residents_in_one_house(my_house)
        display_residents_by_age(residents_list)

    elif action == '7':  # Displat residents by age in range
        residents_list = residents_in_one_house(my_house)
        display_residents_by_age_range(residents_list)

    elif action == '8':  # Displat a specific resident
        residents_list = residents_in_one_house(my_house)
        display_specific_resident(residents_list)

    elif action == '9':  # (ALL HOUSES) Display all residents
        residents_list = residents_in_all_houses(houses_list)
        display_full_residents_list(residents_list)

    elif action == '10':  # (ALL HOUSES) Display residents in one floor
        residents_list = residents_in_all_houses(houses_list)
        display_residents_by_floor(residents_list)

    elif action == '11':  # (ALL HOUSES) Displat residents by age
        residents_list = residents_in_all_houses(houses_list)
        display_residents_by_age(residents_list)

    elif action == '12':  # (ALL HOUSES) Displat residents by age in range
        residents_list = residents_in_all_houses(houses_list)
        display_residents_by_age_range(residents_list)

    elif action == '13':  # (ALL HOUSES) Displat a specific resident
        residents_list = residents_in_all_houses(houses_list)
        display_specific_resident(residents_list)


def add_new_resident(my_house):

    temp_resident = Resident(0, 0, 0, 0, 0, 0, 0, 0, 0)

    for flat in my_house.flats:
        flat.print_short_info()

    flat_to_add = input(
        "Enter the ID of the apartment to which the new tenant will be added: ")
    flat_to_add = uuid.UUID(flat_to_add)

    for flat in my_house.flats:
        if flat.ID == flat_to_add:
            new_resident = temp_resident.register_new_resident(
                flat.flat_number)
            new_resident.flat_ID = flat.ID
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


def change_resident_info(my_house):
    rsdns_list = residents_in_one_house(my_house)
    display_full_residents_list(rsdns_list)

    choice = input("Enter resident's ID: ")
    choice = uuid.UUID(choice)

    for resident in rsdns_list:
        if resident.ID == choice:
            action = input(
                "What do you want to change?\n[1] - Name\n[2] - Surname\n[3] - Age\n[4] - Phone number\n[5] - Email\n[6] - Flat number\n")
            if action == '1':  # Name
                new_name = input(
                    "Enter new resident's name (or [exit] to exit): ")

                if new_name != 'exit':
                    resident.name = new_name

            elif action == '2':  # Surname
                new_surname = input(
                    "Enter new resident's surname (or [exit] to exit): ")

                if new_surname != 'exit':
                    resident.surname = new_surname

            elif action == '3':  # Age
                new_age = input(
                    "Enter resident's new age (or [exit] to exit): ")

                if new_age != 'exit':
                    resident.age = new_age

            elif action == '4':  # Phone number
                new_phone_number = input(
                    "Enter resident's new phone number (or [exit] to exit): ")

                if new_phone_number != 'exit':
                    resident.phone_number = new_phone_number

            elif action == '5':  # Email
                new_email = input(
                    "Enter new resident's email (or [exit] to exit): ")

                if new_email != 'exit':
                    resident.email = new_email

            elif action == '6':  # Flat number
                try:
                    new_flat_number = int(input(
                        "Enter new resident's name (or [exit] to exit): "))

                    for flat in my_house.flats:
                        if flat.flat_number == new_flat_number:
                            resident.flat_number = new_flat_number

                except TypeError:
                    print("It isn't number!")
                    return False
                except Exception as err:
                    print("ERROR: ", err)
                    return False
            else:
                print("That option is not on the menu!")


def display_full_residents_list(residents_list):
    for resident in residents_list:
        resident.print_short_info()


def display_specific_resident(residents_list):
    display_full_residents_list(residents_list)

    resident_to_display = ("Select resident to display (enter ID): ")
    resident_to_display = uuid.UUID(resident_to_display)

    for rsdnt in residents_list:
        if rsdnt.ID == resident_to_display:
            rsdnt.print_info()


def display_residents_by_age_range(residents_list):
    try:
        age_to_search_min = int(input("Enter min range to search: "))
        age_to_search_max = int(input("Enter max range to search: "))

        for resident in residents_list:
            if age_to_search_min <= resident.age <= age_to_search_max:
                resident.print_short_info()
    except Exception as err:
        print("Error: ", err)


def display_residents_by_age(residents_list):
    try:
        age_to_search = int(input("Enter age to search: "))

        for resident in residents_list:
            if resident.age == age_to_search:
                resident.print_short_info()
    except Exception as err:
        print("Error: ", err)


def display_residents_by_floor(residents_list):
    try:
        floor_to_search = int(input("Enter floor to search: "))

        for flat in residents_list:
            if flat.floor == floor_to_search:
                for resident in flat.residents:
                    resident.print_short_info()
    except Exception as err:
        print("Error: ", err)


def residents_in_all_houses(houses_list):
    residents_list = []

    for house in houses_list:
        for flat in house.flats:
            for resident in flat.residents:
                residents_list.append(resident)


def residents_in_one_house(my_house):
    residents_list = []

    for flat in my_house.flats:
        for resident in flat.residents:
            residents_list.append(resident)
