from second import House, Resident, Flat
import uuid


def delete_house(houses_list):
    try:
        print("\nChoose house to delete: ")
        for house in houses_list:
            house.print_info()

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


def add_an_apartment(houses_list, flats_list):

    full_houses_list(houses_list)
    print()
    house_to_add_ID = input(
        "ID of the building in which the apartment is located: ")
    house_to_add_ID = uuid.UUID(house_to_add_ID)

    for house in houses_list:
        if house.ID == house_to_add_ID:
            new_flat = temp_flat.register_new_flat(house, flats_list)
            if new_flat != False:
                flats_list.append(new_flat)
                # Add flat to house


def delete_an_apartment(flats_list):
    try:
        print("\nChoose flat to delete: ")
        for flat in flats_list:
            flat.print_info()

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


def main_menu():
    print("\n__________________________________________________________________________________________\n")
    print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
    print()
    print("[1] - Add a house")
    print("[2] - Delete house")
    print("[3] - Add an apartment")
    print("[4] - Delete an apartment")
    print("[5] - Add a resident")
    print("[6] - Remove a resident")
    print("[7] - Save information to a file")
    print("[8] - Uploading information from a file")
    print()
    print("[9] - Display full list of houses")
    print("[10] - Display the full list of apartments")
    print("[11] - Display information about a specific apartment")
    print("[12] - Display information about apartments on a particular floor")
    print("[13] - Display information about apartments of the same type")
    print("[0] - exit")
    print("__________________________________________________________________________________________\n")
    action = input("/(o_o)\\  ")
    return action


def full_list_of_apartments(flats_list):
    print("_____________________________________\n")
    for flat in flats_list:
        flat.print_info()


def full_houses_list(houses_list):
    print("_____________________________________\n")
    for house in houses_list:
        house.print_info()


temp_house = House(0, 0, 0, 0, 0, 0)
temp_flat = Flat(0, 0, 0, 0, 0, 0)
temp_resident = Resident(0, 0, 0, 0, 0, 0, 0, 0)

houses_list = []
flats_list = []
residents_list = []

ex = False
first_iteration = True
while not ex:

    if first_iteration == False:
        input("Press Enter to continue...")
    action = main_menu()
    first_iteration = False

    if action == '0':  # Exit
        print("Bye-bye!")
        ex = True

    elif action == '1':  # Add a house
        new_house = temp_house.register_new_house(houses_list)
        houses_list.append(new_house)

    elif action == '2':  # Delete house
        delete_house(houses_list)

    elif action == '3':  # Add an apartment
        add_an_apartment(houses_list, flats_list)

    elif action == '4':  # Delete an apartment
        delete_an_apartment(flats_list)

    elif action == '5':  # Add a resident
        print("")

    elif action == '6':  # Remove a resident
        print("")

    elif action == '7':  # Save information to a file
        print("")

    elif action == '8':  # Uploading information from a file
        print("")

    elif action == '9':  # Display full list of houses
        full_houses_list(houses_list)

    elif action == '10':  # Display the full list of apartments
        full_list_of_apartments(flats_list)

    elif action == '11':  # Display information about a specific apartment
        print("")

    elif action == '12':  # Display information about apartments on a particular floor
        print("")

    elif action == '13':  # Display information about apartments of the same type
        print("")

    else:
        print("Wrong choice! Try again!")
