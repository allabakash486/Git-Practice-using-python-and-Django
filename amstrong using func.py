def is_Armstrong(num,dup,ndig,sol=0):
    while num!=0:
        ld =num%10
        sol+=(ld)**ndig
        num //=10
    return sol==dup
num=153
print('armstrong' if(num,num,len(str(num))) else 'not Armstrong')

print()

def is_Disarum(var,dup,ndigi,sol=0):
    while var!=0:
        ld = var%10
        sol += (ld)**ndigi
        ndigi -= 1
        var //= 10
    return sol==dup
var=135
print('disarum' if is_Disarum(var,var,len(str(var))) else 'not disarum')
