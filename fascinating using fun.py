def is_fasi(num):
    cheack=str(num)+str(num*2)+str(num*3)
    for val  in range(1,10):
        if str(val) not in cheack :
            return False
    return True
num=192
print('fascinating' if is_fasi(num) else 'not fascinating ')
