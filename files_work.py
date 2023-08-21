from second import House, Resident, Flat
import uuid
import csv


def write_data_to_file(houses_list):

    try:
        flats_list = []
        residents_list = []
        data_folder = 'Data_of_program'

        for house in houses_list:

            for flat in house.flats:
                flat.house_ID = house.ID
                flats_list.append(flat)

                for resident in flat.residents:
                    resident.flat_ID = flat.ID
                    residents_list.append(resident)

        with open(f'{data_folder}/houses.csv', 'w', newline='', encoding='utf-8') as houses_file:
            csv_writer = csv.writer(houses_file)
            csv_writer.writerow(['ID', 'house_number', 'address', 'floors',
                                'communication_access', 'departmental_affiliation'])

            for house in houses_list:
                csv_writer.writerow([house.ID, house.house_number, house.address, house.floors,
                                    house.communication_access, house.departmental_affiliation])

        with open(f'{data_folder}/flats.csv', 'w', newline='', encoding='utf-8') as flats_file:
            csv_writer = csv.writer(flats_file)
            csv_writer.writerow(
                ['ID', 'house', 'flat_number', 'floor', 'rooms', 'area', 'house_ID'])

            for flat in flats_list:
                csv_writer.writerow(
                    [flat.ID, 0, flat.flat_number, flat.floor, flat.rooms, flat.area, flat.house_ID])

        with open(f'{data_folder}/residents.csv', 'w', newline='', encoding='utf-8') as residents_file:
            csv_writer = csv.writer(residents_file)
            csv_writer.writerow(['ID', 'name', 'surname', 'age', 'gender',
                                'phone_number', 'email', 'flat_number', 'flat_ID'])

            for resident in residents_list:
                csv_writer.writerow([resident.ID, resident.name, resident.surname, resident.age, resident.gender,
                                    resident.phone_number, resident.email, resident.flat_number, resident.flat_ID])
        return True
    except Exception as err:
        print(f"ERROR: {err}")
        return False


def read_data_from_file():

    try:
        data_folder = 'Data_of_program'
        list_flats = []
        list_houses = []
        lisr_residents = []

        with open(f'{data_folder}/houses.csv', 'r', newline='', encoding='utf-8') as houses_file:
            csv_reader = csv.reader(houses_file)
            next(csv_reader)

            for row in csv_reader:
                house = House(row[0], row[1], row[2], row[3], row[4], row[5])
                list_houses.append(house)

        with open(f'{data_folder}/flats.csv', 'r', newline='', encoding='utf-8') as flats_file:
            csv_reader = csv.reader(flats_file)
            next(csv_reader)

            for row in csv_reader:
                flat = Flat(row[0], row[1], row[2],
                            row[3], row[4], row[5], row[6])
                list_flats.append(flat)

        with open(f'{data_folder}/residents.csv', 'r', newline='', encoding='utf-8') as residents_file:
            csv_reader = csv.reader(residents_file)
            next(csv_reader)

            for row in csv_reader:
                resident = Resident(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                lisr_residents.append(resident)

        for house in list_houses:
            for flat in list_flats:
                if house.ID == flat.house_ID:
                    house.attach_flat(flat)
                    flat.house = house

        for house in list_houses:
            for flat in house.flats:
                for rsdnt in lisr_residents:
                    if rsdnt.flat_ID == flat.ID:
                        flat.attach_resident(resident)

        for house in list_houses:
            house.ID = uuid.UUID(house.ID)
            for flat in house.flats:
                flat.ID = uuid.UUID(flat.ID)
                for rsident in flat.residents:
                    rsident.ID = uuid.UUID(rsident.ID)

        return list_houses

    except Exception as err:
        print(f"ERROR: {err}")
        return False
