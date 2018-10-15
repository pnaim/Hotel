from datetime import datetime, date
from threading import Thread
import threading

class Stay:
    def __init__(self, room_type: '', from_date: '00-00-0000', days: 0, price: 0.0):
        self._room_type = room_type
        self._from_date = from_date
        self._days = days
        self._price = price
    def __str__(self):
        return '\nType of room: %s\nDate of check-in: %s\nNumber of days: %s\nTotal price: %d\n'%(self._room_type, self._from_date, self._days, self._price)
    def set_room_type(self, room_type):
        while True:
            try:
                try:
                    rooms = open('rooms.txt', 'r')
                except IOError:
                    print('Files for reading the kinds of rooms corrupt or not found\n')
                list= []
                for line in rooms:
                    room = line.strip()
                    list.append(room)
                rooms.close()
                print('\nSelect the type of room that interests: ')
                room = input('')
                if room in list:
                    room_type = room
                    self._room_type = room_type
                    break
                elif room.islower():
                    raise ValueError
                else:
                    print('Enter a type of room available\n')
            except ValueError:
                print('Enter a room with the first letter capitalised\n')

    def get_days(self):
        return self._days

    def set_price(self, price):
        try:
            cal_price = open('price_rooms','r')
        except IOError:
            print('Files for searching prices corrupt or not found')
        for type in cal_price:
            line = type.strip()
            list = line.split()
            if list[0] == self._room_type:
                price == float(list[1])*self._days
                self._price = price
                break
        cal_price.close()

    def set_days(self, days):
        while True:
            try:
                print('How many days you want to stay?\n')
                ndays = int(input(''))
                if ndays >= 1:
                    days = ndays
                    self._days = days
                    break
                elif ndays == 0:
                    print('Enter a valid number of nights')
            except ValueError:
                print('Enter a valid character')


    def set_from_date (self, from_date):
            date_today = date.today()
            print('Insert the date of arrival:')
            while True:
                dt = select_date()
                if dt >= date_today:
                    from_date = dt
                    self._from_date= from_date
                    break
                else:
                    print('The date is not available')

def select_date():
    date_today = date.today()
    yr = date_today.year
    while True:
        try:
            print("Enter the day:")
            day = int(input(''))
            print("Enter the month:")
            month = int(input(''))
            while True:
                try:
                    print("Enter the year:")
                    year = int(input(''))
                    if yr == year:
                        break
                    else:
                        if year < yr:
                            print('Enter the correct year:')
                        elif year > yr:
                            print('You cannot select year other than current one')
                except ValueError:
                    print('Invalid character')
            dt = date(year, month, day)
            break
        except ValueError:
            print('Invalid date. Enter date correctly')
    return dt


def booking(scheme, op):
    scheme.acquire()
    op.set_room_type('room_type')
    op.set_from_date('from_date')
    op.set_days('days')
    op.set_price('price')
    print(op)
    global Single, Double
    if op._room_type == 'Single' and Single > 0:
        Single = Single -1
    elif op._room_type == 'Double' and Double > 0:
        Double = Double -1
    else:
        print('We are sorry, the type of the room you requested is unavailable, please select other types')

    scheme.release()

print("Welcome to hotel Mewah\nHere are the following type of the rooms available:\n")

try:
    roomsdisp = open('rooms.txt', 'r')
except IOError:
    print('Files for reading rooms corrupt or not found')
list = []
for line in roomsdisp:
    rooms = line.strip
    list.append(rooms)
    print(rooms)
roomsdisp.close()

Single = 1
Double = 1
reservation = Stay()
sema = threading.Semaphore(2)
t1 = Thread(target = booking, args = (sema, reservation,))


t1.start()
