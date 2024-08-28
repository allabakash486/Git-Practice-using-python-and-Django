def fa(num,fa=1):
    for val in range(1,num+1):
        fa*=val
    return fa
def dig(num,sum=0):
    while num!=0:
        ld=(num%10)
        sum+=fa(ld)
        num//=10
    return sum
def spe(num):
    return num==dig(num)
num=145
print('special number' if spe(num) else 'Not special number')
def sq(num,sum=0):
    while num!=0:
        sum+=(num%10)**2
        num//=10
    return sum
def happy(num):
    while num>9:
        num = sq(num)
    return num==1 or num==7
num=6
print('happy number' if happy(num) else 'not happy')
def FN(num):
    for val in range(1,10):
        if str(val) not in check:
            print('Not fascinating number')
            break
    return 'Fascinating number'
num=192
check=str(num)+str(num*2)+str(num*3)
print(FN(num))
def sunny(var,n=0):
    while (n)**2<=var+1:
        if (n)**2==var+1:
            return True
            break
        n+=1
    return False
var=24
print('Sunny' if sunny(var) else 'Not sunny')
def pronic(var,n=0):
    while (n)*(n+1)<=var:
        if (n)*(n+1)==var:
            return True
            break
        n+=1
    return False
var=30
print('Pronic' if pronic(var) else 'Not Pronic')
def pali(num,copy,sol=0):
    while num!=0:
        sol=(sol*10)+(num%10)
        num//=10
    return sol!=copy
def prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
    return True
num=13
revnum=prime(num)
print('Emirp number' if prime(num) and pali(num,num) and num!=revnum else 'Not Emirp number')
def pali(num,copy,sol=0):
    while num!=0:
        sol=(sol*10)+(num%10)
        num//=10
    return sol==copy
def prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
    return True
num=11
print('paliprime' if prime(num) and pali(num,num) else 'not Paliprime')

def prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
    return True
num=11
print('Prime' if prime(num) else 'not prime')
def fac(num,fa=1):
    for val in range(1,num+1):
        fa*=val
    return fa
num=5
print(f'factorial of {num} ={fac(num)}')
def Arm(num,dup,power,sol=0):
    while num!=0:
        ld=num%10
        sol+=(ld)**(power)
        num //= 10
    return sol == dup
num=153
power=len(str(num))
print('Armstrong number'  if Arm(num,num,power) else  'Not Armstrong')
def DisArm(num,dup,power,sol=0):
    while num!=0:
        ld=num%10
        sol+=(ld)**(power)
        power -= 1
        num //= 10
    return sol == dup
num=135
power=len(str(num))
print('Disarum number'  if DisArm(num,num,power) else  'Not Disarum')

        
    

    
        
