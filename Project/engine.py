# engine.py
import random

class Engine:
    def __init__(self):
        self.emoji = {
            '1': '🍊',
            '2': '🍋',
            '3': '🍈',
            '4': '🍓',
            '5': '🍌',
            '6': '🍍',
            '7': '🫐',
            '8': '🥥',
            '9': '🥝',
            '10': '🍎',
            '11': '🍇',
            '12': '🥭',
            '13': '🥑',
            '14': '🍑',
            '15': '🍏'
        }
        self.emojiMix = []
        self.finalizado = False
        self.player1 = True;
        self.player2 = False;
        self.comporbador = False;
        self.player1Guess = '';
        self.player2Guess = '';
        self.anchoTablero = '';
        self.altoTablero = '';
        self.tableroVacio = True; #este pasas a ser false en paint table al crear el tablero
        #compobador si ha fallado o no el player 1 o 2

    #Funcion que s encarga de dar el mensaje de bienvenida
    def welcome(self):
        print('Memory')
        print("Introduce el tamaño del tablero en el formato 'ancho x alto'. Ejemplo: 5x6")
        print("El tamaño máximo permitido es 5x6")

    #FUncion que se encarga de recoger los datos del alumno y crear una lista de emojis randoms usando la funcion radnomEmoji
    #Por ultimo esta función llama a printTable que esta se encargara de crear la tabla con lo necesitado
    def dataTable(self):
        user = input('')
        parts = user.split('x')
        ancho = int(parts[0])
        alto = int(parts[1])

        if (ancho * alto % 2 != 0):
            while ancho * alto % 2 != 0:
                print('Ha ocurrido un problema, el tablero es impar, vuelve a intentarlo\n')
                print("Introduce el tamaño del tablero en el formato 'ancho x alto'. Ejemplo: 5x6")
                print("El tamaño máximo permitido es 5x6")

                user = input('')
                parts = user.split('x')
                ancho = int(parts[0])
                alto = int(parts[1])

        #Pasamos el numero de emojis que vamos a utilizar
        print("\nQue el juego comience :D")
        nrEmoji = int(ancho * alto) / 2;
        self.randomEmoji(nrEmoji)
        print(self.emojiMix)
        self.paintTable(ancho, alto)
        self.start()


       
    #En un futuro, cuando un usuario acerte mostrara la con todos los valores acertados.
    def paintTable(self, ancho, alto):
        index = 0
        iAltura = 0

        if self.tableroVacio == True:
            self.anchoTablero = ancho;
            self.altoTablero = alto;
            for i in range(alto):
                for h in range(ancho):
                    print("□ ", end=' ')
                    #print(self.emojiMix[index][1], end=' ') 
                    index += 1
                print()
            self.tableroVacio = False;
        #ESTO HAY QUE METERLO EN OTRO LADO
        '''elif self.tableroVacio == False:
            for i in range(self.altoTablero):
                for h in range(self.anchoTablero):
                    current_index = i * self.anchoTablero + h
                    if current_index == ancho or current_index == alto:
                        print(self.emojiMix[current_index][1], end=' ')
                    #print(self.emojiMix[index][1], end=' ') 
                    print("□ ", end=' ')
                    index += 1
                print()'''
            
    def start(self):
        while self.finalizado != True:
            if (self.player1 == True):
                #Primera elección
                print("\nA continuación sera el turno de Player 1")
                print('\nPLAYER 1 - 1º GUESS')
                print("Recuerda introducir la respuesta en formato 'ancho x altura'. Ejemplo 3x3")
                self.player1Guess = input('')
                parts = self.player1Guess.split('x')
                #Restamos menos uno para ajustarlo al array
                guess1_x = int(parts[0]) - 1 
                guess1_y = int(parts[1]) - 1
                
                #Ej. 1x1 lo que hace es, 0 * 5 + 0 = 0
                #Entonces elige la posicion 0 de la "Matriz"
                guess1_index = guess1_y * self.anchoTablero + guess1_x
                
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        if current_index == guess1_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        else:
                            print("□ ", end=' ')
                    print()

                # Segunda elección
                print('\nPLAYER 1 - 2º GUESS')
                print("Recuerda introducir la respuesta en formato 'ancho x altura'. Ejemplo 3x3")
                self.player1Guess = input('')
                parts = self.player1Guess.split('x')
                guess2_x = int(parts[0]) - 1
                guess2_y = int(parts[1]) - 1
                
                # Calculamos el índice de la segunda elección
                guess2_index = guess2_y * self.anchoTablero + guess2_x
                
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        #La comporbacion del guess1 y la comprobacion del guess2
                        if current_index == guess1_index or current_index == guess2_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        else:
                            print("□ ", end=' ')
                    print()

                #comprobar la KEY
                #print(self.emojiMix[guess1_index][0], " Y " ,self.emojiMix[guess2_index][0])
            #Cambio de turno
            elif self.player2 == True:
                #Primera elección
                print("\nA continuación sera el turno de Player 2")
                print('\nPLAYER 2 - 1º GUESS')
                print("Recuerda introducir la respuesta en formato 'ancho x altura'. Ejemplo 3x3")
                self.player1Guess = input('')
                parts = self.player1Guess.split('x')
                #Restamos menos uno para ajustarlo al array
                guess1_x = int(parts[0]) - 1 
                guess1_y = int(parts[1]) - 1
                
                #Ej. 1x1 lo que hace es, 0 * 5 + 0 = 0
                #Entonces elige la posicion 0 de la "Matriz"
                guess1_index = guess1_y * self.anchoTablero + guess1_x
                
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        if current_index == guess1_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        else:
                            print("□ ", end=' ')
                    print()

                # Segunda elección
                print('\nPLAYER 2 - 2º GUESS')
                print("Recuerda introducir la respuesta en formato 'ancho x altura'. Ejemplo 3x3")
                self.player1Guess = input('')
                parts = self.player1Guess.split('x')
                guess2_x = int(parts[0]) - 1
                guess2_y = int(parts[1]) - 1
                
                # Calculamos el índice de la segunda elección
                guess2_index = guess2_y * self.anchoTablero + guess2_x
                
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        #La comporbacion del guess1 y la comprobacion del guess2
                        if current_index == guess1_index or current_index == guess2_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        else:
                            print("□ ", end=' ')
                    print()

                #comprobar la KEY
                #print(self.emojiMix[guess1_index][0], " Y " ,self.emojiMix[guess2_index][0])
                #Si la respuesta es correcta imprimimos la tabla
            if self.comprobarRespuesta(self.emojiMix[guess1_index][0], self.emojiMix[guess2_index][0]) == True:
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        if current_index == guess1_index or current_index == guess2_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        #print(self.emojiMix[index][1], end=' ') 
                        print("□ ", end=' ')
                        index += 1
                    print()
                
    
    def comprobarRespuesta(self, guess1, guess2):
        if guess1 == guess2:
                print("\nCoincidencia encontrada")
                self.comporbador = True;
                return True;
        elif self.player1 == True:
            print("\nNo hay coincidencia")
            self.player1 = False
            self.player2 = True
            return False;
        elif self.player2 == True:
            print("\nNo hay coincidencia")
            self.player1 = True
            self.player2 = False
            return False;
                
        input("\nPresiona Enter para continuar...")
        #Conseguir que imprima el tablero. Esto lo voy a intentar hacer desde la propia clase start :)
 
    #Ggenera un emjoji randome dpendiendo del resultado que ha introducido el usuario / 2 por ejemplo si el tablero es
    #5x6 este es un 30, entonces lo dividimos entre 2 y el resultado es el numero de emojis que vamos a usar. Este
    #ES DIVIDIDO EN EL METODO DATA TABLE.
    def randomEmoji(self, number):
        pair1 = []
        pair2 = []
        # Recogemos el nr max de emojis que vamos a utilizar
        emojisUsados = random.sample(list(self.emoji.items()), k=int(number))
        #
        for valor_aleatorio in emojisUsados:
            pair1.append(valor_aleatorio)
            pair2.append(valor_aleatorio)
        
        pair1.extend(pair2);
        #print(pair1)
        self.emojiMix = random.sample(pair1, k=int(number * 2))