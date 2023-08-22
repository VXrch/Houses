from second import House, Resident, Flat
from files_work import write_data_to_file, read_data_from_file
from houses import house_menu, choose_house_to_work_with
from flats import flat_menu
from residents import resident_menu


def main_menu(houses_list, my_house):

    ext = False

    while ext == False:

        print("__________________________________________________________________________________________\n")
        print("\n[1] - house menu")
        print("[2] - flats menu")
        print("[3] - residents menu")
        print("[4] - Save information to a file")
        print("[5] - Uploading information from a file")
        print("[0] - Exit")
        print("__________________________________________________________________________________________\n")
        action = input("/(o_o)\\  ")

        if action == '1':  # house menu
            my_house, houses_list = house_menu(my_house, houses_list)

        elif action == '2':  # flats menu
            my_house, houses_list = flat_menu(my_house, houses_list)

        elif action == '3':  # residents menu
            my_house, houses_list = resident_menu(my_house, houses_list)

        elif action == '4':  # Save information to a file
            write_data_to_file(houses_list)

        elif action == '5':  # Uploading information from a file
            read_data_from_file()

        elif action == '0':  # Exit

            save_info = input(
                "Would you like to save information before exit?\m[Y][N]\n  ")
            save_info = save_info.lower()

            if save_info == 'y':
                write_data_to_file(houses_list)
            else:
                print("Ok! Have a nice day!")

            ext = True
        else:
            print("Wrong choice!")


temp_resident = Resident(0, 0, 0, 0, 0, 0, 0, 0, 0)
temp_house = House(0, 0, 0, 0, 0, 0)
temp_flat = Flat(0, 0, 0, 0, 0, 0, 0)
my_house = House(0, 0, 0, 0, 0, 0)
houses_list = []

houses_list = read_data_from_file()

if len(houses_list) != 0:
    my_house = choose_house_to_work_with(houses_list)
else:
    print(
        "You don't have finished homes yet! To start working with the program, register a new house!")
    new_house = temp_house.register_new_house(houses_list)
    houses_list.append(new_house)
    my_house = choose_house_to_work_with(houses_list)


main_menu(houses_list, my_house)
