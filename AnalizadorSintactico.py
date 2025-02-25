preanalisis = ''  # Declaración global

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
    global preanalisis  # Declaración global
    if caracter == preanalisis:
        return True
    else:
        return False

def verificar_cadena(cadena):
    global preanalisis  # Declaración global
    for i in range(len(cadena)):
        preanalisis = cadena[i] 
        Lista()  
        if not coincidir(cadena[i]):
            print ("la cadena no cumple con los procesos")  # Se actualiza solo si la función retorna True
            break  # O podrías usar 'continue' si quieres que solo lo ignore y siga

def main():
    cadena = input("Ingresa una cadena: ")
    verificar_cadena(cadena)

preanalisis = ''  # Inicia la variable global
main()