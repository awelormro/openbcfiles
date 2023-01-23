def abisiesto(a):
    if a%4==0:
        if a%100==0:
            print('año bisiesto')
        else:
            print('año no bisiesto')
    elif a%4==0 and a%100!=0:
        print('año bisiesto')
    else:
        print('año no bisiesto')

abisiesto(2000)
abisiesto(1995)
abisiesto(1700)
abisiesto(2024)

