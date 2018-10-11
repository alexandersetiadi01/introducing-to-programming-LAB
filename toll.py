# Toll ver.1 by Ellery alexander setiadi

class Car:                      # make a class for car

    def __init__(self, car):    # initialize car in class car
        self.c = car            # declare that car is part of the class

    def get_car(self):          # function for return car
        return self.c           # return car


class Truck:                    # make a class for truck

    def __init__(self, truck):  # initialize truck in class truck
        self.t = truck          # declare that truck is part of the class

    def get_truck(self):        # function for return truck
        return self.t           # return truck


class Bus:                      # make a class for bus

    def __init__(self, bus):    # initialize bus in class bus
        self.b = bus            # declare that bus is part of the class

    def get_bus(self):          # function for return bus
        return self.b           # return bus


class TollGate(Car, Bus, Truck):    # make a class for toll gate that inherit from car , bus and truck classes

    def __init__(self, type):       # initialize type
        super().__init__(type)      # make a super class

    def car_fee(self):              # function for car's fee
        Car.get_car = 6000          # car's fee
        return Car.get_car          # return the car's fee

    def bus_fee(self):              # function for bus's fee
        Bus.get_bus = 8000          # bus's fee
        return Bus.get_bus          # return the bus's fee

    def truck_fee(self):            # function for truck's fee
        Truck.get_truck = 10000     # truck's free
        return Truck.get_truck      # return the trucks's fee


restart = "Y"                       # make a variable call restart


def toll_operator():                # function for toll operator
    while restart != ("N"):         # using while loop which has condition restart is not "N"
        print("|=========<Toll>=========|")     # decoration
        print("category of vehicle: ")          # decoration
        print("1. Car (Rp.6.000) \n2. Bus (Rp.8.000) \n3. Truck (Rp.10.000)") # show the option
        choice = input("type of vehicle: ").lower()  # to input the choice that you want
        TG = TollGate(choice)   # make an object called TG for class TollGate
        if choice == "car":     # if choice is equal to "car" , run the code
            print("Fee: Rp.{}".format(TG.car_fee()))    # print car's fee from class
            menu = input("Is there any other vehicle (Y/N)?\n  ").upper()   # make a variable called menu to choose
            #Y to continue the program and N to quit

            if menu == "N":     # if menu is equal to "N"
                print("<exit program>\n have a nice trip")  # print this text
                break       # stop the program

        elif choice == "bus":   # if choice is equal to bus, run the code
            print("Fee: Rp.{}".format(TG.bus_fee()))    # print bus's fee from class
            menu = input("Is there any other vehicle (Y/N)?\n ").upper()    # make a variable called menu to choose
            #Y to continue the program and N to quit

            if menu == "N": #if menu is equal to N
                print("<exit program> \n have a nice trip")  # show this text
                break   # stop the program

        elif choice == "truck": # if choice is equal to truck, run the code
            print("Fee: Rp.{}".format(TG.truck_fee()))  # print truck's fee from class
            menu = input("Is there any other vehicle (Y/N)?\n ").upper()# make a variable called menu to choose
            #Y to continue the program and N to quit

            if menu == "N": # if menu is equal to N
                print("<exit program> \n have a nice trip") # show this text
                break   # stop the program


toll_operator()     # call the function toll_operator


