def is_pali(num,copy,dsum=0):
    while num!=0:
        ld=num%10
        dsum=dsum*10+ld
        num//=10
    return copy!=dsum
def is_prime(num):
    for val in range(2,num//2+1):
        if num%val==0:
            return False
    return True
num=17
palinum=is_pali(num,num)
print('Emirp number' if is_pali(num,num) and is_prime(num) and (palinum!=num) else 'not Emirp number')
        
