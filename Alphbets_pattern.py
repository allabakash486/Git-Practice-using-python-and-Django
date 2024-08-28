for row in range(0,5):
        if row==0:
            dummy=68;
            for val in range(4):
                if val==0:
                    print(' '*4+chr(dummy),end=' ')
                    dummy +=6;
                else:
                    if val!=3:
                        print(' '*5+chr(dummy),end=' ')
                        dummy +=6;
                    else:
                        print(' '*4+chr(dummy))

        elif row == 1:
            dumm = 67;
            for val in range(8):
                if (val%2==0):
                    if val==0:
                        print(" "*2+chr(dumm),end=' ')
                    else:
                        print(chr(dumm),end=' ')
                elif (val%2 !=0):
                    if val ==7:
                        print(chr(dumm))
                    else:
                        dumm+=2
                        print(' '*1,chr(dumm),end="  ")
                        dumm +=4
        elif row==4:
            dummy=65;
            for val in range(5):
                if val ==0:
                    print(chr(dummy),end=' ');
                    dummy +=6;
                else:
                    print(' '*5,chr(dummy),end=' ');
                    dummy +=6;
            '''elif (col == 4):
                print(chr(69), end = ' ')
            elif (col == 8):
                print(chr(73),end =' ')
            elif(col == 10):
                print(chr(75),end =' ')
            elif (col == 14):
                print(chr(79), end = ' ')
            elif (col == 16):
                print(chr(81),end =' ')
            elif(col == 20 ):
                print(chr(85),end =' ')
            elif (col == 22):
                print(chr(87),end=' ')
            elif (col==23):
                print()
            else:
                print(' ',end=' ')
        if row == 25:
            if (col==1):
                print(chr(66),end=' ')
            elif (col == 5):
                print(chr(70), end = ' ')
            elif (col == 7):
                print(chr(72),end =' ')
            elif(col == 11):
                print(chr(76),end =' ')
            elif (col == 13):
                print(chr(78), end = ' ')
            elif (col == 17):
                print(chr(82),end =' ')
            elif(col == 19 ):
                print(chr(84),end =' ')
            elif (col == 23):
                print(chr(88),end=' ')
            elif (col==24):
                print()
            else:
                print(' ',end=' ')
        if row==26:        
            if (col==0):
                print(chr(65),end=' ')
            elif (col == 6):
                print(chr(71), end = ' ')
            elif (col == 12 ):
                print(chr(77),end =' ')
            elif (col == 18):
                print(chr(83),end =' ')
            elif col == 24:
                print(chr(89),end=' ')
            elif col == 25:
                print()
            
            else:
                print(' ',end=' ')'''
