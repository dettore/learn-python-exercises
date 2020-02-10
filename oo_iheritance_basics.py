# inheritance

# Python conventions:
# 1. Class names should normally use the CapWords convention.
# 2. Function names should be lowercase, with words separated by underscores as neccessary to improve readability.
# 3. Always use self for the first argument to instance methods.
# 4. Multiline comments should use the # symbol for each line.

# creating an object from a class, nerds call it creating an instance

class AutoMobile:
    '''->Automobile base / parent class'''

    model_year = "2019"

    def start(self):
        print("Automobile is starting ... vroom, vroom!")

    def turn_off(self):
        '''-> shut off auto ...'''
        print("Click, pud, pud ... thud.  Vehicle is off.")


# creating a class called Truck as an inheritance from AutoMobile
# Automobile is the parent of Truck

class Truck(AutoMobile):
    '''-> Truck - a type of automobile. '''

    def __init__(self, year=None):
        if year is None:
            self.year = 2018
        else:
            self.year = year

    def __str__(self):
        return "2019 truck sold by StudioWeb."

    def truck_year(self):
        print("This truck was built in: " + str(self.year))

    def dumpload(self, load=None):
        if load is None:
            print("Truck has nothing to dump.")
        else:
            print("Truck is dumping ... " + str(load))


my_truck = Truck("2021")
my_truck.truck_year()

#create another truck, but don't specify the year
another_truck = Truck()
another_truck.truck_year()

#have the truck dump something
my_truck.dumpload(2000)

#have another truck has nothing to dump
another_truck.dumpload()

print(type(another_truck))
