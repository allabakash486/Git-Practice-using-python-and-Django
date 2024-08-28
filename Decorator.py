def Outermethod(argument):
    def Inner():
        argument()
        print('Inner function is exeuted')
    return Inner
@Outermethod
def Name():
    print("Hello python")
Name()