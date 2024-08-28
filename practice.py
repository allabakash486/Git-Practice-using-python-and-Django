'''#Armstrong using functios
def Armstrong(num,copy,digi,res=0):
    while num!=0:
        res+=(num%10)**digi
        num//=10
    return res==copy
num=153
print('Armstrong' if Armstrong(num,num,len(str(num))) else 'not armstrong')
#disarum using special nnumber
def disarum(num,dup,dig,sol=0):
    while num!=0:
        sol+=(num**(dig))
        num//=10
        dig-=1
    return dup!=sol
num=135
print('Disarum' if disarum(num,num,len(str(num))) else 'not disarum')
#special number using functions
def spe(num,fa=1):
    for val in range(1,num+1):
        fa*=val
    return fa
def rem(num,sum=1):
    while num!=0:
        ld=num%10
        sum +=spe(ld)
        num//=10
    return sum
num= 145
print('Special ' if rem(num) else 'not special')
print()
#happy number using procedural approach
var=19
while var>9:
    sol=0
    while var!=0:
        ld=var%10
        sol+=ld**2
        var//=10
    var=sol
print('Happy number'if var==1 or var==7  else 'Happy number')
#special number
spenum=145
copy,sol=spenum,0
while spenum!=0:
    ld=spenum%10
    fa=1
    for val in range(1,ld+1):
        fa*=val
    sol+=fa
    spenum//=10
print('Special' if copy==sol  else  'Not special') 
def pali(num ,count):
    if num==0:
        return 0
    return (num%10)*(10**(count-1))+pali(num//10,count-1)
num=12
print('palindrome' if num== pali(num,len(str(num))) else 'Not palindrome')
def prime(num,n=1):
    if n==num+1:
        return 0
    return (num%n==0)+prime(num,n+1)
def rev( num, count ):
    if num==0:
        return 0
    return ((num%10)(10*(count -1))+ rev(num,len(str(num))))
num =11
revnum=prime(num)
print("Emirp" if (prime(num)==2 and prime(revnum)==2 and num!=revnum)  else "Not emirp")
#happy number using function
def happy(num):
    while num>9:
        sum=0
        while num!=0:
            sum+=(num%10)**2
            num//=10
        num=sum
    return num==1 or num==7
print(list(filter(happy,range(1,110))))
    
#prime using filter function and range to range number
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
print(list(filter(prime,range(1,100))))
sp=0
st=5
for val in range(5):
    print(" "*sp +"*"*st)
    sp+=1
    st-=1
sp=4-1
st=1
for val in range(4):
    print(' '*sp +'*'*st)
    sp-=1
    st+=2
sp=0
st=7
for val in range(4):
    print(' '*sp+'*'*st)
    sp+=1
    st-=2
sp=3
st=1
for val in range(4):
    print(' '*sp +'*'*st)
    sp-=1
    st+=2
sp=1
st=5
for valin in range(3):
    print(' '*sp +'*'*st)
    sp+=1
    st-=2
sp=0
st=5
for val in range(3):
    print(' '*sp+'*'*st)
    sp+=1
    st-=2
sp=1
st=3
for val1 in range(2):
    print(' '*sp+'*'*st)
    sp-=1
    st+=2
num=1
n=5
st=1
sp=n//2
for val in range(n//2+1):
    print(' '*sp +str(num)*st)
    sp-=1
    num+=1
    st+=2
sp=1
st=n-2
for val1 in range(n//2):
    print(' '*sp+str(num)*st)
    sp+=1
    st-=2
    num+=1
var=5
for row in range(var):
    for line in range(var):
        print('*', end=' ')
    print()
num=5
for val in range(num):
    for line in range(val):
        print('*' ,end=' ')
    print()
for val in range(5,0,-1):
    for line in range(val):
        print('*', end=' ')
    print()
n=5
sp=n-1
st=1
for val in range(1,n+1):
    for sp1 in range(sp):
        print(' ',end='')
    for st1 in range(st):
        print('*',end=' ')
    
    sp-=1
    st+=1
    print()
var=9
for line in range(1,var+1):
    for row in range(line):
        if row==0 or line==var or row==line-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
#output
    

         
lines=9
for line in range(lines,0,-1):
    for row in range(line):
        if line==lines or row==0 or row==line-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
lines=9
spaces=lines-1
for row in range(1,lines+1):
    for sp in range(spaces):
        print(' ',end=' ')
    for st in range(row):
        if st==0 or st==row-1 or row==lines:
            print('*' ,end=' ')
        else:
            print(' ',end=' ')
    print()
    spaces-=1
var=9
space=0
for line in range(var,0,-1):
    for sp in range(space):
        print(' ',end='')
    for st in range(line):
        if st==0 or line==var or st==line-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    space+=1
lines=9
for line in range(lines):
    for row in range(lines):
        if row==line or row+line==lines-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=5
for row in range(var):
    for col in range(var):
        if col==0 or row==0 or row==var-1 or col==var-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=9
for row in range(var):
    for col in range(var):
        if col==0 or row==0 or row==var-1 or col==var-1 or col==row==var//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=5
for row in range(var):
    for col in range(var):
        if col==0 or row==0 or row==var-1 or col==var-1 or col==var//2 or row==var//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
lines=4
space=lines//2 +1
star=1
for row in range(1,lines+1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        if st==0 or  st==star-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    space-=1
    star+=2

def conqure(Mlist,Llist,Rlist):
    mind,lind,rind=0,0,0
    while lind<len(Llist) and rind < len(Rlist):
        if Llist[lind]>Rlist[rind]:
            Mlist[mind]=Rlist[rind]
            rind+=1
        else:
            Mlist[mind]=Llist[lind]
            lind+=1
        mind+=1
    while lind < len(Llist):
        Mlist[mind]=Llist[lind]
        lind+=1
        mind+=1
    while rind <len(Rlist):
        Mlist[mind]=Rlist[rind]
        rind+=1
        mind+=1
        
def devide(L):
    if len(L)>1:
        left=L[:len(L)//2]
        right=L[len(L)//2:]
        devide(left)
        devide(right)
        conqure(L,left,right)
        
L=[1,90,2,88,7,55,66,7]
devide(L)
print(L)

var=10
for row in range(1,var+1):
    for col in range(row):
        if col==0 or col==row-1 or row==var:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=10
for row in range(var,0,-1):
    for col in range(row):
        if col==0 or col==row-1 or row==var:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=10
space=var-1
for row in range(1,var+1):
    for sp in range(space):
        print(' ',end=' ')
    for col in range(row):
        if col==0 or col==row-1 or row==var :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    space-=1
var=10
space=0
for row in range(var,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for col in range(row):
        if col==0 or col==row-1 or row==var:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    space+=1
    print()
var=10
for row in range(var):
    for col in range(var):
        if col==row or col+row==var-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=5
for row in range(var):
    for col in range(var):
        if col==0 or row==0 or row==var-1 or col==var-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=9
for row in range(var):
    for col in range(var):
        if col==0 or row==0 or row==var-1 or col==var-1 or row==col==var//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
var=10
space=var-1
star=1
for row in range(1,var+1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        if st==0 or st==star-1 or star==var*2 -1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
            
    space-=1
    star+=2
    print()
var=10
space=0
star=var*2-1
for row in range(var,0,-1):
    for sp in range(space):
        print(' ',end=' ')
    for st in range(star):
        if st==0 or st==star-1 or star==var*2 -1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
            
    space+=1
    star-=2
    print()
def Even(num):
    if num%2==0:
        return 'Even'
    return 'Odd'
num=10
print(Even(num))
def prime(num):
    for n in range(2,num//2+1):
        if num%n==0:
            return 'Not prime number'
    return 'Prime'
num=3
print(prime(num))
def palindrom(num,copy,sol=0):
    while num!=0:
        sol=sol*10+(num%10)
        num//=10
    return sol==copy
num=11
print('Palindrome' if palindrom(num,num)  else  'Not prime')
    
def rev(num,copy,sol=0):
    while num!=0:
        sol=sol*10+(num%10)
        num//=10
    return sol
def prime(num):
    for n in range(2,num//2+1):
        if num%n==0:
            return False
    return True
num=13
revnum=rev(num,num)
print('Emirp number' if prime(revnum) and prime(num) and num!=revnum  else 'Not Emirp number')
def Fact(num,fact=1):
    for fa in range(1,num+1):
        fact*=fa
    return fact
def Ld(num):
    sum=0
    while num!=0:
        l_dig=num%10
        sum+=Fact(l_dig)
        num//=10
    return sum
def special(num):
    return Ld(num)==num
num=145
print('Special Number' if special(num) else 'Not special number')
def happy(num):
    while num>9:
        sum=0
        while num!=0:
            ld=num%10
            sum+=ld**2
            num//=10
        num=sum
    return num==1 or num==7
num=10
print('Happy number' if happy(num) else 'Not Happy number')
def prime(num):
    for fa in range(2,num//2+1):
        if num%fa==0:
            return False
    return True
def pali(num,copy,sol=0):
    while num!=0:
        ld=num%10
        sol=sol*10+ld
        num//=10
    return sol==copy
num=11
print('Paliprime number' if pali(num,num) and prime(num) else 'Not Paliprime number')
def pronic(num,n=0):
    while n*(n+1)<=num:
        if n*(n+1)==num:
            return True
        n+=1
    return False
num=30
print('Pronic number' if pronic(num) else 'Not Pronic number')
def sunny(num,n=0):
    while n**2<=num+1:
        if n**2==num+1:
            return True
        n+=1
    return False
num=624
print('Sunny number' if sunny(num) else 'Not a sunny number')
def Arm(num,copy,power,sol=0):
    while num!=0:
        sol+=(num%10)**power
        num//=10
    return copy==sol
num=153
power=len(str(num))
print('Armstrong number' if Arm(num,num,power) else 'Not armstrong number')

def Disarum(num,copy,power,sol=0):
    while num!=0:
        sol+=(num%10)**power
        num//=10
        power-=1
    return copy==sol
num=135
power=len(str(num))
print('Disarum number' if Disarum(num,num,power) else 'Not Disraum number')
def conqure(Mlist,Llist,Rlist):
    mind,rind,lind=0,0,0
    while lind<len(Llist) and rind<len(Rlist):
        if Llist[lind]>Rlist[rind]:
            Mlist[mind]=Rlist[rind]
            rind+=1
        else:
            Mlist[mind]=Llist[lind]
            lind+=1
        mind+=1
    while lind<len(Llist):
        Mlist[mind]=Llist[lind]
        mind+=1
        lind+=1
    while rind<len(Rlist):
        Mlist[mind]=Rlist[rind]
        rind+=1
        mind+=1
def divide(L):
    if len(L)>1:
        left=L[:len(L)//2]
        right=L[len(L)//2:]
        divide(left)
        divide(right)
        conqure(L,left,right)
L=[1,23,1,2,3,4,55,6]
divide(L)
print(L)
line =5
star=1
space=line-1
for row in range(line):
    for sp in range(space):
        print(' ',end=' ')
    space-=1
    for col in range(star):
        if col==0 or col==star-1 or star==line*2-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    star+=2
def even(num):
    if num%2==0:
        return True
    return False
num=10
print(f'{num} is Even nuber' if even(num) else 'odd number')
def rev(num,power):
    if num==0:
        return 0
    return (num%10)*10**(power-1) + rev(num//10,power-1)
num=12321
print('palindrome' if rev(num,len(str(num)))==num else 'Not palindrome')
def rev(num,power):
    if num==0:
        return 0
    return (num%10)*10**(power-1) + rev(num//10,power-1)
def prime(num,n=1):
    if n==num+1:
        return False
    return int(num%n==0) + prime(num,n+1)
num=11
print('palindrome' if rev(num,len(str(num)))== num and prime(num)==2 else 'Not palindrome')
def prime(num,n=1,sol=0):
    if n==num+1:
        return False
    return (num%n==0) + prime(num,n+1)
def rev(num,power):
    if num!=0:
        return False
    return (num%10)*10**(power-1) + rev(num//10,power-1)
num=15
revnum=prime(num)
print('Emirp number' if (prime(num)==2) and (num!=revnum) and (prime(revnum)==2) else 'Not Emirp number ')
def sunny(num,n=0):
    if n**2 <=  num+1:
        if n**2==num+1:
            return True
        return sunny(num,n+1)
    return False
num=16
print('Sunny Number' if sunny(num) else 'Not sunny number')
def Pronic(num,n=0):
    if n*(n+1) <=  num:
        if n*(n+1)==num:
            return True
        return Pronic(num,n+1)
    return False
num=12
print('pronic Number' if Pronic(num) else 'Not Pronic number')
def harshad(num):
    if num==0:
        return 0
    return (num%10) + harshad(num//10)
num=12
print('Harshad Number' if num % harshad(num)==0 else 'Not harshad')

def Armstrong(num,power):
    if num==0:
        return 0
    return (num%10)**power + Armstrong(num//10,power)
num=153
print('Armstrong Number' if num == Armstrong(num,len(str(num))) else 'Not Armstrong number')
def Armstrong(num,power):
    if num==0:
        return 0
    return (num%10)**power + Armstrong(num//10,power-1)
num=135
print('Disarum Number' if num == Armstrong(num,len(str(num))) else 'Not Armstrong number')
def sqr(num):
    if num==0:
        return False 
    return (num%10)**2+ sqr(num//10)
def happy(num):
    if num>9:
        return happy(sqr(num))
    return num==1 or num==7
num=19
print('Happy number' if happy(num) else 'Not')
def fact(num):
    if num==0 or num==1:
        return 1
    return  (num)*fact(num-1)
def special(num):
    if num==0:
        return False
    return fact(num%10) +special(num//10)
num=145
print('Special number' if special(num)== num else 'Not Special number')
def fas(num,n=1,fa=0):
    check=str(num)+str(num*2)+str(num*3)
    if n>9:
        return False
    if str(n) in check:
        return (fa+1)+fas(num,n+1)
    return False
num=192
print('Fascinating number' if fas(num)==9 else 'Not Fascinating number')
def sqr(num):
    if num==0:
        return False
    return (num%10)**2+sqr(num//10)
def Happy(num):
    if num>=9:
        return Happy(sqr(num))
    return num==1 or num ==7
num=19
print('Happy number' if Happy(num) else 'Not happy number')
def fact(num,fa=1):
    if fa==num:
        return num
    return (fa)*fact(num,fa+1)
def special(num):
    if num==0:
        return False
    return fact(num%10)+special(num//10)
num=144
print('Special number' if special(num)==num else 'Not Special number')
def Binary(num,power=1):
    if num==0:
        return False
    return (num%2)*power + Binary(num//2,power*10)
num=10
print(Binary(num))
def Integer(num,val=1):
    if num==0:
        return False
    return (num%10)*(val) + Integer(num//10,val*2)
num=1000
print(Integer(num))
print((lambda a,b:a+b)(11,10))
L=[1,2,3,4,5]
print(list(map(lambda a1:a1*a1, L)))
def prime(num,fa=2):
    for line in range(num//2+1):
        if num%fa==0:
            return False
    return num
print(list(map(prime,range(10,21))))
def rev(num,sol=0):
    while num!=0:
        sol=sol*10+(num%10)
        num//=10
    return sol
print(list(map(rev,range(11,21))))
l1=[1,2,3,4,5,6,7,8,9,0]
l2=[10,20,34,50,60,60,70,90,89,0]
res=[]
for ind in range(10):
    res.append(l1[ind]+l2[ind])
print(res)
l1=[11,22,33,44]
l2=[1,2,3,4]
print(list(map(lambda v1,v2:v1+v2,l1,l2)))
print('\n'.join(list(map(lambda a1:'*'*a1,range(4,0,-1)))))
print('\n'.join(list(map(lambda a1,a2: ' '*a1 + '*'*a2,range(1,5),range(1,5)))))

print('Not' if list(filter(lambda num:list(filter(lambda a1:num%a1==0,range(2,num//2+1) ,range(1,10))) else 'Prime')))
def sqr(num,sol=0):
    if num==0:
        return num
    return (num%10)**2+sqr(num//10) 
    
def check(num):
    if num<=9:
        return num
    return check(sqr(num))
    
num=19
print('Happy number' if check(num) ==1 or check(num)==7 else 'not happy number')
def fact(num,fa=1):
    if fa==num:
        return num
    return fa*fact(num,fa+1)
def special(num):
    if num==0:
        return False
    return fact(num%10)+special(num//10)
def check (num):
    return special(num)==num
num=145
print('Special number' if check(num) else 'Not spcial number')
def prime(num,fa=1):
    if fa==num+1:
        return False
    return (num%fa==0) + prime(num,fa+1)
def rev(num,power):
    if num==0:
        return False
    return (num%10)*10**(power-1)+rev(num//10,power-1)
num=13
power=len(str(num))
revnum=rev(num,power)
print('Emirp number' if (prime(num)==2) and (prime(revnum)==2) and (num!=revnum) else 'Not Emirp number')
l=[1,2,3,4,5,63,4,5,6]
low=0
high=len(l)//2-1
user=63
for ind in range(len(l)-1):
    if l[ind]==user:
        print(ind)
        break
else:
    print(-1)
l=[1,2,3,4,5,6,78,90]
low=0
high=len(l)-1
user=5
for ind in range(len(l)-1):
    ind=int(low+((low-high)/(l[low]-l[high]))*(user-l[low]))
    if l[ind]>user:
        high=ind-1
    elif l[ind]<user:
        low=ind+1
    elif l[ind]==user:
        print(ind)
        break
else:
    print(-1)
def quick(var):
    if len(var)<=1:
        return var
    pivot=var[0]
    low=[var[ind] for ind in range(1,len(var)) if pivot>var[ind]]
    high=[var[ind] for ind in range(1,len(var)) if pivot<=var[ind]]
    return quick(low)+[pivot]+quick(high)
var=[-7,5,14,15,1,41,]
print(quick(var))
def quick(var):
    if len(var)<=1:
        return var
    pivot=var[0]
    low=[var[ind] for ind in range(1,len(var)) if pivot>var[ind]]
    high=[var[ind] for ind in range(1,len(var)) if pivot<=var[ind]]
    return quick(low)+[pivot]+quick(high)
var=[1,2,56,1,4,15,1,5]
print(quick(var))
l=[1,2,3,4,6,89]
user=5
low=0
high=len(l)-1
while low<=high:
    mid=(low+high)//2
    if l[mid]>user:
        high=mid-1
    elif l[mid]<user:
        low=mid+1
    elif l[mid]==user:
        print(mid)
        break
else:
    print(-1)
l=[1,2,3,4,6,89]
user=89
low=0
high=len(l)-1
while low<=high and l[low]<=user<l[high]:
    ind=int(low+((low-high)/(l[low]-l[high]))*(user-l[low]))
    if l[ind]>user:
        high=ind-1
    elif l[ind]<user:
        low=ind+1
    elif l[ind]==user:
        print(ind)
        break
else:
    print(-1)
l=[8,-1,4,5]
for ind in range(len(l)):
    for ind2 in range(ind):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
    
print(l)
l=[9,21,1,2,3,4]
for ind in range(len(l)-1):
    lowind=ind
    for ind2 in range(ind,len(l)):
        if l[lowind]>l[ind2]:
            lowind=ind2
    l[ind],l[lowind]=l[lowind],l[ind]
print(l)
l=[9,21,1,2,3,4]
for ind in range(len(l)-1):
    for ind2 in range(ind+1):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)
s='We are Engineers'
alpha_count,Special_count,dig_count=0,0,0
for ind in range(len(s)) :
    
    if ('A'<=s[ind]<='Z') or ('a'<=s[ind]<='z'):
        alpha_count+=1
    elif '0'<=s[ind]<='9':
            dig_count+=1
    else:
        Special_count+=1
    
print(alpha_count,dig_count,Special_count)
def conqure(Mlist,Llist,Rlist):
    mind,lind,rind=0,0,0
    while lind<len(Llist) and rind<len(Rlist):
        if Llist[lind]>Rlist[rind]:
            Mlist[mind]=Rlist[rind]
            rind+=1
        else:
            Mlist[mind]=Llist[lind]
            lind+=1
        mind+=1
    while lind<len(Llist):
        Mlist[mind]=Llist[lind]
        mind+=1
        lind+=1
    while rind<len(Rlist):
        Mlist[mind]=Rlist[rind]
        rind+=1
        mind+=1
        
def devide(L):
    if len(L)>1:
        right,left=L[0:len(L)//2],L[len(L)//2:]
        devide(left)
        devide(right)
        conqure(L,left,right)
L=[2,3,1,3,4,5,6,90]
devide(L)
print(L)
def happy(num):
    while num>9:
        sum=0
        while num!=0:
            sum+=(num%10)**2
            num//=10
        num=sum
    return num==1 or num==7
num=19
print('Happy number' if happy(num) else 'Not')
def sqr(num,sol=0):
    if num==0:
        return False
    return (num%10)**2+sqr(num//10)
def happy(num):
    if num>9:
        return happy(sqr(num))
    return num==1 or num==7
num=12
print('Happy number' if happy(num) else 'Not ')
def special(num,dup,sol=0):
    while num!=0:
        ld=(num%10)
        fa=1
        for ind in range(1,ld+1):
            fa*=ind
        sol+=fa
        num//=10
    return sol==dup
num=145
print('Special number' if special(num,num) else 'Not special number')
def fact(num,fa=1):
    if fa==num:
        return num
    return fa*fact(num,fa+1)
def special(num):
    if num==0:
        return False
    return fact(num%10)+ special(num//10)
num=145
print('Special number' if special(num)== num else 'Not special number')
def prime(num,fa=1):
    if fa==num+1:
        return False
    return (num%fa==0)+prime(num,fa+1)
num=12
print('Prime' if prime(num)==2 else 'Not')'
def emirp(num,copy,sol=0):
    while num!=0:
        sol=(sol*10)+(num%10)
        num//=10
    return sol!=copy       
for val in range(2,copy//2+1):
    if copy%val==0:
        return False
else:
    for val2 in range(2,sol//2+1):
        if sol%val2==0:
            return False
        return True
    else:
        return False
num=13
print('Emirp' if emirp(num,num)  else  'Not')
num=int(input('Enter the input'))
while num!=0:
    ld=num%10
    if num>1:        
        for val in range(2,int((num)**(0.5)+1)):
            if num%val==0:
                print('Not Prime')
                break
        else:
            print('Prime')
    num//=10'''
n='Class'
result=''
for ind in range(len(n)):
    word=""
    for sv in range(ind+1,len(word)+1):
        Word+=n[sv]
    print(word)
    word=''
    


    
    






















        

    
    
        
        





