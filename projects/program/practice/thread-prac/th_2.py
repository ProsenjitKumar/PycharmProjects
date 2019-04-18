from threading import *


class BookMyBus:

    def __init__(self, availableSeats):
        self.availableSeats = availableSeats

    def buy(self, seatsRequested):

        print("Total seats available:",self.availableSeats)

        if self.availableSeats>=seatsRequested:
            print("Confirming a Seat")
            print("Processing the payment")
            print("Printing the ticket")
            self.availableSeats-=seatsRequested
        else:
            print("Sorry. No seats available")


obj = BookMyBus(10)
t1 = Thread(target=obj.buy,args=(3,))
t2 = Thread(target=obj.buy,args=(4,))
t3 = Thread(target=obj.buy,args=(3,))