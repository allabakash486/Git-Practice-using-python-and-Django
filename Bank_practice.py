class Bank():
    Ifsc= 'B1234';
    B_name = 'SOMETHING';
    Rate_of_intrest =  7;
    B_branch_name = 'Bengaluru';
    def __init__(self,name,contact,Adhar,Bal,Pin):
        self.name = name;
        self.contact = contact;
        self.Adhar = Adhar;
        self.Bal = Bal;
        self.Pin = Pin;
    def withdraw(self):
        if self.Pin == self.takepin():
            amount = int(input("Enter the withdraw amount: "))
            if amount <= self.Bal:
                self.Bal -= amount
                print(f'{amount} is debited successfully!! ')
                print(f'Available Balance is {self.Bal}')
            else:
                print('Insufficient funds!!! ')
        else:
            print('You entered Wrong pin!!!')
    def Deposite(self):
        if self.Pin == self.takepin():
            amount = int(input("Enter the withdraw amount: "))
            self.Bal += amount
            print(f'{amount} is Credited successfully!! ')
            print(f'Available Balance is {self.Bal}')
        else:
            print('You entered Wrong pin!!!')
    def Check_Balance(self):
        if self.Pin == self.takepin():
            print(f'Available Balance is {self.Bal}')
        else:
            print('You entered Wrong pin!!!')
    @classmethod
    def Change_Rate_of_intrest(cls):
        new_ROI = float(input('Enter the New Rate of intrest:'));
        Bank.Rate_of_intrest = new_ROI;
    @staticmethod
    def takepin():
        pasword = int(input("Enter the Pin:"))
        return pasword
customer = Bank('Shaik',6300299581,236759679098,13000,1234)
Customer1 = Bank('Shaik',7063002991,236759679097,1299,4321)
Bank.withdraw(customer)
class Version1():
    settings = 'Common for evryone';
    Features = 'same';
    def __init__(self,name,Gender,Contact,Display_picture,Textmessage):
        self.name = name
        self.Gender =Gender;
        self.Contact = Contact;
        self.Display_picture = Display_picture;
        self.Textmessage = Textmessage;
    def V1(self):
        print(f'{self.name} is available ')
        print(f'{self.Gender} is gender ')
        print(f'{self.Contact} is Mobile ')
        print(f'{self.Display_picture} is iamge ')
        print(f'{self.Textmessage} yes ')
class Version2(Version1):
    def __init__(self,Audiocall,Videocall):
        Version1.__init__(self);
        self.Audipcall = Audiocall;
        self.Videocall = Videocall;
    def V2(self):
        Version1.V1(self)
        print(f'{self.Audiocall} is available ')
        print(f'{self.Videocall} is gender ')
        
class Version3(Version2):
    def __init__(self,Status,Block_number):
        Version2.__init__(self)
        self.Status = Status;
        self.Block_number = Block_number;
    def V3(self):
        Version2.V2(self);
        print(f'{self.Contact} is Mobile ')
        print(f'{self.Display_picture} is iamge ')
        
user1 = Version1('Shaik','Male',6300299581,'Display_picture is acceptable','Yes we can textmessages')
user1.V1()


    

    
        
