def happy(num):
    while num>9:
        sum=0
        while num!=0:
            sum+=(num%10)**2
            num//=10
        num=sum
    return num==1 or num==7
print(list(filter(happy,range(1,101))))

            
