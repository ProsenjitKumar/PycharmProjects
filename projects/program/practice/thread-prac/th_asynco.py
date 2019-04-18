from threading import *


class BookingBus():
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        # self.l = Lock()
        self.l = Semaphore()

    def buy(self, requestedSeats):
        self.l.acquire()
        print("Total seats available:", self.availableSeats)
        if self.availableSeats >= requestedSeats:
            print("confirming Seat")
            print('\n')
            self.availableSeats -= requestedSeats
        else:
            print("Sorry! Seats Limited.")
        self.l.release()


objBookingBus = BookingBus(15)
t1 = Thread(target=objBookingBus.buy, args=(5,))
t2 = Thread(target=objBookingBus.buy, args=(5,))
t3 = Thread(target=objBookingBus.buy, args=(6,))

t1.start()
t2.start()
t3.start()



