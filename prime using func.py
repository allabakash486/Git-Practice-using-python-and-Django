def check(n):
    fa =0
    for lin in range(1,n+1):
        if n%lin==0:
            fa+=1
    if fa==2:
        print('prime')
    else:
        print('not prime')
    return 'None'
(check(19))        
