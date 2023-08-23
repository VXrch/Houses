from second import House, City
from files_work import write_data_to_file, read_data_from_file
from houses import house_menu, choose_house_to_work_with
from flats import flat_menu
from residents import resident_menu
from city import city_menu, choose_city_to_work_with


def main_menu(houses_list, my_house):

    ext = False

    while ext == False:

        print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
        print()
        print("[1] - City menu")
        print("[2] - House menu")
        print("[3] - Flat menu")
        print("[4] - Resident menu")
        print("[5] - Save information to a file")
        print("[6] - Uploading information from a file")
        print("[0] - Exit")
        print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        action = input("/(o_o)\\  ")

        if action == '1':  # city menu
            my_city, citys_list = city_menu(my_city, citys_list)

        elif action == '2':  # house menu
            my_house, houses_list = house_menu(my_house, houses_list)

        elif action == '3':  # flat menu
            my_house, houses_list = flat_menu(my_house, houses_list)

        elif action == '4':  # resident menu
            my_house, houses_list = resident_menu(my_house, houses_list)

        elif action == '5':  # Save information to a file
            write_data_to_file(houses_list)

        elif action == '6':  # Uploading information from a file
            read_data_from_file()

        elif action == '0':  # Exit

            save_info = input(
                "Would you like to save information before exit?\n[Y][N]\n  ")
            save_info = save_info.lower()

            if save_info == 'y':
                write_data_to_file(houses_list)
            else:
                print("Ok! Have a nice day!")

            ext = True
        else:
            print("Wrong choice!")


#####################################################################################################################

temp_city = City(0, 0, 0, 0, 0, 0, 0, 0)
my_city = City(0, 0, 0, 0, 0, 0, 0, 0)
citys_list = []

temp_house = House(0, 0, 0, 0, 0, 0, 0, 0)
my_house = House(0, 0, 0, 0, 0, 0, 0, 0)
houses_list = []


#####################################################################################################################


citys_list = read_data_from_file()
houses_list = my_city.houses

if len(citys_list) != 0:
    my_city = choose_city_to_work_with(citys_list)
else:
    print(
        "You don't have finished citys yet! To start working with the program, register a new city!")
    new_city = temp_city.register_new_city(citys_list)
    citys_list.append(new_city)
    my_city = choose_city_to_work_with(citys_list)


if len(houses_list) != 0:
    my_house = choose_house_to_work_with(houses_list)
else:
    print(
        "You don't have finished homes yet! To start working with the program, register a new house!")
    new_house = temp_house.register_new_house(houses_list, my_city)
    houses_list.append(new_house)
    my_house = choose_house_to_work_with(houses_list)

#####################################################################################################################

main_menu(houses_list, my_house)
