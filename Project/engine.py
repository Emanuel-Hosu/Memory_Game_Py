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
        self.posicionesAcertadas = [];
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
        self.paintTable(ancho, alto)#hay que quitar esto
        self.start()


       
    #En un futuro, cuando un usuario acerte mostrara la con todos los valores acertados.
    def paintTable(self, ancho, alto):
        index = 0
        if self.tableroVacio == True:
            self.anchoTablero = ancho
            self.altoTablero = alto
        
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        for i in range(alto):
            for h in range(ancho):
                current_index = i * self.altoTablero + h
                if current_index in self.posicionesAcertadas:
                    # Si la posición ya ha sido acertada, muestra el emoji
                    print(self.emojiMix[current_index][1], end=' ')
                else:
                    # Si no ha sido acertada, muestra el cuadrado
                    print("□ ", end=' ')
                index += 1
            print()
        
        self.tableroVacio = False
            
    def start(self):
        self.paintTable(self.anchoTablero, self.altoTablero)
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
                
                guess1_index = guess1_y * self.anchoTablero + guess1_x
                
                # Mostrar tablero con la primera elección
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        if current_index in self.posicionesAcertadas or current_index == guess1_index:
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
                
                guess2_index = guess2_y * self.anchoTablero + guess2_x
                
                # Mostrar tablero con ambas elecciones
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        if current_index in self.posicionesAcertadas or current_index == guess1_index or current_index == guess2_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        else:
                            print("□ ", end=' ')
                    print()

            elif self.player2 == True:
                #Primera elección
                print("\nA continuación sera el turno de Player 2")
                print('\nPLAYER 2 - 1º GUESS')
                print("Recuerda introducir la respuesta en formato 'ancho x altura'. Ejemplo 3x3")
                self.player2Guess = input('')  # Corregido: era player1Guess
                parts = self.player2Guess.split('x')
                guess1_x = int(parts[0]) - 1 
                guess1_y = int(parts[1]) - 1
                
                guess1_index = guess1_y * self.anchoTablero + guess1_x
                
                # Mostrar tablero con la primera elección
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        if current_index in self.posicionesAcertadas or current_index == guess1_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        else:
                            print("□ ", end=' ')
                    print()

                # Segunda elección
                print('\nPLAYER 2 - 2º GUESS')
                print("Recuerda introducir la respuesta en formato 'ancho x altura'. Ejemplo 3x3")
                self.player2Guess = input('')  # Corregido: era player1Guess
                parts = self.player2Guess.split('x')
                guess2_x = int(parts[0]) - 1
                guess2_y = int(parts[1]) - 1
                
                guess2_index = guess2_y * self.anchoTablero + guess2_x
                
                # Mostrar tablero con ambas elecciones
                for i in range(self.altoTablero):
                    for h in range(self.anchoTablero):
                        current_index = i * self.anchoTablero + h
                        if current_index in self.posicionesAcertadas or current_index == guess1_index or current_index == guess2_index:
                            print(self.emojiMix[current_index][1], end=' ')
                        else:
                            print("□ ", end=' ')
                    print()

            if self.comprobarRespuesta(self.emojiMix[guess1_index][0], self.emojiMix[guess2_index][0]) == True:
                self.posicionesAcertadas.append(guess1_index)
                self.posicionesAcertadas.append(guess2_index)
                self.paintTable(self.anchoTablero, self.altoTablero)  # Mostrar tablero actualizado con las coincidencias
                self.isFinished()#Veridicamos si el juego ha acabado
        
        #Cuando se sale del whiel(osea el juego ha acabado)
        print("Game is over.\nResults are: ") #En un futuro, siempre que un jugador acierte agregaremos un punto por cada acertado para 
        #print("Player1: 2 pairs right")
        #print("Player2: 2 pairs right")
        #print("Draw")
                
    
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

    def isFinished(self):
        if len(self.posicionesAcertadas) == len(self.emojiMix):
            self.finalizado = True;