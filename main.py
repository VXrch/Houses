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


def main_menu():
    print("\n__________________________________________________________________________________________\n")
    print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
    print()
    print("[1] - Add a resident to a house\n[2] - Remove a resident from a house")
    print("[3] - Add apartment\n[4] - Delete an apartment")
    print("[5] - Attaching a resident to an apartment\n[6] - Unattaching a resident from an apartment")
    print("[7] - Save information to a file\n[8] - Uploading information from a file")
    print("[9] - Display the full list of residents\n[10] - Display the full list of apartments")
    print("[11] - Display information about a specific apartment\n[12] - Display information about apartments on a particular floor.")
    print("[13] - Display information about apartments of the same type\n[14] - Add a house")
    print("[15] - Delete house\n[16] - Display all houses\n[0] - exit")
    print("__________________________________________________________________________________________")
    print()
    action = input("/(o_o)\\  ")
    return action


temp_house = House(0, 0, 0, 0, 0, 0)
temp_flat = Flat(0, 0, 0, 0, 0)
temp_resident = Resident(0, 0, 0, 0, 0, 0, 0)

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
    elif action == '1':  # Add a resident to a house
        print("")
    elif action == '2':  # Remove a resident from a house
        print("")
    elif action == '3':  # Add apartment
        print("")
    elif action == '4':  # Delete an apartment
        print("")
    elif action == '5':  # Attaching a resident to an apartment
        print("")
    elif action == '6':  # Unattaching a resident from an apartment
        print("")
    elif action == '7':  # Save information to a file
        print("")
    elif action == '8':  # Uploading information from a file
        print("")
    elif action == '9':  # Display the full list of residents
        print("")
    elif action == '10':  # Display the full list of apartments
        print("")
    elif action == '11':  # Display information about a specific apartment
        print("")
    elif action == '12':  # Display information about apartments on a particular floor
        print("")
    elif action == '13':  # Display information about apartments of the same type
        print("")

    elif action == '14':  # Add a house
        new_house = temp_house.register_new_house()
        houses_list.append(new_house)

    elif action == '15':  # Delete house
        delete_house(houses_list)

    elif action == '16':  # Display all houses
        print("Total houses in the database: ", len(houses_list))
        for house in houses_list:
            house.print_info()

    else:
        print("Wrong choice! Try again!")
