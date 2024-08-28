'''class parent():
    variable  = 100
    variable1 = 200
    variable3 = 300
    def method(self):
        print('Methode is excuted in parent class')
class child(parent):
    var=200
    def methode2(self):
        print('Methode1 is executed in the child class')
        super().method()
object1 = parent()
object2 = child()
object2.methode2()'''
class State_bank_of_India():
    branch_name = 'Madanapalle'
    IFSC = 'SBINO123423'
    No_of_branches = 200
    Rate_of_Intrest = 5
    def __init__(self,name,mob,pan,pin,bal):
        self.Name = name
        self.Mob  = mob
        self.Pan  = pan
        self.pin  = pin
        self.Bal  = bal
    def withdraw(self):
        if self.pin ==self.takepin():
            amount = int(input('Enter the withdraw amount'))
            if amount<=self.bal:
                self.bal -= amount
                print('Amount is withdraw succuessfully.....')
                print(f'Available bal is {self.bal}')
            else:
                print('Insuffcient balance')
        else:
            print('Invalid pin')
    def deposite(self):
        if self.pin ==self.takepin():
            amount = int(input('Enter the deposit amount'))
            self.bal += amount
            print(f'Available bal is {self.bal}')
        else:
            print('Invalid pin')
    def checkbal(self):
        if self.pin ==self.takepin():
            print(f'Available bal is {self.bal}')
        else:
            print('Invalid pin')    
    def change_ROI(slef):
        new_Rate_of_intrest   = float(input('Enter the new rate of intrest'))
        obj.Rate_of_Intrest = new_Rate_of_intrest
    @staticmethod
    def takepin():
        password = int(input('Enter the pin'))
        return passwaord
obj = State_bank_of_India('A',123098765,'DJUPA234',1234,5000)
obj.checkbal()
    
    
        
        
    
