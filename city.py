from second import City
import uuid


def city_menu(my_city, citys_list):

    ex = False

    while not ex:

        print("\n__________________________________________________________________________________________\n")
        print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
        print()
        print("[1] - Add a city")
        print("[2] - Delete city")
        print("[3] - Change city info")
        print("[4] - Change city to work")
        print()
        print("[5] - Display full list of citys")
        print("[6] - Display information about a specific city")
        print("[7] - Display city to work")
        print()
        print("Display information about citys by: ")
        print("[8] - Country")
        print("[9] - Region")
        print("[10] - Year of foundation")
        print("[11] - population")
        print("[12] - Area")
        print("[13] - Area in range")
        print("[14] - Population density")
        print()
        print("[0] - Go back")
        print("__________________________________________________________________________________________\n")
        action = input("/(o_o)\\  ")

        if action == '0':
            ex = True

        elif action == '1':  # Add a city
            citys_list = add_new_city(citys_list)

        elif action == '2':  # Delete city
            citys_list = delete_city(citys_list, my_city)

        elif action == '3':  # Change city info
            citys_list = change_city_info(citys_list)

        elif action == '4':  # Change the city to work
            my_new_city = change_city_to_work_with(citys_list)
            my_city = my_new_city

        elif action == '5':  # Display full list of citys
            full_citys_list(citys_list)

        elif action == '6':  # Display information about a specific city
            display_info_about_specific_city(citys_list)

        elif action == '7':  # Display my city
            my_city.print_info()

        elif action == '8':  # Display information about citys by country
            print_by_country(citys_list)

        elif action == '9':  # Display information about citys by region
            print_by_region(citys_list)

        elif action == '10':  # Display information about citys by year of foundation
            print_by_year_of_foundation(citys_list)

        elif action == '11':  # Display information about citys by population
            print_by_population(citys_list)

        elif action == '12':  # Display information about citys by area
            print_by_area(citys_list)

        elif action == '13':  # Display information about citys by area in range
            print_by_area_in_range(citys_list)

        elif action == '14':  # Display information about citys by population density
            print_by_population_density(citys_list)

        else:
            print("That option is not on the menu!")

        input("Press any key to continue... ")

    return my_city, citys_list


def add_new_city(citys_list):
    temp_city = City(0, 0, 0, 0, 0, 0, 0, 0)

    new_city = temp_city.register_new_city(citys_list)
    if new_city != None:
        citys_list.append(new_city)

    return citys_list


def delete_city(citys_list, my_city):
    try:

        print("\nChoose city to delete: ")
        full_citys_list(citys_list)

        choice = input("Enter city id: ")
        choice_uuid = uuid.UUID(choice)

        if choice == my_city.ID:
            print("You can't delete a city that's currently in robot. Change the active city to another one and try again!")
        else:
            for city_number, city in enumerate(citys_list):
                if city.ID == choice_uuid:
                    citys_list.pop(city_number)
                    deleted = True

            if not deleted:
                text = ""
                print(f"{text:.^5} City is not found! Try again later! {text:.^5}")
            else:
                text = ""
                print(f"{text:.^5} City was successfully deleted! {text:.^5}")

    except TypeError:
        print("Wrong type!")
    except Exception as err:
        print("ERROR ---> ", err)
    finally:
        return citys_list


def change_city_info(citys_list):
    full_citys_list(citys_list)

    city_to_change_info = input("Enter city ID: ")
    city_to_change_info = uuid.UUID(city_to_change_info)

    info_to_change = input(
        "What do you want to change?\n[1] - City name\n[2] - Country\n[3] - Region\n[4] - Year of foundationation\n[5] - population\n[6] - Area\n[7] - Population density\n[0] - Go back")

    try:

        for city in citys_list:
            if city.ID == city_to_change_info:

                if info_to_change == '1':  # City name
                    new_info = input(
                        "Enter new city name (or [exit] to exit): ")
                    if new_info != 'exit':
                        city.city_name = new_info

                elif info_to_change == '2':  # Country
                    new_info = input(
                        "Enter new country (or [exit] to exit): ")
                    if new_info != 'exit':
                        city.country = new_info

                elif info_to_change == '3':  # Region
                    new_info = input(
                        "Enter new city region (or [exit] to exit): ")
                    if new_info != 'exit':
                        city.region = new_info

                elif info_to_change == '4':  # Year of foundationation
                    new_info = input(
                        "Enter new year of foundationation (or [exit] to exit): ")
                    if new_info != 'exit':
                        city.year_of_foundationation = new_info

                elif info_to_change == '5':  # population
                    new_info = input(
                        "Enter new population (or [exit] to exit): ")
                    if new_info != 'exit':
                        city.population = new_info

                elif info_to_change == '6':  # Area
                    new_info = float(input(
                        "Enter new city area (or [0] to exit): "))
                    if new_info != 0:
                        city.area = new_info

                elif info_to_change == '7':  # Population density
                    new_info = input(
                        "Enter new population density (or [0] to exit): ")
                    if new_info != '0':
                        city.population_density = new_info

                elif info_to_change == '0':
                    print()
                else:
                    print("That option is not on the menu!")

    except TypeError:
        print("Type error! You must enter a number!")
    except Exception as err:
        print("\n________________________ERROR ----- >",
              err, "________________________")

    return citys_list


def choose_city_to_work_with(citys_list):

    ext = False

    while not ext:

        full_citys_list(citys_list)

        print("\n-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
        city_to_work = input("Enter city id to work with: ")
        city_to_work = uuid.UUID(city_to_work)

        for city in citys_list:
            if city.ID == city_to_work:
                return city

        print("Wrong ID! Try again!")
        input("")


def change_city_to_work_with(citys_list):

    full_citys_list(citys_list)

    city_to_work = input("Enter city id to work with: ")
    city_to_work = uuid.UUID(city_to_work)

    for city in citys_list:
        if city.ID == city_to_work:
            print("city was found!")
            return city

    print("City is not found!")


def print_by_country(citys_list):

    search = input("Enter country to search for: ")

    find = False

    for city in citys_list:
        if city.country == search:
            city.print_short_info()

    if find == False:
        print("City is not found!")


def print_by_region(citys_list):

    search = input("Enter region to search for: ")

    find = False

    for city in citys_list:
        if city.region == search:
            city.print_short_info()

    if find == False:
        print("City is not found!")


def print_by_year_of_foundation(citys_list):

    search = input("Enter year of foundation to search for: ")

    find = False

    for city in citys_list:
        if city.year_of_foundation == search:
            city.print_short_info()

    if find == False:
        print("City is not found!")


def print_by_population(citys_list):

    search_min = input("Enter min range of population to search for: ")
    search_max = input("Enter max range of population to search for: ")

    find = False

    for city in citys_list:
        if search_min <= city.population <= search_max:
            city.print_short_info()

    if find == False:
        print("City is not found!")


def print_by_area(citys_list):

    search = input("Enter area to search for: ")

    find = False

    for city in citys_list:
        if city.area == search:
            city.print_short_info()

    if find == False:
        print("City is not found!")


def print_by_area_in_range(citys_list):

    search_min = input("Enter min range of area to search for: ")
    search_max = input("Enter max range of area to search for: ")

    find = False

    for city in citys_list:
        if search_min <= city.area <= search_max:
            city.print_short_info()

    if find == False:
        print("City is not found!")


def print_by_population_density(citys_list):

    search = input("Enter population density to search for: ")

    find = False

    for city in citys_list:
        if city.population_density == search:
            city.print_short_info()

    if find == False:
        print("City is not found!")


def full_citys_list(citys_list):
    for city in citys_list:
        city.print_short_info()


def display_info_about_specific_city(citys_list):

    full_citys_list(citys_list)

    city_to_display = input("Enter city ID to search full info: ")
    city_to_display = uuid.UUID(city_to_display)

    for city in citys_list:
        if city.ID == city_to_display:
            city.print_info()


def choose_city_or_create_a_new_one(my_city, citys_list):

    ext = False
    temp_city = City(0, 0, 0, 0, 0, 0, 0, 0)

    while ext == False:

        full_citys_list(citys_list)

        print(
            "\nDo you want to continue working with what we already have or create a new one?")
        move_on = input("[1] - Continue\n[2] - Create a new one\n : ")

        if move_on == '1':

            if len(citys_list) == 1:
                for city in citys_list:
                    my_city = city
            else:
                my_city = choose_city_to_work_with(citys_list)

            ext = True

        elif move_on == '2':
            new_city = temp_city.register_new_city(citys_list)
            if new_city != None:
                citys_list.append(new_city)
                move_on = input(
                    "The city is registered! Start working with this city?\n [Y][N]\n : ")
                move_on = move_on.lower()

                if move_on == 'y':
                    my_city = new_city
                    ext = True
                else:
                    print("Ok! Then let's create a new city!")

    return my_city, citys_list
