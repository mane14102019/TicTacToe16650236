import random

def Tablero(tablero):
    print('\n\t    |      |         ')
    print('\t ', tablero[1], '|  ', tablero[2], ' | ', tablero[3])
    print('\t    |      |         ')
    print('\t----------------')
    print('\t    |      |         ')
    print('\t ', tablero[4], '|  ', tablero[5], ' | ', tablero[6])
    print('\t    |      |       ')
    print('\t----------------')
    print('\t    |      |         ')
    print('\t ', tablero[7], '|  ', tablero[8], ' | ', tablero[9])
    print('\t    |      |       \n')

def verificarO(tablero):
    if tablero[1] == tablero[2] == tablero[3] == 'O' or tablero[4] == tablero[5] == tablero[6] == 'O' or tablero[7] == tablero[8] == tablero[9] == 'O':
        return True
    elif tablero[1] == tablero[4] == tablero[7] == 'O' or tablero[2] == tablero[5] == tablero[8] == 'O' or tablero[3] == tablero[6] == tablero[9] == 'O':
        return True
    elif tablero[1] == tablero[5] == tablero[9] == 'O' or tablero[3] == tablero[5] == tablero[7] == 'O':
        return True
    else:
        return False

def verificarX(tablero):
    if tablero[1] == tablero[2] == tablero[3] == 'X' or tablero[4] == tablero[5] == tablero[6] == 'X' or tablero[7] == tablero[8] == tablero[9] == 'X':
        return True
    elif tablero[1] == tablero[4] == tablero[7] == 'X' or tablero[2] == tablero[5] == tablero[8] == 'X' or tablero[3] == tablero[6] == tablero[9] == 'X':
        return True
    elif tablero[1] == tablero[5] == tablero[9] == 'X' or tablero[3] == tablero[5] == tablero[7] == 'X':
        return True
    else:
        return False

def main(tablero):
    bandera = 1
    while bandera:
        primero = random.randint(0, 1)
        contador = 0
        if primero == 0:
            Tablero(tablero)
            print("\t Turno de la maquina")
            n = random.randint(1, 9)
            while tablero[n] != ' ':
                n = random.randint(1, 9)
            tablero[n] = 'O'
            contador = 1
            primero = 1
        while  verificarX(tablero) ==verificarO(tablero) == False and contador < 9:
            primero = primero % 2
            if primero == 0:
                Tablero(tablero)
                print("\t Turno de la maquina")
                n = random.randint(1, 9)
                while tablero[n] != ' ':
                    n = random.randint(1, 9)
                tablero[n] = 'O'
            else:
                Tablero(tablero)
                n = int(input("\t Tu turno -\t"))
                while n not in tablero or tablero[n] != ' ':
                    n = int(input("\n\t Casilla Incorrecta, elige de nuevo -\t"))
                tablero[n] = 'X'
            primero += 1
            contador += 1
        if verificarX(tablero):
            Tablero(tablero)
            print("\n\t Ganaste.")
        elif verificarO(tablero):
            Tablero(tablero)
            
            print("\n\t Ganó la maquina.")
        else:
            Tablero(tablero)
            print("\n\t Empate.")
        while 1:
            print('\n\t 0- Salir \t\t 1- Continuar')
            bandera = int(input('\n\t Elige - \t'))
            if bandera in (0, 1):
                break
            else:
                print('\n\t Opcion Incorrecta, elige de nuevo')
        tablero = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

print('\n\t Juego del gato')
tablero = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
main(tablero)