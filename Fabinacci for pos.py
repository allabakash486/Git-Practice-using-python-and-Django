def Fabi(pos,First = 0,Second = 1):
    if (pos==1 or pos == 2):
        return (pos - 1)
    else:
        for val in range(pos-2):
            Third = (First + Second)
            First,Second = Second , Third
        return Third
print(Fabi(3))
def Fab(pos):
    if pos == 1 or pos == 2:
        return pos - 1
    return Fab(pos-1)+Fab(pos-2)
print(Fab(10))