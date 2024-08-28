var =145
copy =var
ans =0
while var!=0:
    ld=var%10
    fa =1
    for num in range(1,ld+1):
        fa*=num
    ans+=fa
    var//=10
if ans==copy:
    print('special number')
else:
    print('not special number')
