import uuid


class House:
    """Describes the house, stores information about the number of apartments and residents in it."""

    def __init__(self, ID, house_number, address, floors, communication_access, departmental_affiliation):
        self.ID = ID
        self.house_number = house_number
        self.address = address
        self.floors = floors

        # Тип доступу (індивідуальні, блоковані, секційні, коридорні, галерейні, змішаної структури)
        self.communication_access = communication_access

        # Відомча приналежність (державна, кооперативна, приватна тощо).
        self.departmental_affiliation = departmental_affiliation

        self.flats = []

    def attach_flat(self, flat_ID):
        self.flats.append(flat_ID)

    def print_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"House id: {self.ID}\nHouse number: {self.house_number}\nAdress: {self.address}\nFloors: {self.floors}\nCommunication access: {self.communication_access}\nDepartmental affiliation: {self.departmental_affiliation}\nFlats: [", len(self.flats), "]")

        itr = 1
        for flat in self.flats:
            print(f"[{itr}] - {flat.ID}")
            itr += 1

    def print_short_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"House id: {self.ID}\nHouse number: {self.house_number}\nAdress: {self.address}\nFloors: {self.floors}\nFlats: [", len(self.flats), "]")

    def register_new_house(self, houses_list):

        try:
            print(
                "__________________________________________________________________________________________\n")
            house_nmbr = input("House number: ")
            address = input("House adress: ")
            for house in houses_list:
                if house.house_number == house_nmbr and house.address == address:
                    print("This house is already listed!")
                    return False

            floors = int(input("Number of floors: "))
            if floors <= 0:
                print("A house cannot have less than one floor!")
                return False

            communication_access = input(
                "Communication access (individual, blocked, corridor, gallery, mixed, etc.): ")
            communication_access = communication_access.lower()
            departmental_affiliation = input(
                "Departmental_affiliation (state, cooperative, private, etc.): ")
            departmental_affiliation = departmental_affiliation.lower()

            Id = uuid.uuid4()

            new_house = House(Id, house_nmbr, address, floors,
                              communication_access, departmental_affiliation)

            return new_house
        except Exception as err:
            print("ERROR ---> ", err)


class Flat:
    """Describes the apartment and stores information about its residents"""

    def __init__(self, ID, house, flat_number, floor, rooms, area):
        self.ID = ID
        self.house = house
        self.flat_number = flat_number
        self.floor = floor
        self.rooms = rooms
        self.area = area
        self.residents = []

    def print_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"Flat id: {self.ID}\nHouse address: {self.house.address}\nHouse number: {self.house.house_number}\nFlat number: {self.flat_number}\nFloor: {self.floor}\nRooms: {self.rooms}\nArea: {self.area}\nResidents: [", len(self.residents), "]")

        itr = 1
        for resident in self.residents:
            print(f"[{itr}] - {resident.ID}")
            itr += 1

    def print_short_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"Flat id: {self.ID}\nHouse number: {self.house.house_number}\nHouse address: {self.house.address}\nFlat number: {self.flat_number}\nFloor: {self.floor}\nResidents: [", len(self.residents), "]")

    def attach_resident(self, resident_ID):
        self.residents.append(resident_ID)

    def register_new_flat(self, my_house):
        try:
            print(
                "__________________________________________________________________________________________\n")

            flat_nmbr = int(input("Flat number: "))
            for flat in my_house.flats:
                if flat.flat_number == flat_nmbr:
                    print("This flat is already listed!")
                    return False

            floor = int(input("The apartment is located on the floor: "))
            if 0 > floor > my_house.floors:
                print(
                    f"Wrong floor! There are only {my_house.floors} floors in this building!")
                return False

            rooms = int(input("Number of rooms: "))
            if rooms <= 0:
                print("An apartment cannot have less than 1 room!")
                return False

            area = float(input("Size of apartment in square meters: "))
            if area <= 0:
                print("The apartment cannot be less than 1 square meter!")
                return False

            Id = uuid.uuid4()

            new_flat = Flat(Id, my_house, flat_nmbr, floor, rooms, area)

            return new_flat
        except Exception as err:
            print("ERROR ---> ", err)


class Resident:
    """Description of the person"""

    def __init__(self, ID, name, surname, age, gender, phone_number, email, flat_number):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.flat_number = flat_number

    def print_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"ID: {self.ID}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nGender: {self.gender}\nPhone number: {self.phone_number}\nEmail: {self.email}\nFlat number: {self.flat_number}")

    def register_new_resident(self, flat_number):
        try:
            print(
                "__________________________________________________________________________________________\n")
            name = input("Name: ")
            surname = input("Surname: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            phone_number = input("Phone number: ")
            email = input("Email: ")
            Id = uuid.uuid4()

            new_resident = Resident(Id, name, surname, age,
                                    gender, phone_number, email, flat_number)

            return new_resident
        except Exception as err:
            print("ERROR ---> ", err)
