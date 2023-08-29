from second import House, City
from houses import house_menu, choose_house_to_work_with, choose_house_or_create_a_new_one
from files_work import files_menu, write_data_to_file, read_data_from_file
from city import city_menu, choose_city_or_create_a_new_one
from residents import resident_menu
from flats import flat_menu


def main_menu(my_city, my_house, citys_list):

    ext = False

    while ext == False:

        print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
        print()
        print("[1] - City menu")
        print("[2] - House menu")
        print("[3] - Flat menu")
        print("[4] - Resident menu")
        print("[5] - Files menu")
        print("[0] - Exit")
        print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        action = input("/(o_o)\\  ")

        if action == '1':  # city menu
            my_city, citys_list = city_menu(my_city, citys_list)

        elif action == '2':  # house menu
            my_city, my_house, my_city.houses = house_menu(
                my_city, my_house, my_city.houses)

        elif action == '3':  # flat menu
            my_house, my_city.houses = flat_menu(my_house, my_city.houses)

        elif action == '4':  # resident menu
            my_house, my_city.houses = resident_menu(my_house, my_city.houses)

        elif action == '5':  # files menu
            citys_list = files_menu(citys_list)

        elif action == '0':  # exit

            save_info = input(
                "Would you like to save information before exit?\n[Y][N]\n  ")
            save_info = save_info.lower()

            if save_info == 'y':
                write_data_to_file(citys_list)
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
my_city.houses = []

ext = False

#####################################################################################################################


print("")
print("|-_-_-_-_-_-_-_---|> Welcome <|---_-_-_-_-_-_-_-|")
print("")

citys_list = read_data_from_file()


go_on = True
if len(citys_list) > 0:
    my_city, citys_list = choose_city_or_create_a_new_one(my_city, citys_list)
else:
    print(
        "\nYou don't have finished citys yet! To start working with the program, register a new city!")
    while go_on == True:
        new_city = temp_city.register_new_city(citys_list)
        if new_city != None:
            citys_list.append(new_city)
            my_city, citys_list = choose_city_or_create_a_new_one(
                my_city, citys_list)
            go_on = False


go_on = True
if len(my_city.houses) > 0:
    my_house, my_city = choose_house_or_create_a_new_one(my_house, my_city)
else:
    print(
        "\nYou don't have finished homes yet! To start working with the program, register a new house!")
    while go_on == True:
        new_house = temp_house.register_new_house(my_city.houses, my_city)
        if new_house != None:
            my_city.attach_house(new_house)
            my_house, my_city = choose_house_or_create_a_new_one(
                my_house, my_city)
            go_on = False


#####################################################################################################################

main_menu(my_city, my_house, citys_list)
