preanalisis = ''
flag=0
limite_cadena = 0
cadena = ""

def Lista():
    digito()
    Resto_Lista()

def Resto_Lista():
    global preanalisis  # Declaración global
    if preanalisis == '+':
        coincidir('+')
        digito()
        Resto_Lista()
    elif preanalisis == '-':
        coincidir('-')
        digito()
        Resto_Lista()
    else:
        pass

def digito():
    global preanalisis  # Declaración global
    if preanalisis == '0':
        coincidir('0')
    elif preanalisis == '1':
        coincidir('1')
    elif preanalisis == '2':
        coincidir('2')
    elif preanalisis == '3':
        coincidir('3')
    elif preanalisis == '4':
        coincidir('4')
    elif preanalisis == '5':
        coincidir('5')
    elif preanalisis == '6':
        coincidir('6')
    elif preanalisis == '7':
        coincidir('7')
    elif preanalisis == '8':
        coincidir('8')
    elif preanalisis == '9':
        coincidir('9')
    else:
        print("no coincide la cadena")

def coincidir(caracter):
    global preanalisis
    global cadena
    global flag
    global limite_cadena
    flag+=1
    if flag <= limite_cadena:
        print("El caracter", caracter, "es válido")
        preanalisis= cadena[flag]
    else:
        print("El caracter", caracter, "es válido")
        print("la cadena es valida")

    


def main():
    global limite_cadena
    global preanalisis
    global cadena
    cadena = input("Ingresa una cadena: ")
    limite_cadena=len(cadena)-1
    preanalisis = cadena[0]
    Lista()


preanalisis = ''
flag = 0
limite_cadena = 0
cadena = ""  
main()