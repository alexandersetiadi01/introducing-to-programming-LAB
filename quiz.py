class Single:                       # class for single room
    def __init__(self, single):     # initialize single
        self.s = single

    def get_room(self):             # get room for single
        return self.s               # return self.s


class Double:                       # class for double room
    def __init__(self, double):     # initialize double
        self.d = double

    def get_room(self):             # get room for double
        return self.d               # return self.d


class Elite:                        # class for elite room
    def __init__(self, elite):      # initialize elite
        self.e = elite

    def get_room(self):             # get room for elite
        return self.e               # return self.e


class Hotel(Single, Double, Elite): # make a class for hotel
    def __init__(self, category):   # initialize category
        super().__init__(category)  # use super class

    def single_price(self):         # function for single room's price
        self.s = 150000             # value of s is 150000
        return self.s               # return the value

    def double_price(self):         # function for double room's price
        self.d = 300000             # value of d is 300000
        return self.d               # return the value

    def elite_price(self):          # function for elite room's price
        self.e = 450000             # value of e is 450000
        return self.e               # return the value


restart = "Y"                       # restart is equal to Y


def receptionist():                 # function for receptionist
    single = []                     # empty array for single
    double = []                     # empty array for double
    elite = []                      # empty array for elite
    available_s = 5                # set available for single room to 5
    available_d = 3                # set available for double room to 3
    available_e = 2                 # set available for elite room to 2

    while restart != ("N"):
        print("1. check in\n2. check out\n3. reservation list")
        choice = input("=> ")       # type your choice
        if choice == "1":           # if choice is equal to 1, run the code
            print("available room: single = {} double = {} elite = {} ".format(available_s, available_d, available_e))
            print("room in use: single = {} double = {} elite = {}".format(len(single), len(double), len(elite)))
            print("category: 1.single 2.double 3.elite")
            category = input("category: ")  # choose your room category
            h = Hotel(category)             # create variable h to call class hotel
            if category == "1":             # if category is equal to 1, run the code
                if len(single) <= 5:       # len single is less or equal to 5
                    time = int(input("how long: ")) # input your time
                   print("Rp.{}".format(h.single_price() * time))  # print single room price times time
                    room_number = input("what is your reservation name:")   # enter your reservation name
                    single.append(room_number)      # add it to single
                    available_s -= 1                # decrease available s by 1        
                    menu = input("Y to continue the program/N to quit = ").upper() # choose what to do with the program
                    if menu == "N": # if menu is N, run the code
                        print("available room: single = {} double = {} elite = {} ".format(available_s, available_d,
                                                                                           available_e))
                        print("room in use: single = {} double = {} elite = {}".format(len(single), len(double),
                                                                                       len(elite)))
                        break       # stop the code
                elif len(single) > 15:                  # if len single is more than 15, show this text
                    print("no more room for single")

            if category == "2":
                if len(double) <= 3:
                    time = int(input("how long: "))  # input your time
                    print("Rp.{}".format(h.double_price() * time))  # print double room price times time
                    room_number = input("what is your reservation name: ")  # enter your reservation name
                    double.append(room_number)      # add it to double
                    available_d -= 1                # decrease available d decrease by 1
                    menu = input("Y to continue the program/N to quit = ").upper()  # choose what to do with the program
                    if menu == "N":
                        print("available room: single = {} double = {} elite = {} ".format(available_s, available_d,
                                                                                           available_e))
                        print("room in use: single = {} double = {} elite = {}".format(len(single), len(double),
                                                                                       len(elite)))
                        break       # stop the program
                elif len(double) > 13:  # if len double is more than 13, show this text
                    print("no more room for double")

            if category == "3":                 # if category is 3, run the code
                if len(elite) <= 2:             # if len elite is less or equal to 8, run the code
                    time = int(input("how long: "))  # input your time
                    print("Rp.{}".format(h.single_price() * time))  # print elite room price times time
                    room_number = input("what is your reservation name:")   # enter your reservation name
                    elite.append(room_number)       # add it to elite
                    available_e -= 1                # available e is decreased by 1
                    menu = input("Y to continue the program/N to quit = ").upper()  # choose what to do with the program
                    if menu == "N":
                        print("available room: single = {} double = {} elite = {} ".format(available_s, available_d,
                                                                                           available_e))
                        print("room in use: single = {} double = {} elite = {}".format(len(single), len(double),
                                                                                       len(elite)))
                        break

                else:
                    print("no more room for elite")

        elif choice == "2":   # if choice is equal to 2, run the code
            print("available room: single = {} double = {} elite = {} ".format(available_s, available_d, available_e))
            print("room in use: single = {} double = {} elite = {}".format(len(single), len(double), len(elite)))
            print("category: 1.single 2.double 3.elite")
            category = input("category: ")  # choose the room's category
            if category == "1":             # if category is 1, run the code
                room_number = input("what is your reservation name:")   # enter your reservation name
                if room_number in list(single): # if room_number is in list single, run this code
                    single.remove(room_number)  # remove it from single
                    available_s += 1            # increase available s by 1             
                    menu = input("Y to continue the program/N to quit = ").upper()  # choose what to do with the program
                    if menu == "N":
                        print("available room: single = {} double = {} elite = {} ".format(available_s, available_d,
                                                                                           available_e))
                        print(
                            "room in use: single = {} double = {} elite = {}".format(len(single), len(double), len(elite)))
                        break
            if category == "2":     # if category is equal to 2, run the code
                room_number = input("what is your reservation name:")  # enter your reservation name
                if room_number in list(double):  # if room_number is in list double, run this code
                    double.remove(room_number)   # remove it form double
                    available_d += 1             # increase available d by 1
                    menu = input("Y to continue the program/N to quit = ").upper()  # choose what to do with the program
                    if menu == "N":
                        print("available room: single = {} double = {} elite = {} ".format(available_s, available_d,
                                                                                           available_e))
                        print("room in use: single = {} double = {} elite = {}".format(len(single), len(double),
                                                                                       len(elite)))
                        break
            if category == "3":     # if category is 3, run the code
                room_number = input("what is your reservation name:")  # enter your reservation name
                if room_number in list(elite):  # if room_number is in list elite, run this code
                    elite.remove(room_number)   # remove it from elite
                    available_e += 1            # increase available e by 1
                    menu = input("Y to continue the program/N to quit = ").upper()  # choose what to do with the program
                    if menu == "N":
                        print("available room: single = {} double = {} elite = {} ".format(available_s, available_d,
                                                                                           available_e))
                        print("room in use: single = {} double = {} elite = {}".format(len(single), len(double),
                                                                                       len(elite)))
                        break
            
          elif choice == "3":
            print("reservation list:")
            print("single: {}".format(single))      # get the entire list of single room
            print("double: {}".format(double))      # get the entire list of double room
            print("elite: {}".format(elite))        # get the entire list of elite room

receptionist()          # call function receptionist


