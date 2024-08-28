#bank Application only backend code
class Ourbank():
    Branch_name = 'Bengaluru'
    IFSC_Code   = 'OBNO12435'
    Rate_of_Intrest = 7
    def Details(self,Name,Mob,Pan,Bal,Pin):
        self.Name = Name
        self.Mob = Mob
        self.Pan = Pan
        self.Bal = Bal
        self.Pin = Pin
    def Withdraw(self):
        if self.pin == self.Takepin():
            amount = int(input('Enter the withdraw amount:'))
            if amount<= self.Bal:
                self.Bal -= amount
                print(f'Amount is debited Successfully  Availble balanace is{self.Bal}')
            else:
            print('Insuffecient funds')
        else:
            print('Your Entered Wrong Pin')
    def Deposite(self):
        if self.pin == self.Takepin():
            amount = int(input('Enter the deposited amount '))
            self.Bal += amount
            print('Amount is credited successfully ')
            print(f'Available bal is {self.Bal}')
        else:
            print('Your Entered Wrong Pin')
    def Checkbal(self):
        if self.pin == self.Takepin():
            print(f'Available balanace is {self.Bal}')
        else:
            print('Your Entered Wrong Pin')
    @classmethode
    def Change_of_ROI(cls):
        newval = float(input('Enter the New ROI :'))
        Ourbank.Rate_of_Intrest() = newval
    @staticmethode
    def Takepin():
        password = int(input('Enter the pin :'))
        return password
Shaik = Ourbank()
SHAIK = Ourbank()
Shaik.Details('Shaik',90008309502,'DJUPA23BY',12700,1234)
SHAIK.Details('Syed',85529967754,'DJGUA23N',15000,4321)
SHAIK.Withdraw()

    
