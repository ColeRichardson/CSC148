
class Building:
    """A building
    Precondition: no rooms can have the same name, all room names must be unique
    >>> Building1 = Building('1234 thomas st', 5)
    >>> Building1.address
    '1234 thomas st'
    >>> Building1.num_rooms
    5

    """
    def __init__(self, address: str, num_rooms: int):
        """Initialize the Building, occurs at time of construction
        >>> Building1 = Building('1234 thomas st', 5)
        >>> Building1.address
        '1234 thomas st'
        >>> Building1.num_rooms
        5
        >>> Building1.rooms
        []
        """
        self.address = address
        self.num_rooms = num_rooms
        self.rooms = []

    def __str__(self):
        """prints the sum of the square footages of all the rooms in the building.
        >>> Building1 = Building("1234 thomas st", 5)
        >>> foyer = Room("foyer", 100.5)
        >>> Building1.add_room(foyer)
        >>> den = Room("den", 50.6)
        >>> Building1.add_room(den)
        >>> print(Building1)
        151.1
        """
        sum_sqft = 0
        for room in self.rooms:
            sum_sqft += room.sqr_ft
        return str(sum_sqft)

    def add_room(self, room):
        """adds the room to the buildings list of rooms
        room: Room object
        >>> Building1 = Building("1234 thomas st", 2)
        >>> foyer = Room("foyer", 100.1)
        >>> Building1.add_room(foyer)
        >>> print(Building1)
        100.1
        >>> den = Room("den", 50.6)
        >>> Building1.add_room(den)
        >>> print(Building1)
        150.7
        """
        self.rooms.append(room)

    def rename_room(self, old: str, new: str):
        """renames the room name, takes in the old name,
         which is also the Room object and renames that room to the new name
        >>> Building1 = Building("1234 thomas st", 2)
        >>> foyer = Room("foyer", 100)
        >>> Building1.add_room(foyer)
        >>> foyer.name
        'foyer'
        >>> Building1.rename_room('foyer', 'hall')
        >>> foyer.name
        'hall'
        """
        for room in self.rooms:
            if room.name == old:
                room.name = new
                break

class House(Building):
    """ a type of building that is a house, with a max of 10 rooms
    and a different __str__ method
    Precondition: num_rooms <= 10
    Precondition: no rooms can have the same name, all room names must be unique
    >>> my_house = House('3456 appleview cr', 2)
    >>> bedroom = Room('bedroom', 12.2)
    >>> kitchen = Room('kitchen', 13.3)
    >>> my_house.add_room(bedroom)
    >>> my_house.add_room(kitchen)
    >>> my_house.rooms
    [bedroom, kitchen]
    >>> print(my_house)
    "Welcome to our house"
    "bedroom, 12.2"
    "kitchen, 13.3"
    """

    def __init__(self, name: str, num_rooms: int):
        """initialize this house at time of construction
        num_rooms <= 10
        >>> Building1 = Building("1234 thomas st", 5)
        >>> Building1.address
        "1234 thomas st"
        >>> Building1.num_rooms
        5
        >>> Building1.rooms
        []
        """
        self.name = name
        self.num_rooms = num_rooms
        self.rooms = []

    def __str__(self):
        """prints "Welcome to our house"
        and each room and square footage, seperated by commas
        >>> my_house = House('my_house', 2)
        >>> bedroom = Room('bedroom', 12.2)
        >>> kitchen = Room('kitchen', 13.3)
        >>> my_house.add_room(bedroom)
        >>> my_house.add_room(kitchen)
        >>> my_house.rooms
        [bedroom, kitchen]
        >>> print(my_house)
        "Welcome to our house"
        "bedroom, 12.2"
        "kitchen, 13.3"
        """
        print("Welcome to our house")
        for room in self.rooms:
            print(room.name, room.sqr_ft)

class Business(Building):
    """ a type of building that is a business, with no limit on number of rooms,
    but no room can be named Bedroom
    and all rooms square footage must be at least 100
    Precondition: no rooms in the same building can have the same name
    all room names within the same building must be unique

    """
    def __init__(self, name, num_rooms):
        """ initializes the business building
        preconditions: num_rooms > 0, Room.name != Bedroom, Room.sqr_ft >= 100
        >>> Business1 = Business("1234 maple st", 2)
        >>> Business1.address
        "1234 maple st"
        >>> Business1.num_rooms
        2
        >>> Business1.rooms
        []
        """
        self.name = name
        self.num_rooms = num_rooms
        self.rooms = []

    def change_sqrft(self, name: str, new_sqrft: str):
        """ renames the old room to the new name of the room.
        >>> Business1 = Business("1234 maple st", 2)
        >>> Business1.address
        "1234 maple st"
        >>> kitchen = Room('kitchen', 101)
        >>> main_office = Room('main_office', 200)
        >>> Business1.add_room(kitchen)
        >>> Business1.add_room(main_office)
        >>> print(Business1)
        301
        >>> Business1.change_sqrft(kitchen, 201)
        >>> print(Business1)
        401
        """
        for room in self.rooms:
            if room.name == name:
                room.sqr_ft = new_sqrft
                break

class Room:
    """A room inside a building
    >>> Room1 = Room("bedroom", 100)
    >>> Room1.name
    bedroom
    >>> Room1.sqr_ft
    100
    """
    def __init__(self, name: str, sqr_ft: float):
        """Initialize a room, occurs at time of construction
        """
        self.name = name
        self.sqr_ft = sqr_ft

if __name__ == '__main__':
    check = True
    while check:
        building = input('please enter the type of building, must be a building, house, or business.')
        if building != 'building' or building != 'business' or building != 'house':
            print('sorry you didnt type in a correct name for the building type, its case sensitive, please try again')
            continue
        address = input('please enter the address of the building ?')
        num_rooms = int(input('please enter the number of rooms.'))
        if building == 'building':
            print(address)
            temp = Building(address, num_rooms)
            print(address)
            check = False
        elif building == 'house':
            if num_rooms > 10:
                num_rooms = int(input('sorry, the maximum number of rooms for a house is 10, please enter a number of rooms less than or equal to 10'))
            temp = House(address, num_rooms)
            check = False
        elif building == 'business':
            temp = Business(address, num_rooms)
            check = False

    if not check:
        for i in range(0, num_rooms):
            name = input('what is the name of the room?')
            if building == 'business':
                if name == 'Bedroom' or name == 'bedroom':
                    name = input('sorry, a room in a business cannot be named bedroom or Bedroom please choose another name')
            sqrft = float(input('what is the square footage of the room?'))
            if building == 'business':
                if sqrft < 100:
                    sqrft = float(input('sorry the minimum square footage for a room in a business is 100 please enter a number for square footage greater than or equal to 100'))
            room = Room(name, sqrft)
            temp.add_room(room)

