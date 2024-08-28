var=109
copy=var
ams=0
count=len(str(var))
while var != 0:
    rem = var % 10
    ams = ams + rem**count
    var //= 10
if copy == ams:
    print(f'{copy} is amstrong')
else:
    print(f'{copy} is not amstrong')
var=109
copy=var
disarms=0
count=len(str(var))
while var != 0:
    rem = var % 10
    disarms = disarms + rem**count
    var //= 10
    count -=1
if copy != disarms:
    print(f'{copy} is disarms')
else:
    print(f'{copy} is not disarms')
