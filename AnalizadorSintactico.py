def Lista():
    digito()
    Resto_Lista()

def Resto_Lista():
    if preanilisis == '+':
        coincidir('+')
        digito()
        Resto_Lista()
    elif preanilisis == '-':
        coincidir('-')
        digito()
        Resto_Lista()
    else:
        pass

def digito():
    if preanilisis == '0':
        coincidir('0')
    elif preanilisis == '1':
        coincidir('1')
    elif preanilisis == '2':
        coincidir('2')
    elif preanilisis == '3':
        coincidir('3')
    elif preanilisis == '4':
        coincidir('4')
    elif preanilisis == '5':
        coincidir('5')
    elif preanilisis == '6':
        coincidir('6')
    elif preanilisis == '7':
        coincidir('7')
    elif preanilisis == '8':
        coincidir('8')
    elif preanilisis == '9':
        coincidir('9')
    else:
        print("no coincide la cadena")