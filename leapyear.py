#leap year
def Is_leapyear(num):
    if ((num%4==0 and num%100 != 0) or (num%400 == 0)):
        return(f"{num} is leap year")
    else:
        return(f"{num} is not leap year")
num = int(input("Enter the year : "))
print(Is_leapyear(num))
print('-'*20)
#leap year with how many days in months based on year which is leap year .
def Is_leapyear(num,var):
    if ((num%4==0 and num%100 != 0) or (num%400 == 0)):
        print(f"{num} is leap year")
        if (var%2 == 0):
            if (var == 2):
                return("29 days")
            else:
                return("30 days")
        else:
            return("31 days")
    else:
        print(f"{num}Not a leap year")
        if (var%2 == 0):
            if (var == 2):
                return("28 days")
            else:
                return("30 days")
        else:
            return("31 days")
num = int(input("Enter the year value"))
var = int(input("Enter the month in decimal"))
print(Is_leapyear(num,var))
        
