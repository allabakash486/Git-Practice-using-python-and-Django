var=17
copy=var
res=0
while var!=0:
    ld=var%10
    res=res*10+ld
    var//=10
if res!=copy:
    for num in range(2,copy//2+1):
        if copy%num==0:
            print('not Emirp number')
            break
    else:
        for num2 in range(2,res//2+1):
            if res%num2==0:
                print('Not Emirp number')
        else:
            print('Emirp nummber')
else:
    print('not emirp number')

#special
integer=40585
copy=integer
sol=0
while integer!=0:
    ld=integer%10
    fact=1
    integer//=10
    for num in range(1,ld+1):
        fact*=num
    sol+=fact 
print('Special number' if copy==sol else 'not special number')
#Happy number
num=19
while num>9:
    sum=0
    while num!=0:
        ld=num%10
        sum+=ld**2
        num//=10
    num=sum
print('happy number' if num==1 or num==7 else 'Not happy number')
#sunny number
num=15
n=0
while n*n<=num+1:
    if n*n==num+1:
        print('Sunny number')
        break
    n+=1
else:
    print('not Sunny number')
#Fascinating number
num=192
var=str(num)+str(num*2)+str(num*3)
for val in range(1,10):
    if str(val) not in var:
        print('Not Fascinating number')
        break
else:
    print('Fascinating number')
#pronic number
num=12
n=0
while (n)*(n+1)<=num:
    if (n)*(n+1)==num:
        print('pronic number')
        break
    n+=1
else:
    print('Not pronic number')
num=156
copy=num
sol=0
while num!=0:
    ld=num%10
    sol+=ld
    num//=10
print('Harshad number' if copy%sol==0 else 'Not harshad number')

num=153
sol=0
copy=num
power=len(str(num))
while num!=0:
    ld=num%10
    sol+=(ld)**power
    num//=10
print('Armstrong number' if copy==sol else 'Not Armstrong')
num=135
sol=0
copy=num
power=len(str(num))
while num!=0:
    ld=num%10
    sol+=(ld)**power
    power-=1
    num//=10
print('Disarum number' if copy==sol else 'Not Disarum')
num=11
copy,sol=num,0
while num !=0:
    sol=(sol*10)+(num%10)
    num//=10
if sol==copy:
    for dig in range(2,copy//2+1):
        if copy%dig==0:
            print('Not paliprime')
            break
    else:
        print('paliprime')

num=5
fa=1
for val in range(1,num+1):
    fa*=val
print(f'factorial of {num} = {fa}')
num=145
sol,copy=0,num
while num!=0:
    ld=num%10
    num//=10
    sum=1
    for val in range(1,ld+1):
        sum*=val
    sol+=sum
print('Special number' if sol==copy else 'Not special number')
var=10
if var%2==0:
    print('Even number')
else:
    print('odd')

    






















    
    
        
    
        
