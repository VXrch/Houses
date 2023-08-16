class House:
    def __init__(self, adress, floors, communication_access, departmental_affiliation, number_of_apartments):
        self.adress = adress
        self.floors = floors

        # Тип доступу (індивідуальні, блоковані, секційні, коридорні, галерейні, змішаної структури)
        self.communication_access = communication_access

        # Відомча приналежність (державна, кооперативна, приватна тощо).
        self.departmental_affiliation = departmental_affiliation

        self.number_of_apartments = number_of_apartments
        self.house_residents = []

    def get_info(self):
        return (self.adress, self.floors, self.communication_access, self.departmental_affiliation, self.number_of_apartments, self.house_residents)

    def print_info(self):
        print(
            f"Adress: {self.adress}\nFloors: {self.floors}\nCommunication access: {self.communication_access}\nDepartmental affiliation: {self.departmental_affiliation}\nNumber of apartments: {self.number_of_apartments}\nHouse residents: {self.house_residents}")

    def attach_resident(self, resident):
        self.house_residents.append(resident)

    def register_new_house(self):
        adress = input("Enter house adress: ")
        floors = input("Enter number of floors: ")
        communication_access = input(
            "Communication access (individual, blocked, corridor, gallery, mixed, etc.): ")
        departmental_affiliation = input(
            "Departmental_affiliation (state, cooperative, private, etc.): ")
        number_of_apartments = input("Number of apartments: ")
        return (adress, floors, communication_access, departmental_affiliation, number_of_apartments)


class Resident:
    def __init__(self, id, name, surname, age, gender, phone_number, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.email = email

    def print_info(self):
        try:
            print(
                f"ID: {self.id}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nGender: {self.gender}\nPhone number: {self.phone_number}\nEmail: {self.email}")
        except Exception as err:
            print("ERROR: ", err)

    def get_info(self):
        return (self.id, self.name, self.surname, self.age, self.gender, self.phone_number, self.email)

    def register_new_resident(self):
        name = input("Enter resident name: ")
        surname = input("Enter resident surname: ")
        age = input("Enter resident age: ")
        gender = input("Enter resident gender: ")
        phone_number = input("Enter resident phone number: ")
        email = input("Enter resident email: ")
        return (name, surname, age, gender, phone_number, email)


class Flat:
    def __init__(self, flat_number, floor, rooms, area):
        self.flat_number = flat_number
        self.floor = floor
        self.rooms = rooms
        self.area = area
        self.residents = []

    def get_info(self):
        return (self.flat_number, self.floor, self.rooms, self.area, self.residents)

    def print_flat_info(self):
        print(
            f"Flat number: {self.flat_number}\nFloor: {self.floor}\nRooms: {self.rooms}\nArea: {self.area}\nResidents: {self.residents}")

    def attach_resident(self, resident):
        self.residents.append(resident)

    def register_new_flat(self):
        flat_number = input("Enter flat number: ")
        floor = input("The apartment is located on the floor: ")
        rooms = input("Number of rooms: ")
        area = input("Size of apartment in square meters: ")
        return (flat_number, floor, rooms, area)
