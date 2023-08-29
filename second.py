import uuid


class House:
    """Describes the house, stores information about the number of apartments and residents in it."""

    def __init__(self, ID, house_number, address, floors, communication_access, departmental_affiliation, city_ID, city):
        self.ID = ID
        self.house_number = house_number
        self.address = address
        self.floors = int(floors)

        # Тип доступу (індивідуальні, блоковані, секційні, коридорні, галерейні, змішаної структури)
        self.communication_access = communication_access

        # Відомча приналежність (державна, кооперативна, приватна тощо).
        self.departmental_affiliation = departmental_affiliation

        self.flats = []
        self.city_ID = city_ID
        self.city = city

    def attach_flat(self, flat):
        self.flats.append(flat)

    def print_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"House id: {self.ID}\nHouse number: {self.house_number}\nAdress: {self.address}\nCity: {self.city.city_name}\nFloors: {self.floors}\nCommunication access: {self.communication_access}\nDepartmental affiliation: {self.departmental_affiliation}\nFlats: [", len(self.flats), "]")

        itr = 1
        for flat in self.flats:
            print(f"[{itr}] - {flat.ID}")
            itr += 1

    def print_short_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"House id: {self.ID}\nHouse number: {self.house_number}\nAdress: {self.address}\nCity: {self.city.city_name}\nFloors: {self.floors}\nFlats: [", len(self.flats), "]")

    def register_new_house(self, houses_list, city):
        new_house = None
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

            if house_nmbr != '' and address != '' and communication_access != '' and departmental_affiliation != '':

                new_house = House(Id, house_nmbr, address, floors,
                                  communication_access, departmental_affiliation, 0, city)
            else:
                print("You can't register empty value!")

        except ValueError:
            print("Invalid area input. Please enter a valid number!")
        except Exception as err:
            print("ERROR ---> ", err)
        finally:
            return new_house


class Flat:
    """Describes the apartment and stores information about its residents"""

    def __init__(self, ID, house, flat_number, floor, rooms, area, house_ID):
        self.ID = ID
        self.house = house
        self.flat_number = int(flat_number)
        self.floor = int(floor)
        self.rooms = int(rooms)
        self.area = float(area)
        self.house_ID = house_ID
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

    def attach_resident(self, resident):
        self.residents.append(resident)

    def register_new_flat(self, my_house):
        new_flat = None
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
            new_flat = Flat(Id, my_house, flat_nmbr, floor, rooms, area, 0)

        except ValueError:
            print("Invalid area input. Please enter a valid number!")
        except Exception as err:
            print("ERROR ---> ", err)
        finally:
            return new_flat


class Resident:
    """Description of the person"""

    def __init__(self, ID, name, surname, age, gender, phone_number, email, flat_number, flat_ID):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.age = int(age)
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.flat_number = int(flat_number)
        self.flat_ID = flat_ID

    def print_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"ID: {self.ID}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nGender: {self.gender}\nPhone number: {self.phone_number}\nEmail: {self.email}\nFlat number: {self.flat_number}")

    def print_short_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"ID: {self.ID}\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nFlat number: {self.flat_number}")

    def register_new_resident(self, flat_number):
        new_resident = None
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

            if name != '' and surname != '' and gender != '' and phone_number != '' and email != '':
                new_resident = Resident(Id, name, surname, age,
                                        gender, phone_number, email, flat_number, 0)
            else:
                print("You can't register empty value!")

        except ValueError:
            print("Invalid area input. Please enter a valid number!")
        except Exception as err:
            print("ERROR ---> ", err)
        finally:
            return new_resident


class City:
    """Description of the city"""

    def __init__(self, ID, city_name, country, region, year_of_foundation, population, area, population_density):
        self.ID = ID
        self.city_name = city_name
        self.country = country
        self.region = region
        self.year_of_foundation = year_of_foundation
        self.population = population
        self.area = area
        self.population_density = population_density

        self.houses = []

    def attach_house(self, house):
        self.houses.append(house)

    def print_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"City ID: {self.ID}\nCity name: {self.city_name}\nCountry: {self.country}\nRegion: {self.region}\nYear of foundation: {self.year_of_foundation}\nCity division: {self.population}\nArea: {self.area}\nPopulation density: {self.population_density}")
        i = 0
        for house in self.houses:
            print(f"[{i}] house ID: {house.ID}")
            i += 1

    def print_short_info(self):
        print("__________________________________________________________________________________________\n")
        print(
            f"City ID: {self.ID}\nCity name: {self.city_name}\nCountry: {self.country}\nRegion: {self.region}\nRegistered houses: {len(self.houses)}")

    def register_new_city(self, citys_list):
        new_city = None
        try:
            print(
                "__________________________________________________________________________________________\n")

            city_name = input("City name: ")
            for city in citys_list:
                if city.city_name.lower() == city_name.lower():
                    print("This town is alredy listed!")
                    return None

            country = input("Country: ")
            region = input("Region: ")
            year_of_foundation = input("Year of foundation: ")
            population = input("City division: ")

            area = float(input("Area in square meters (number): "))
            if area < 1:
                print("The apartment cannot be less than 1 square meter!")
                return None

            population_density = input("Population density: ")

            Id = uuid.uuid4()

            if city_name != '' and country != '' and region != '' and year_of_foundation != '' and population != '' and population_density != '':
                new_city = City(Id, city_name, country, region,
                                year_of_foundation, population, area, population_density)
            else:
                print("You can't register empty value!")
                return None

        except ValueError:
            print("Invalid area input. Please enter a valid number!")
            return None
        except Exception as err:
            print("ERROR ---> ", err)
        finally:
            return new_city
