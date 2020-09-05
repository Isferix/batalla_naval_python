'''
Batalla Naval en Python [Python]
Proyecto Integrador
---------------------------
Autor: Ishef Glatzel
Version: 2.0
 
Descripcion:
Programa creado para practicar los conocimientos adquiridos a lo largo del curso
'''

__author__ = "Ishef Glatzel"
__email__ = "ishefglatzel@outlook.com"
__version__ = "2.0"

# Librerias
from random import randint
import os, os.path
import errno
import numpy as np

clear = lambda: os.system('cls')

class jugador():
    def __init__(self):
        '''
        Funcion constructora del objeto jugador:
        - Setea un tablero base por defecto en forma de array
        - Setea un diccionario con la traduccion de las ubicaciones en notacion a coordenadas
        - Setea el estado inicial del tablero a iniciar
        - Genera una lista 'flota' donde se almacenaran la ubicacion de los barcos
        - Inicializa la variable name que almacenara el nombre del jugador
        - Inicializa la variable tablero para almacenar en texto el tablero
        - Inicializa la variable humano para indicar que clase de jugador es
        '''
        self.tablero = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ])
        self.flota = []
        self.estado = 'iniciar'
        self.diccionario_casillas = {'A1': (0,0), 'A2': (0,1), 'A3': (0,2), 'A4': (0,3), 'A5': (0,4), 'A6': (0,5), 'A7': (0,6), 'A8': (0,7), 'A9': (0,8), 'A10': (0,9),
                        'B1': (1,0), 'B2': (1,1), 'B3': (1,2), 'B4': (1,3), 'B5': (1,4), 'B6': (1,5), 'B7': (1,6), 'B8': (1,7), 'B9': (1,8), 'B10': (1,9),
                        'C1': (2,0), 'C2': (2,1), 'C3': (2,2), 'C4': (2,3), 'C5': (2,4), 'C6': (2,5), 'C7': (2,6), 'C8': (2,7), 'C9': (2,8), 'C10': (2,9),
                        'D1': (3,0), 'D2': (3,1), 'D3': (3,2), 'D4': (3,3), 'D5': (3,4), 'D6': (3,5), 'D7': (3,6), 'D8': (3,7), 'D9': (3,8), 'D10': (3,9),
                        'E1': (4,0), 'E2': (4,1), 'E3': (4,2), 'E4': (4,3), 'E5': (4,4), 'E6': (4,5), 'E7': (4,6), 'E8': (4,7), 'E9': (4,8), 'E10': (4,9),
                        'F1': (5,0), 'F2': (5,1), 'F3': (5,2), 'F4': (5,3), 'F5': (5,4), 'F6': (5,5), 'F7': (5,6), 'F8': (5,7), 'F9': (5,8), 'F10': (5,9),
                        'G1': (6,0), 'G2': (6,1), 'G3': (6,2), 'G4': (6,3), 'G5': (6,4), 'G6': (6,5), 'G7': (6,6), 'G8': (6,7), 'G9': (6,8), 'G10': (6,9),
                        'H1': (7,0), 'H2': (7,1), 'H3': (7,2), 'H4': (7,3), 'H5': (7,4), 'H6': (7,5), 'H7': (7,6), 'H8': (7,7), 'H9': (7,8), 'H10': (7,9),
                        'I1': (8,0), 'I2': (8,1), 'I3': (8,2), 'I4': (8,3), 'I5': (8,4), 'I6': (8,5), 'I7': (8,6), 'I8': (8,7), 'I9': (8,8), 'I10': (8,9),
                        'J1': (9,0), 'J2': (9,1), 'J3': (9,2), 'J4': (9,3), 'J5': (9,4), 'J6': (9,5), 'J7': (9,6), 'J8': (9,7), 'J9': (9,8), 'J10': (9,9)}               
        self.nombre = None
        self.tablero_texto = ''
        self.humano = None


    def imprimir_tablero(self):
        '''
        Funcion que imprime por consola el tablero y guarda el tablero en texto en la variable self.tablero_texto
        
        NOTA: El 'estado' del tablero define como se imprimiran las casillas en pantalla 
        0: Neutro
        1: Agua
        2: Fuego
        3: Barco
        '''
        def imprimir():
            """
            Funcion que se encarga de imprimir el tablero en consola
            """
            def decorador(fila, buscado, reemplazado):
                print
                for dato in range(len(buscado)):
                    fila = fila.replace(buscado[dato], reemplazado[dato])
                return fila
            
            
            tablero_texto = self.tablero_texto.split('\n')
            tablero_texto.pop(0) # Se elimina el encabezado
            tablero_texto.pop(0) # Se elimina la linea punteada
            # Se eliminan los 'enters' del final
            tablero_texto.pop()  
            tablero_texto.pop()
            tablero_texto.pop()
    
            omitir_numeracion = lambda fila: fila[4::] if fila[3]=='|' else fila[3::]
            if self.estado == 'iniciar':
                if self.humano:
                    print('    A B C D E F G H I J\n  ---------------------')
                    for i, fila in enumerate(tablero_texto): 
                        #El decorador solo reemplaza 0s para poner huecos vacios
                        fila = decorador(omitir_numeracion(fila), ['0',], ['-',])
                        if i == 10:
                            break
                        else:
                            if i+1 != 10:
                                print(f' {i+1}|', fila, sep='')
                            else:
                                print(f'{i+1}|', fila, sep='')
                        
            elif self.estado == 'jugar':
                print('    A B C D E F G H I J\n  ---------------------')
                for i, fila in enumerate(tablero_texto): 
                # El decorador oculta las partes de los barcos y el 
                # fuego lo escribe como una X
                    fila = decorador(omitir_numeracion(fila), ['2', '3'], ['X', '0'])
                    if i == 10:
                        break
                    else:
                        if i+1 != 10:
                            print(f' {i+1}|', fila, sep='')
                        else:
                            print(f'{i+1}|', fila, sep='')
        
        self.tablero_texto = '      A B C D E F G H I J\n    -----------------------\n'

        contador = 1
        for columna in self.tablero:
            if contador == 10:
                self.tablero_texto += f'{contador}|'
            else:
                self.tablero_texto += f'  {contador}|'
                contador += 1
                
            for i, fila in enumerate(columna):

                if i != 9:
                    self.tablero_texto += f' {fila}'
                else:   
                    self.tablero_texto += f' {fila}\n'


        self.tablero_texto += '\n\n'

        imprimir()


    def notacion_a_casilla(self, notacion):
        '''
        Funcion que se encarga de traducir una ubicacion escrita como notacion algebraica a indices para que interprete el sistema

        @param notacion: String de 2 caracteres, 1 letra y 1 numero, que es traducido

        NOTA: En caso de no encontrarse dicha ubicacion en el diccionario, se retornara None
        
        '''
        return self.diccionario_casillas.get(notacion)


    def construir_flota(self, lista=[4,3,3,3,2,2,2,1,1]):
        """
        Funcion que se encarga de construir la flota, esta compuesta de muchas funciones
        @param lista: Lista con los barcos que constara el jugador y que tiene que configurar
        """

        def generar_datos():
            """Genera coordenadas aleatorias"""
            diccionario_fila = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                                7: '7', 8: '8', 9: '9', 10: '10'} 
            diccionario_columna = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
                                7: 'G', 8: 'H', 9: 'I', 10: 'J'}

            diccionario_direccion = {1: 'UP', 2: 'DOWN', 3: 'RIGHT', 4: 'LEFT'}
        
            fila = diccionario_fila.get(randint(1,10))
            columna = diccionario_columna.get(randint(1,10))
            ubicacion = columna+fila
            direccion = diccionario_direccion.get(randint(1,4))

            return ubicacion, direccion


        def confirmar_barco(item, comprobacion):
            """Se asegura de que los barcos esten en coordenadas correctas y posibles"""
            def confirmar_validez_coordenadas():
                if (0 <= item[0] < 10) and (0 <= item[1] < 10):
                    return True
                else:
                    return False


            def confirmar_cercania():
                #Desarrollo en curso....
                pass


            def confirmar_unidad():
                for barco in self.flota:
                    for coordenada in barco:
                        if item == coordenada:
                            return False
                return True


            if comprobacion == 'coordenadas':
                confirmacion = confirmar_validez_coordenadas()
            elif comprobacion == 'cercania':
                confirmacion = confirmar_cercania()
            elif comprobacion == 'unico':
                confirmacion = confirmar_unidad()
            
            return confirmacion    

        
        def construir_barco(self, barco, largo):
            """Funcion mas importante que se encarga de armar y compilar el barco"""

            def comprobacion_errores():
                if ubicacion == None:
                    print('La ubicacion introducida es invalida')

                if direccion == None:
                    print('La direccion introducida es invalida')

                if ubicacion == None or direccion == None:
                    return None

                return True           


            def obtener_direcion():
                direccion = input('Introduzca la direccion: UP | DOWN | LEFT | RIGHT\n')

                if direccion == 'UP' or direccion == 'DOWN' or direccion == 'LEFT' or direccion == 'RIGHT':
                    return direccion
                else:
                    return None


            def armar_barco(ubicacion, direccion):
                """Funcion critica del programa, el barco es creado y compilado"""
                barco = []
                def compilar_barco(ubicacion, direccion):
                    """
                    Segun las especificaciones del jugador (@param ubicacion, @param direcion)\n
                    el programa infiere la evolucion de su posicion y genera las coordenadas que ocuparan
                    """

                    if direccion == 'UP':
                        mod = 'y'
                        compilar = lambda: coordenada_y -1

                    elif direccion == 'DOWN':
                        mod = 'y'
                        compilar = lambda: coordenada_y +1

                    elif direccion == 'LEFT':
                        mod = 'x'
                        compilar = lambda: coordenada_x -1

                    elif direccion == 'RIGHT':
                        mod = 'x'
                        compilar = lambda: coordenada_x +1
                        
                    
                    coordenada_x = ubicacion[0]
                    coordenada_y = ubicacion[1]
                    for i in range(largo):
                        barco.append([coordenada_x, coordenada_y])
                        if mod == 'x':
                            coordenada_x = compilar()
                        elif mod == 'y':
                            coordenada_y = compilar()
                        
                        
                    return barco

                if largo != 1:
                    barco = compilar_barco(ubicacion, direccion)
                else:
                    barco = [[ubicacion[0], ubicacion[1]]]
                

                for coordenada in barco:
                    if confirmar_barco(coordenada, 'coordenadas') is False:
                        if self.humano:
                            print('El barco introducido supera los limites del tablero, por favor intente de nuevo')
                        return construir_barco(self, barco, largo)
                    if confirmar_barco(coordenada, 'unico') is False:
                        if self.humano:
                            print('El barco introducido contacta con partes de otros barcos, por favor intente de nuevo')
                        return construir_barco(self, barco, largo)
                return barco 


            if self.humano:
                self.imprimir_tablero()
                ubicacion = self.notacion_a_casilla(input('Introduzca la ubicacion del barco de longitud {}: \n'.format(largo)))
                if largo != 1:
                    direccion = obtener_direcion()
                else:
                    direccion = False

                if comprobacion_errores() == None:
                    input('Por favor, ingrese de vuelta la ubicacion y direccion\nPresione Enter para continuar...')
                    clear()
                    return construir_barco(self, barco, largo)

                barco = armar_barco(ubicacion, direccion)
            else:
                self.imprimir_tablero()
                ubicacion, direccion = generar_datos()
                barco = armar_barco(self.notacion_a_casilla(ubicacion), direccion)

            return barco
        

        def dibujar_barco(barco):
            """Escribe el barco en el tablero y limpia la consola"""
            for coordenada in barco:
                self.tablero[coordenada[1], coordenada[0]] = 3
            if self.humano:
                clear()

        #Flujo de la funcion 
        # - Se crea una lista para almacenar el barco
        # - Se crea el barco
        # - Se guarda en la flota
        # - Se escribe en el tablero
        for i in lista:
            barco = []
            barco = construir_barco(self, barco, i)
            self.flota.append(barco)
            dibujar_barco(barco)
     

    def disparar(self, jugador, jugada):
        """
        Fucnion que se encarga de disparar al rival

        @param jugador: Jugador al que se dispara
        @param jugda: Lista que indica el numero de jugada y el jugador que la efectua
        @param humano: Indica si el jugador que dispara es humano o no
        """

        def grabar_jugada():
            """Graba la jugada en el `archivo .txt` dentro de la carpeta partidas"""
            with open(f"{nueva_carpeta}/Partida_{partida}.txt", "a") as fi:
                if jugada[1] == 0:
                    fi.write('{}. {} '.format(jugada[0], ubicacion))
                if jugada[1] == 1:
                    fi.write('{}\n'.format(ubicacion))


        def disparo(blanco):
            """
            Funcion encargada de efectuar el disparo sobre el tablero y actualizar la flota
            @param blanco: Ubicacion del disparo
            """
            def actualizar_flota():
                barco_hallado = [barco for barco in jugador.flota if list(blanco) in barco]
                index = jugador.flota.index(barco_hallado[0])
                jugador.flota[index].remove(list(blanco))
                if len(jugador.flota[index]) == 0:
                    jugador.flota.remove(barco_hallado[0])
                    print('Hundido!')
                else:
                    print('Fuego!')

            objetivo = jugador.tablero[blanco[1]][blanco[0]]
            
            clear()
            if objetivo == 0:
                jugador.tablero[blanco[1]][blanco[0]] = 1
                print('Agua :(')
            elif objetivo == 3:
                jugador.tablero[blanco[1]][blanco[0]] = 2
                actualizar_flota()


        if self.humano:
            ubicacion = (input('Introduzca su disparo: '))
            blanco = jugador.notacion_a_casilla(ubicacion)

            if blanco == None:
                print("La ubicacion introducida no es valida o ya ha sido usada")
                return self.disparar(jugador, jugada, humano)

        else:

            diccionario_fila = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                                7: '7', 8: '8', 9: '9', 10: '10'} 
            diccionario_columna = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F',
                                7: 'G', 8: 'H', 9: 'I', 10: 'J'}
            fila = diccionario_fila.get(randint(1,10))
            columna = diccionario_columna.get(randint(1,10))
            ubicacion = columna+fila

            blanco = jugador.notacion_a_casilla(ubicacion)

            if blanco == None:
                return self.disparar(jugador, jugada)

        if blanco == None:
            print("La ubicacion introducida no es valida o ya ha sido usada")
            return self.disparar(jugador, jugada)
        else:
            jugador.diccionario_casillas.pop(ubicacion)
            disparo(blanco)
            grabar_jugada()
        


def armar_juego():
    """Funcion que controla el flujo inicial del programa definiendo los jugadores sus nombres y sus flotas"""

    def modalidad():
        modo = input(
            "Introduzca CPU para jugar contra la maquina o 1v1 para jugar de a 2 jugadores:\n")
        if modo == 'CPU' or modo == '1v1':
            return modo
        return modalidad()


    def configurar_partido(modalidad):
        """
        Se encarga de `configurar el partido` segun la modalidad especificada\n
        @param modalidad: modalidad, puede ser `CPU` o `1v1`"""
        

        def configurar_jugador(jugador, tipo, nombre):
            if tipo == 'humano':
                jugador.humano = False
                jugador.construir_flota()
                jugador.nombre = nombre
            else:
                jugador.humano = False
                jugador.construir_flota()
                jugador.nombre = nombre


        if modalidad == "CPU":

            print('La modalidad seleccionada es CPU... Corriendo programa...')

            nombre_1 = input("Introduzca su nombre:\n")

            print('Es momento de que configure su flota')
            configurar_jugador(jugador_1, 'humano', nombre_1)
            
            print('Ahora la computadora configurara su flota...')
            configurar_jugador(jugador_2, 'CPU', 'Bot')

        elif modalidad == "1v1":

            print('La modalidad seleccionada es 1v1... Corriendo programa...')

            nombre_1 = input("Introduzca su nombre:\n")

            print(f'Es momento de que {nombre_1} configure su flota')
            configurar_jugador(jugador_1, 'humano', nombre_1)

            nombre_2 = input("Introduzca su nombre:\n")

            print(f'Es momento de que {nombre_2} configure su flota')
            configurar_jugador(jugador_2, 'humano', nombre_2)


    def grabar_flota(jugador_1=jugador_1, jugador_2=jugador_2):
        """Funcion encargada de crear el archivo.txt de las partidas y guardar las flotas de los jugadores"""
        with open(f"{nueva_carpeta}/Partida_{partida}.txt", "w") as fi:
            fi.seek(0)
            fi.write(f'Jugador 1: {jugador_1.nombre}\n\n')
            fi.write(jugador_1.tablero_texto)

            fi.write(f'Jugador 2: {jugador_2.nombre}\n\n')
            fi.write(jugador_2.tablero_texto)

            fi.write('\n')


    modalidad = modalidad()
    configurar_partido(modalidad)
    grabar_flota()


def jugar():
    """Funcion que controla el flujo principal del programa manejando los turnos de cada uno de los jugadores hasta
    que el jugo finaliza"""

    def comprobar_finalizacion(turno):
        """Funcion encarga de comprobar si el juego continua
        @param turno: Segun el turno se infiere el ganador si es que el juego termino"""
        if turno == 0:
            if len(jugador_2.flota) == 0:
                return finalizar(jugador_1)
        if turno == 1:
            if len(jugador_1.flota) == 0:
                return finalizar(jugador_2)
    
    jugada = 0
    while True:
        jugada += 1

        print(f"Turno de {jugador_1.nombre}")
        jugador_2.imprimir_tablero()
        jugador_1.disparar(jugador_2, [jugada, 0])
        jugador_2.imprimir_tablero()
        comprobar_finalizacion(0)
        input('Presione Enter para continuar...')
        clear()

        print(f"Turno de {jugador_2.nombre}")
        jugador_1.imprimir_tablero()
        jugador_2.disparar(jugador_1, [jugada, 1])
        jugador_1.imprimir_tablero()
        comprobar_finalizacion(1)
        input('Presione Enter para continuar...')
        clear()


def finalizar(ganador):
    """
    Funcion que anuncia el ganador en pantalla y anota el resultado en el archivo.txt de la partida
    """
    print(f'{ganador.nombre} ha sido el ganador')
    with open(f"{nueva_carpeta}/Partida_{partida}.txt", "a") as fi:
        if ganador == jugador_1:
            fi.write('\n' + '1-0')
        elif ganador == jugador_2:

            fi.write('\n' + '0-1')
    quit()


if __name__ == '__main__':
    print("Iniciando Juego...")

    #Se establece la direccion desde donde se ejecuta el programa
    direccion = (os.path.dirname(os.path.abspath(__file__)))

    #Se intenta crear la carpeta partidas en caso de no existir
    nueva_carpeta = (direccion + '\Partidas')
    try:
        os.mkdir(nueva_carpeta)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    #Conteo de cuantas partidas ya han sido jugadas
    partida = len([name for name in os.listdir(nueva_carpeta)]) 
    
    #Se define el PRINCIPIO DEL JUEGO
    jugador_1 = jugador()
    jugador_2 = jugador()
    armar_juego()

    print("Hora de jugar!")
    jugador_1.estado = 'jugar'
    jugador_2.estado = 'jugar'
    jugar()