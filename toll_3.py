# Toll ver.3 by Ellery alexander setiadi


class Car:  # make a class for car

    def __init__(self, car):  # initialize car in class car
        self.c = car          # declare that car is part of the class

    def get_car(self):  # function for return car
        return self.c   # return car


class Truck:  # make a class for truck

    def __init__(self, truck):  # initialize truck in class truck
        self.t = truck          # declare that truck is part of the class

    def get_truck(self):  # function for return truck
        return self.t     # return truck


class Bus:  # make a class for bus

    def __init__(self, bus):  # initialize bus in class bus
        self.b = bus          # declare that bus is part of the class

    def get_bus(self):  # function for return bus
        return self.b   # return bus


class TollGate1(Car, Bus, Truck):  # make a class for toll gate that inherit from car , bus and truck classes

    def __init__(self, type):  # initialize type
        super().__init__(type)  # make a super class

    def car_fee(self):  # function for car's fee
        Car.get_car = 6000  # car's fee
        return Car.get_car  # return the car's fee

    def bus_fee(self):  # function for bus's fee
        Bus.get_bus = 8000  # bus's fee
        return Bus.get_bus  # return the bus's fee

    def truck_fee(self):  # function for truck's fee
        Truck.get_truck = 10000  # truck's free
        return Truck.get_truck  # return the trucks's fee


class TollGate2(Car, Bus, Truck):  # make a class for toll gate that inherit from car , bus and truck classes

    def __init__(self, type):  # initialize type
        super().__init__(type)  # make a super class

    def car_fee(self):  # function for car's fee
        Car.get_car = 18000  # car's fee
        return Car.get_car  # return the car's fee

    def bus_fee(self):  # function for bus's fee
        Bus.get_bus = 20000  # bus's fee
        return Bus.get_bus  # return the bus's fee

    def truck_fee(self):  # function for truck's fee
        Truck.get_truck = 25000  # truck's free
        return Truck.get_truck  # return the trucks's fee



restart = "Y"  # make a variable call restart


def toll_operator():  # function for toll operator
    car = 0        # the number of car start from 0
    bus = 0        # the number of bus start from 0
    truck = 0      # the number of truck start from 0
    car1 = 0
    bus1 = 0
    truck1 = 0
    while restart != ("N"):  # using while loop which has condition restart is not "N"
        print(
            "=========================================================================================================")
        print(
            "                                     Toll payment systems                                                ")
        print(
            "                                     PT. Jasa Marga, Tbk.                                                ")
        print(
            "=========================================================================================================")

        location = input("location: ")

        print("toll meruya or toll pondok aren ???")
        if location == "meruya":
            print("category of vehicle: ")  # decoration
            print("1. Car (Rp.6.000) \n2. Bus (Rp.8.000) \n3. Truck (Rp.10.000)")  # show the option
            choice = input("type of vehicle: ").lower()  # to input the choice that you want
            TG1 = TollGate1(choice)  # make an object called TG for class TollGate

            if choice == "car":  # if choice is equal to "car" , run the code
                print("Fee: Rp.{}".format(TG1.car_fee()))  # print car's fee from class
                car += 1    # add the number of car by 1
                menu = input("Is there any other vehicle (Y/N)?\n  ").upper()  # make a variable called menu to choose
                # Y to continue the program and N to quit

                if menu == "N":  # if menu is equal to "N"
                    print("toll Meruya")
                    print("car  bus  truck")    # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car, bus, truck))   # print the total number of car,bus,truck
                    print("---------------")
                    revenue = (TG1.car_fee() * car + TG1.bus_fee() * bus + TG1.truck_fee() * truck)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue))  # print the revenue(total fee)
                    print("toll Pondok Aren")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car1, bus1, truck1))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue1 = (TG2.car_fee() * car1 + TG2.bus_fee() * bus1 + TG2.truck_fee() * truck1)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue1))   # print the revenue(total fee)
                    r = revenue + revenue1  # total from revenue and revenue1 for the grand total revenue
                    print("grand total revenue = {}".format(r))
                    print("<exit program>\n have a nice trip")  # print this text

                    break  # stop the program

            elif choice == "bus":  # if choice is equal to bus, run the code
                print("Fee: Rp.{}".format(TG1.bus_fee()))  # print bus's fee from class
                bus += 1    # add the number of bus by 1
                menu = input("Is there any other vehicle (Y/N)?\n ").upper()  # make a variable called menu to choose
                # Y to continue the program and N to quit

                if menu == "N":  # if menu is equal to N
                    print("toll Meruya")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car, bus, truck))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue = (TG1.car_fee() * car + TG1.bus_fee() * bus + TG1.truck_fee() * truck)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue))  # print the revenue(total fee)
                    print("toll Pondok Aren")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car1, bus1, truck1))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue1 = (TG2.car_fee() * car1 + TG2.bus_fee() * bus1 + TG2.truck_fee() * truck1)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue1))  # print the revenue(total fee)
                    r = revenue + revenue1  # total from revenue and revenue1 for the grand total revenue
                    print("grand total revenue = {}".format(r))
                    print("<exit program>\n have a nice trip")  # print this text
                    
                    break  # stop the program

            elif choice == "truck":  # if choice is equal to truck, run the code
                print("Fee: Rp.{}".format(TG1.truck_fee()))  # print truck's fee from class
                truck += 1  # add the number of truck by 1
                menu = input("Is there any other vehicle (Y/N)?\n ").upper()  # make a variable called menu to choose
                # Y to continue the program and N to quit

                if menu == "N":  # if menu is equal to N
                    print("toll Meruya")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car, bus, truck))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue = (TG1.car_fee() * car + TG1.bus_fee() * bus + TG1.truck_fee() * truck)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue))  # print the revenue(total fee)
                    print("toll Pondok Aren")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car1, bus1, truck1))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue1 = (TG2.car_fee() * car1 + TG2.bus_fee() * bus1 + TG2.truck_fee() * truck1)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue1))  # print the revenue(total fee)
                    r = revenue + revenue1  # total from revenue and revenue1 for the grand total revenue
                    print("grand total revenue = {}".format(r))
                    print("<exit program>\n have a nice trip")  # print this text
                    
                    break  # stop the program
        elif location == "pondok aren":
            print("category of vehicle: ")  # decoration
            print("1. Car (Rp.18.000) \n2. Bus (Rp.20.000) \n3. Truck (Rp.25.000)")  # show the option
            choice = input("type of vehicle: ").lower()  # to input the choice that you want
            TG2 = TollGate2(choice)
            if choice == "car":  # if choice is equal to "car" , run the code
                print("Fee: Rp.{}".format(TG2.car_fee()))  # print car's fee from class
                car1 += 1    # add the number of car by 1
                menu = input("Is there any other vehicle (Y/N)?\n  ").upper()  # make a variable called menu to choose
                # Y to continue the program and N to quit

                if menu == "N":  # if menu is equal to "N"
                    print("toll Meruya")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car, bus, truck))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue = (TG1.car_fee() * car + TG1.bus_fee() * bus + TG1.truck_fee() * truck)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue))  # print the revenue(total fee)
                    print("toll Pondok Aren")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car1, bus1, truck1))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue1 = (TG2.car_fee() * car1 + TG2.bus_fee() * bus1 + TG2.truck_fee() * truck1)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue1))  # print the revenue(total fee)
                    r = revenue + revenue1  # total from revenue and revenue1 for the grand total revenue
                    print("grand total revenue = {}".format(r))
                    print("<exit program>\n have a nice trip")  # print this text

                    break  # stop the program

            elif choice == "bus":  # if choice is equal to bus, run the code
                print("Fee: Rp.{}".format(TG2.bus_fee()))  # print bus's fee from class
                bus1 += 1    # add the number of bus by 1
                menu = input("Is there any other vehicle (Y/N)?\n ").upper()  # make a variable called menu to choose
                # Y to continue the program and N to quit

                if menu == "N":  # if menu is equal to N
                    print("toll Meruya")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car, bus, truck))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue = (TG1.car_fee() * car + TG1.bus_fee() * bus + TG1.truck_fee() * truck)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue))  # print the revenue(total fee)
                    print("toll Pondok Aren")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car1, bus1, truck1))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue1 = (TG2.car_fee() * car1 + TG2.bus_fee() * bus1 + TG2.truck_fee() * truck1)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue1))  # print the revenue(total fee)
                    r = revenue + revenue1  # total from revenue and revenue1 for the grand total revenue
                    print("grand total revenue = {}".format(r))
                    print("<exit program>\n have a nice trip")  # print this text
                    
                    break  # stop the program

            elif choice == "truck":  # if choice is equal to truck, run the code
                print("Fee: Rp.{}".format(TG2.truck_fee()))  # print truck's fee from class
                truck1 += 1  # add the number of truck by 1
                menu = input("Is there any other vehicle (Y/N)?\n ").upper()  # make a variable called menu to choose
                # Y to continue the program and N to quit

                if menu == "N":  # if menu is equal to N
                    print("toll Meruya")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car, bus, truck))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue = (TG1.car_fee() * car + TG1.bus_fee() * bus + TG1.truck_fee() * truck)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue))  # print the revenue(total fee)
                    print("toll Pondok Aren")
                    print("car  bus  truck")  # decoration
                    print("---------------")
                    print("{}     {}     {}".format(car1, bus1, truck1))  # print the total number of car,bus,truck
                    print("---------------")
                    revenue1 = (TG2.car_fee() * car1 + TG2.bus_fee() * bus1 + TG2.truck_fee() * truck1)
                    # revenue is the total fee from all vehicle in this toll gate

                    # calculate the total fee from all car, truck, bus
                    print("total revenue = Rp.{}".format(revenue1))  # print the revenue(total fee)
                    # revenue is the total fee from all vehicle in this toll gate
                    r = revenue + revenue1  # total from revenue and revenue1 for the grand total revenue
                    print("grand total revenue = {}".format(r))
                    print("<exit program>\n have a nice trip")  # print this text
                    
                    break  # stop the program

toll_operator()  # call the function toll_operator


