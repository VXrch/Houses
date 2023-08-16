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
    """ 
        def get_ID(self):
            return self.ID

        def get_house_number(self):
            return self.house_number

        def get_adress(self):
            return self.address

        def get_floors(self):
            return self.floors

        def get_communication_access(self):
            return self.communication_access

        def get_departmental_affiliation(self):
            return self.departmental_affiliation

        def get_flats(self):
            return self.flats
    """

    def print_info(self):
        print("__________________________________________________\n")
        print(
            f"House id: {self.ID}\nHouse number: {self.house_number}\nAdress: {self.address}\nFloors: {self.floors}\nCommunication access: {self.communication_access}\nDepartmental affiliation: {self.departmental_affiliation}\nFlats: {self.flats}")

    def register_new_house(self):

        print("__________________________________________________\n")
        house_number = input("Enter house number: ")
        address = input("Enter house adress: ")
        floors = input("Enter number of floors: ")
        communication_access = input(
            "Communication access (individual, blocked, corridor, gallery, mixed, etc.): ")
        departmental_affiliation = input(
            "Departmental_affiliation (state, cooperative, private, etc.): ")
        ID = uuid.uuid4()

        new_house = House(ID, house_number, address, floors,
                          communication_access, departmental_affiliation)

        return new_house


class Flat:
    """Describes the apartment and stores information about its residents"""

    def __init__(self, ID, flat_number, floor, rooms, area):
        self.ID = ID
        self.flat_number = flat_number
        self.floor = floor
        self.rooms = rooms
        self.area = area
        self.residents = []
    """ 
        def get_ID(self):
            return self.ID

        def get_flat_number(self):
            return self.flat_number

        def get_floor(self):
            return self.floor

        def get_rooms(self):
            return self.rooms

        def get_area(self):
            return self.area

        def get_residents(self):
            return self.residents 
    """

    def print_flat_info(self):
        print("__________________________________________________\n")
        print(
            f"Flat id: {self.ID}\nFlat number: {self.flat_number}\nFloor: {self.floor}\nRooms: {self.rooms}\nArea: {self.area}\nResidents: {self.residents}")

    def attach_resident(self, resident):
        self.residents.append(resident)

    def register_new_flat(self):

        print("__________________________________________________\n")
        flat_number = input("Enter flat number: ")
        floor = input("The apartment is located on the floor: ")
        rooms = input("Number of rooms: ")
        area = input("Size of apartment in square meters: ")
        ID = uuid.uuid4()

        new_flat = Flat(ID, flat_number, floor, rooms, area)

        return new_flat


class Resident:
    """Description of the person"""

    def __init__(self, ID, name, surname, age, gender, phone_number, email):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.house = None

    def set_house(self, house):
        self.house = house

    """ 
        def get_ID(self):
            return self.ID

        def get_name(self):
            return self.name

        def get_surname(self):
            return self.surname

        def get_age(self):
            return self.age

        def get_gender(self):
            return self.gender

        def get_phone_number(self):
            return self.phone_number

        def get_email(self):
            return self.email
    """

    def print_info(self):
        print("__________________________________________________\n")
        print(
            f"ID: {self.ID}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nGender: {self.gender}\nPhone number: {self.phone_number}\nEmail: {self.email}")

    def register_new_resident(self):

        print("__________________________________________________\n")
        name = input("Enter resident name: ")
        surname = input("Enter resident surname: ")
        age = input("Enter resident age: ")
        gender = input("Enter resident gender: ")
        phone_number = input("Enter resident phone number: ")
        email = input("Enter resident email: ")
        ID = uuid.uuid4()

        new_resident = Resident(ID, name, surname, age,
                                gender, phone_number, email)

        return new_resident
