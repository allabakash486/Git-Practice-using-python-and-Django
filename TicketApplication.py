maxNumber_of_ticktes = 150
def booking(arg):
    l = []
    def inner():
        if len(l) == 0:
            l.append(arg())
            return l[0]
    return inner
@booking
class Kalki_movei():
    def Book(self,Request_no_of_tickets):
        if(Request_no_of_tickets<=150):
            num = 150 
            print(f'{Request_no_of_tickets} is successfully booked for Kalki Movei....!!!!!!!')
            num -= Request_no_of_tickets
            print(f'Available tickets are {num-Request_no_of_tickets}')
        else:
            print('Ticktes are not available')
@booking
class Rayan_movei():
    def __init__(self):
        maxNumber_of_tickets = 100
    def Book(self,Request_no_of_tickets):
        if(Request_no_of_tickets<=maxNumber_of_tickets):
            print(f'{Request_no_of_tickets} is successfully booked for Rayan Movei....!!!!!!!')
            maxNumber_of_tickets -= Request_no_of_tickets
            print(f'Available tickets are {maxNumber_of_tickets}')
        else:
            print('Ticktes are not available')
class GooglePay():
    print('1) Kalki /n 2) Rayan ')
    Movei_number  = int(input('Enter the number:'))
    if (Movei_number==1):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Kalki_movei()
        obj.Book(Number_of_tickets)
    if (Movei_number==2):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Rayan_movei()
        obj.Book(Number_of_tickets)
class Phonepay():
    print('1) Kalki /n 2) Rayan ')
    Movei_number  = int(input('Enter the number:'))
    if (Movei_number==1):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Kalki_movei()
        obj.Book(Number_of_tickets)
    if (Movei_number==2):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Rayan_movei()
        obj.Book(Number_of_tickets)
class Paytm():
    print('1) Kalki /n 2) Rayan ')
    Movei_number  = int(input('Enter the number:'))
    if (Movei_number==1):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Kalki_movei()
        obj.Book(Number_of_tickets)
    if (Movei_number==2):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Rayan_movei()
        obj.Book(Number_of_tickets)
class Book_My_show():
    print('1) Kalki /n 2) Rayan ')
    Movei_number  = int(input('Enter the number:'))
    if (Movei_number==1):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Kalki_movei()
        obj.Book(Number_of_tickets)
    if (Movei_number==2):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Rayan_movei()
        obj.Book(Number_of_tickets)
class Amazonepay():
    print('1) Kalki /n 2) Rayan ')
    Movei_number  = int(input('Enter the number:'))
    if (Movei_number==1):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Kalki_movei()
        obj.Book(Number_of_tickets)
    if (Movei_number==2):
        Number_of_tickets = int(input("Enter the number of ticktes:"))
        obj = Rayan_movei()
        obj.Book(Number_of_tickets)
GooglePay()
Phonepay()
Paytm()
Book_My_show()



