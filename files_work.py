from second import House, Flat, Resident, City
import uuid
import csv


def files_menu(citys_list):

    ex = False

    while not ex:

        print("\n__________________________________________________________________________________________\n")
        print("(/'O_O)/'--->  What would you like to do?  <---'\\(O_O'\\)")
        print()
        print("[1] - Save information to a file")
        print("[2] - Uploading information from a file")
        print("[3] - Clear all data")
        print()
        print("[4] - Clear data from the citys file")
        print("[5] - Clear data from the houses file")
        print("[6] - Clear data from the flats file")
        print("[7] - Clear data from the residents file")
        print()
        print("[0] - Go back")
        print("\n__________________________________________________________________________________________\n")
        action = input("/(o_o)\\  ")

        if action == '0':  # Exit
            ex = True

        elif action == '1':  # Save information to a file
            write_data_to_file(citys_list)

        elif action == '2':  # Uploading information from a file
            citys_list = read_data_from_file()

        elif action == '3':  # Clear all data
            clear_all_program_data()

        elif action == '4':  # Clear data from the citys file
            clear_data('citys')

        elif action == '5':  # Clear data from the houses file
            clear_data('houses')

        elif action == '6':  # Clear data from the flats file
            clear_data('flats')

        elif action == '7':  # Clear data from the residents file
            clear_data('residents')
        else:
            print("Wrong choice!")

    return citys_list


def write_data_to_file(citys_list):
    try:
        file_1 = 'Data_of_program/citys.csv'
        file_2 = 'Data_of_program/houses.csv'
        file_3 = 'Data_of_program/flats.csv'
        file_4 = 'Data_of_program/residents.csv'

        houses_list = []
        flats_list = []
        residents_list = []

        for city in citys_list:
            for house in city.houses:
                house.city_ID = city.ID
                houses_list.append(house)

                for flat in house.flats:
                    flat.house_ID = house.ID
                    flats_list.append(flat)

                    for resident in flat.residents:
                        resident.flat_ID = flat.ID
                        residents_list.append(resident)

        with open(file_1, 'w', newline='', encoding='utf-8') as citys_file:
            csv_writer = csv.writer(citys_file)
            csv_writer.writerow(['ID', 'city_name', 'country', 'region',
                                'year_of_foundation', 'population', 'area', 'population_density'])

            for city in citys_list:
                csv_writer.writerow(
                    [city.ID, city.city_name, city.country, city.region, city.year_of_foundation, city.population, city.area, city.population_density])

        with open(file_2, 'w', newline='', encoding='utf-8') as houses_file:
            csv_writer = csv.writer(houses_file)
            csv_writer.writerow(['ID', 'house_number', 'address', 'floors',
                                'communication_access', 'departmental_affiliation', 'city_ID', 'city'])

            for house in houses_list:
                csv_writer.writerow([house.ID, house.house_number, house.address, house.floors,
                                    house.communication_access, house.departmental_affiliation, house.city_ID, house.city])

        with open(file_3, 'w', newline='', encoding='utf-8') as flats_file:
            csv_writer = csv.writer(flats_file)
            csv_writer.writerow(
                ['ID', 'house', 'flat_number', 'floor', 'rooms', 'area', 'house_ID'])

            for flat in flats_list:
                csv_writer.writerow(
                    [flat.ID, flat.house, flat.flat_number, flat.floor, flat.rooms, flat.area, flat.house_ID])

        with open(file_4, 'w', newline='', encoding='utf-8') as residents_file:
            csv_writer = csv.writer(residents_file)
            csv_writer.writerow(['ID', 'name', 'surname', 'age', 'gender',
                                'phone_number', 'email', 'flat_number', 'flat_ID'])

            for resident in residents_list:
                csv_writer.writerow([resident.ID, resident.name, resident.surname, resident.age, resident.gender,
                                    resident.phone_number, resident.email, resident.flat_number, resident.flat_ID])

        return True

    except Exception as err:
        print(f"ERROR WITH WRITING TO FILE: {err}")
        return False


def read_data_from_file():

    try:
        file_1 = 'Data_of_program/citys.csv'
        file_2 = 'Data_of_program/houses.csv'
        file_3 = 'Data_of_program/flats.csv'
        file_4 = 'Data_of_program/residents.csv'

        list_of_citys = []
        list_houses = []
        list_flats = []
        list_residents = []

        with open(file_1, 'r', newline='', encoding='utf-8') as citys_file:
            csv_reader = csv.reader(citys_file)
            next(csv_reader)

            for row in csv_reader:
                city = City(row[0], row[1], row[2], row[3],
                            row[4], row[5], row[6], row[7])
                list_of_citys.append(city)

        with open(file_2, 'r', newline='', encoding='utf-8') as houses_file:
            csv_reader = csv.reader(houses_file)
            next(csv_reader)

            for row in csv_reader:
                house = House(row[0], row[1], row[2],
                              row[3], row[4], row[5], row[6], row[7])
                list_houses.append(house)

        with open(file_3, 'r', newline='', encoding='utf-8') as flats_file:
            csv_reader = csv.reader(flats_file)
            next(csv_reader)

            for row in csv_reader:
                flat = Flat(row[0], row[1], row[2],
                            row[3], row[4], row[5], row[6])
                list_flats.append(flat)

        with open(file_4, 'r', newline='', encoding='utf-8') as residents_file:
            csv_reader = csv.reader(residents_file)
            next(csv_reader)

            for row in csv_reader:
                resident = Resident(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                list_residents.append(resident)

        for city in list_of_citys:
            for house in list_houses:
                if city.ID == house.city_ID:
                    city.attach_house(house)
                    house.city = city

        for house in list_houses:
            for flat in list_flats:
                if house.ID == flat.house_ID:
                    house.attach_flat(flat)
                    flat.house = house

        for house in list_houses:
            for flat in house.flats:
                for rsdnt in list_residents:
                    if rsdnt.flat_ID == flat.ID:
                        flat.attach_resident(rsdnt)

        for city in list_of_citys:
            city.ID = uuid.UUID(city.ID)
            for house in city.houses:
                house.ID = uuid.UUID(house.ID)
                for flat in house.flats:
                    flat.ID = uuid.UUID(flat.ID)
                    for rsident in flat.residents:
                        rsident.ID = uuid.UUID(rsident.ID)

        return list_of_citys

    except TypeError as err:
        print("Type Error -----> ", err)
        return []

    except Exception:
        return []


def clear_all_program_data():

    try:

        print("If you continue, all information from ALL files will be erased without the possibility of recovery!")
        move_on = input("Are you sure you want to continue?\n[Y][N]\n  ")
        move_on = move_on.lower()
        if move_on == 'y':
            print("Ok!")
        else:
            return None

        file_1 = 'Data_of_program/citys.csv'
        file_2 = 'Data_of_program/houses.csv'
        file_3 = 'Data_of_program/flats.csv'
        file_4 = 'Data_of_program/residents.csv'

        with open(file_1, 'w') as file:
            file.truncate(0)
        with open(file_2, 'w') as file:
            file.truncate(0)
        with open(file_3, 'w') as file:
            file.truncate(0)
        with open(file_4, 'w') as file:
            file.truncate(0)

        print("Data was successfully cleared!")
        return True

    except Exception as err:
        print("ERROR IN CLEARING DATA -----> ", err)
        return False


def clear_data(file_to_clear):

    print("If you continue, all information from this file will be erased without the possibility of recovery!")
    move_on = input("Are you sure you want to continue?\n[Y][N]\n  ")
    move_on = move_on.lower()

    if move_on == 'y':
        print("Ok!")
    else:
        return None

    file_to_clear = 'Data_of_program/' + file_to_clear + '.csv'

    try:
        with open(file_to_clear, 'w') as file:
            file.truncate(0)

        print("Data was successfully cleared!")
        return True

    except Exception as err:
        print("ERROR IN CLEARING DATA -----> ", err)
        return False
