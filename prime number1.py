var =10
factors =0
if var >=2:
    for fa in range(1,var+1):
        if var%fa==0:
            factors +=1
    print()
    if factors ==2:
        print(f'{var} is prime ')
    else:
        print(f'{var} not prime')
else:
    print(f'{var} not prime')
