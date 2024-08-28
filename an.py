'''class Ourbank():
    Branch_name = 'Bengaluru'
    IFSC_Code   = 'OBNO12435'
    Rate_of_Intrest = 7
    def __init__(self,Name,Mob,Pan,Bal,Pin):
        self.Name = Name
        self.Mob = Mob
        self.Pan = Pan
        self.Bal = Bal
        self.Pin = Pin
    def Withdraw(self):
        if self.Pin == self.Takepin():
            amount = int(input('Enter the withdraw amount:'))
            if amount<= self.Bal:
                self.Bal -= amount
                print(f'Amount is debited Successfully  Availble balanace is {self.Bal}')
            else:
                print('Insuffecient funds')
        else:
            print('Your Entered Wrong Pin')
    def Deposite(self):
        if self.Pin == self.Takepin():
            amount = int(input('Enter the deposited amount '))
            self.Bal += amount
            print('Amount is credited successfully ')
            print(f'Available bal is {self.Bal}')
        else:
            print('Your Entered Wrong Pin')
    def Checkbal(self):
        if self.Pin == self.Takepin():
            print(f'Available balanace is {self.Bal}')
        else:
            print('Your Entered Wrong Pin')
    @classmethod
    def Change_of_ROI(cls):
        newval = float(input('Enter the New ROI :'))
        
    @staticmethod
    def Takepin():
        password = int(input('Enter the pin :'))
        return password
Shaik = Ourbank('Syed',85529967754,'DJGUA23N',15000,4321)
SHAIK = Ourbank('Shaik',90008309502,'DJUPA23BY',12700,1234)
Shaik.Withdraw()
class Whatsapp():
    def __init__(self,Name,Text,Dp):
        self.Name = Name
        self.Text = Text
        self.Dp   = Dp
    def details(self):
        print(self.Name,self.Text,self.Dp)
class WhatsappVersion2(Whatsapp):
    def __init__(self,Audiocall,Status,Loc):
        super().__init__(Name,Text,Dp)
        self.Audiocall = Audiocall
        self.Status = Status
        self.Loc = Loc
    def Details(self):
        Whatsapp().details(self)
        print(self.Audiocall,self.Status,self.Loc)
class WhatsappVersion3(WhatsappVersion2):
    def __init__(self,Videocall,Liveloc,Channel):
        super().__init__(Name,Text,Dp,Audiocall,Status,Loc)
        self.Videocall = Videocall
        self.Liveloc = Liveloc
        self.Channel = Channel
    def details(self):
        WhatsappVersion2().details(self)
        print(self.Videocall,self.Liveloc,self.Channel)
User = Whatsapp('Shaik','Given','Yes')
user2 = WhatsappVersion3('Syed','Given','Yes','Yes','Yes','Not Given','Yes','Alowed For once')
user2.details()
def findMax(s):
    res =""
    for val in range(len(s)):
        if s[val]!=s[val+1]:
            res += s[val]
    result= []
    for ind in range(len(res)):
        result.append(res[ind])
    for ind in range(len(result)):
        for ind1 in range(ind+1,len(result+1)):
            if ((ord(result[ind])<(ord(result[ind])))):
                low = ind1
    result[ind],low[ind]=low[ind],result[ind]
    print("".join(result[::-1]))
s="aaayaaa"
findMax(s)
a = int(input("Enter the starting range"))
last = int(input("Enter the ending range"))
b = a+1
next_num = a+b
print(a,end=' ')
print(b,end=' ')
while (next_num<=last):
    print(next_num,end=' ')
    a=b
    b=next_num
    next_num = a+b
row = int(input('Enter the no.of rows'))
col = int(input('Enter the no.of cols'))
print([[(int(input('Enter the values'))) for val2 in range(col)] for val1 in range(row)])
def Fabi(pos,first_value=0,second_value=1):
    if (pos == 1) or (pos == 2):
        return pos-1
    print(first_value,second_value,end=' ')
    for value in range(pos-1):
        third_value = first_value + second_value
        first_value,second_value = second_value,third_value
        if third_value<= pos:
            print(third_value,end=' ')
pos = int(input('Enter the range position:'))
Fabi(pos)
def fabi(pos,st=0,sec=1):
    if (pos==1 or pos==2):
        return pos-1
    print(st,sec,end=' ')
    for val in range(pos-1):
        Third = st+sec
        st,sec = sec,Third
        print(Third,end=' ')
fabi(10)
#Happy Number
num = 19
while num>9:
    Sol = 0;
    while num!=0:
        ld = (num%10)
        Sol += ld**2
        num //= 10
    num = Sol
print('Happy number' if num==1 or num==7 else ' Not Happy number')
def sqr(num,sol=0):
    while num!=0:
        sol += (num%10)**2
        num //=10
    return sol
def Check_Happy(num):
    while num>9:
        num = (sqr(num))
    return  num == 1 or num ==7
print('Happy number' if Check_Happy(17) else 'Not Happy ')
for row in range(23,27):
    for col in range(row):
        if row==23:        
            if (col==3):
                print(chr(68),end=' ')
            elif (col == 9):
                print(chr(74), end = ' ')
            elif (col == 15 ):
                print(chr(80),end =' ')
            elif (col == 21 ):
                print(chr(86),end =' ')
            elif col == 22:
                print()
            else:
                print(' ',end=' ')
        if row == 24:
            if (col==2):
                print(chr(67),end=' ')
            elif (col == 4):
                print(chr(69), end = ' ')
            elif (col == 8):
                print(chr(73),end =' ')
            elif(col == 10):
                print(chr(75),end =' ')
            elif (col == 14):
                print(chr(79), end = ' ')
            elif (col == 16):
                print(chr(81),end =' ')
            elif(col == 20 ):
                print(chr(85),end =' ')
            elif (col == 22):
                print(chr(87),end=' ')
            elif (col==23):
                print()
            else:
                print(' ',end=' ')
        if row == 25:
            if (col==1):
                print(chr(66),end=' ')
            elif (col == 5):
                print(chr(70), end = ' ')
            elif (col == 7):
                print(chr(72),end =' ')
            elif(col == 11):
                print(chr(76),end =' ')
            elif (col == 13):
                print(chr(78), end = ' ')
            elif (col == 17):
                print(chr(82),end =' ')
            elif(col == 19 ):
                print(chr(84),end =' ')
            elif (col == 23):
                print(chr(88),end=' ')
            elif (col==24):
                print()
            else:
                print(' ',end=' ')
        if row==26:        
            if (col==0):
                print(chr(65),end=' ')
            elif (col == 6):
                print(chr(71), end = ' ')
            elif (col == 12 ):
                print(chr(77),end =' ')
            elif (col == 18):
                print(chr(83),end =' ')
            elif col == 24:
                print(chr(89),end=' ')
            elif col == 25:
                print()
            
            else:
                print(' ',end=' ')
count=0;
num=2
while count!=15:
    for val in range(2,int((num)**(0.5)+1)):
        if num%val==0:
            num +=1
            break
    else:
        print(num,end=' ')
        count +=1
def fas(num):
    check = str(num)+str(num*2)+str(num*3)
    for ind in range (1,10):
        if str(ind) not in check:
            print('Not Fascinating number')
            break
    else:
        print("Fascinating Number")
fas(193)
def fas(num,n=1,fa=0):
    check = str(num)+str(num*2)+str(num*3)
    if n==10:
        return False
    if str(n) not in check:
        return False
    return fa+1+fas(num,n+1)
print('fas' if fas(1729)==9 else 'Not')
def sqr(num,sol=0):
    while num!=0:
        sol += (num%10)**2;
        num//=10
    return sol
def happy(num):
    while num>9:
        num = (sqr(num))
    return num==1 or num==7
print(happy(19))
def squre_of_number(num):
    if num!=0:
        return (num%10)**2+squre_of_number(num//10)
    return False
def happy(num):
    if num<=9:
       return num==1 or num==7 
    return happy(squre_of_number(num))
print('Yes' if happy(19) else 'Not')
def Armstrong(num,dup,sol=0):
    count=len(str(num))
    while num!=0:
        sol+=(num%10)**(count)
        num //= 10
    return dup==sol
print('Yes' if Armstrong(153,153) else 'Not')
a = input('Enter the string: ')
def fun1(a):
    space = len(a)*2-1 
    for val in range(1,len(a)+1):
        dummy =0
        for sp in range(space):
            print(' ',end='')
        space -= 2
        for ind in range(val):
            if (len(a)//2 +ind)<len(a):
                print(a[len(a)//2+ind],end='')
            else:
                print(a[dummy],end='')
                dummy +=1
        print()
fun1(a)
#Bouble sorting
list1 = [0,1,1,2,90,7,6,5,4,3]
for val in range(len(list1)-1,0,-1):
    for ind in range(val):
        if list1[ind]>list1[ind+1]:
            list1[ind],list1[ind+1]=list1[ind+1],list1[ind]
print(list1)
#Selection sorting
l=[0,1,1,2,90,7,6,5,4,3]
for val in range(len(l)-1):
    low = val
    for ind in range(val+1,len(l)):
        if l[low]>l[ind]:
            low = ind
    l[low],l[val]=l[val],l[low]
print(l)
# Quick sort
l= [0,1,1,2,90,7,6,5,4,3]
def quick_sort(l):
    if len(l)<=1:
        return l
    pivot = l[0]
    low_list = [l[i] for i in range(1,len(l)) if(pivot>l[i])]
    high_list = [l[i] for i in range(1,len(l)) if(pivot<=l[i])]
    return quick_sort(low_list) + [pivot] + quick_sort(high_list)
print(quick_sort(l))
# Merge Sorting
L= [1,2,3,4,5,66,0,9,8,7,6,5,5,4,3,3,21,1]
def conquere(Mainlist,Leftlist,Rightlist):
    mi,li,ri = 0,0,0
    while (len(Leftlist)>li) and (len(Rightlist)>ri):
        if Leftlist[li]>Rightlist[ri]:
            Mainlist[mi] = Rightlist[ri]
            ri +=1
        else:
            Mainlist[mi] = Leftlist[li]
            li +=1
        mi +=1
    while (len(Leftlist)>li):
        Mainlist[mi] = Leftlist[li]
        mi +=1
        li +=1
    while (len(Rightlist)>ri):
        Mainlist[mi] = Rightlist[ri]
        mi +=1
        ri +=1
def Devide(L):
    if len(L)>1:
        low ,high= L[:len(L)//2],L[len(L)//2:]
        Devide(low)
        Devide(high)
        conquere(L,low,high)
Devide(L)
print(L)'''

        
        
            
        
    















