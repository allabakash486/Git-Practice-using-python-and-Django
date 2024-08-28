count=0;
num=2
while count!=50:
    for val in range(2,int((num)**(0.5)+1)):
        if num%val==0:
            num +=1
            break
    else:
        print(num,end=' ')
        count +=1
        num +=1
