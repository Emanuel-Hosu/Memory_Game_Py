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
        self.player1Guess = '';
        self.player2Guess = '';
        self.anchoTablero = '';
        self.altoTablero = '';
        self.tableroVacio = True; #este pasas a ser false en paint table al crear el tablero
        self.posicionesAcertadas = [];
        self.scorePlayer1 = 0;
        self.scorePlayer2 = 0;
        self.gameMode = 0

    #Funcion que s encarga de dar el mensaje de bienvenida en un futuro menu() sera el encargado
    def welcome(self):
        print('Memory')
        print("Enter the board size in the format 'width x height'. Example: 5x6")
        print("The maximum allowed size is 5x6")


    #En proceso... creada hoy jeje
    def menu(self):
        user = ""
        if self.tableroVacio == True:
            print("--------------Welcome to Memory--------------")
            print("\n--------------Menu--------------")
            print("\nChoose the game mode")
            print("\n1. Play - Player 1 vs Player 2")
            print("\n2. Play - Player vs Machine")
            print("\n3. Play - Machine 1 vs Machine 2")
            print("\n4. Exit")

    def getMenuChoice(self):
        while True:
            try:
                opcion = int(input("\nSelect a option(1-4): "))
                if 1 <= opcion <= 4:
                    self.gameMode = opcion
                    break
                print("Please, select a valid option (1-4)")
            except ValueError:
                print("Please, input a valid number")

    #FUncion que se encarga de recoger los datos del alumno y crear una lista de emojis randoms usando la funcion radnomEmoji
    #Por ultimo esta función llama a printTable que esta se encargara de crear la tabla con lo necesitado
    def dataTable(self):
        print("===============GAME STARTS===============")
        print("Please, enter the board size in the format 'width x height'. Example: 5x6")
        print("The maximum allowed size is 5x6")
        user = input('')
        parts = user.split('x')
        self.anchoTablero = int(parts[0])
        self.altoTablero = int(parts[1])
        #En caso de que el usuario añada un tamaño de tablero incorrecto
        if (self.anchoTablero * self.altoTablero % 2 != 0):
            while self.anchoTablero * self.altoTablero % 2 != 0:
                print('An issue has occurred, the board size is odd. Please try again.\n')
                print("Enter the board size in the format 'width x height'. Example: 5x6")
                print("The maximum allowed size is 5x6")


                user = input('')
                parts = user.split('x')
                self.anchoTablero = int(parts[0])
                self.altoTablero = int(parts[1])

        nrEmoji = int(self.anchoTablero * self.altoTablero) / 2; #El numero de emoji que vamos a utilizar, por ejemplo si es una tabla 2x2 solo se van a utilizar 2 emojis, cada uno con su pareja
        self.randomEmoji(nrEmoji) #Randomeamos los emojis
        #print(self.emojiMix) #BORRAR EN UN FUTUOR, solo la utilizo para pruebas
        self.start()

       
    #Funcion que se encarga de pintar el tablero, tambien cuadno hay una pareja acertada, que esta se comprueba en el metodo comprobarRespuesta(), 
    #este se encarga de printear las parejas acertadas
    def paintTable(self):
        index = 0

        print("\n")
        for i in range(self.altoTablero):
            for h in range(self.anchoTablero):
                current_index = i * self.altoTablero + h
                if current_index in self.posicionesAcertadas:
                    #Si se encuentra en posicionesAcertadas, este pinta el emoji
                    print(self.emojiMix[current_index][1], end=' ')
                else:
                    #Si no se acierta la respuesta pinta un cuadrado en blanco.
                    print("□ ", end=' ')
                index += 1
            print()
        
        self.tableroVacio = False
            
    def start(self):
        #self.paintTable(self.anchoTablero, self.altoTablero)
        while self.finalizado != True:
            self.paintTable()
            if self.gameMode == 1:
                if (self.player1 == True):
                    #Primera elección
                    print("\n---------Player 1 TURN---------")
                    print('\nPLAYER 1 - 1º GUESS')
                    print("Remember to enter the answer in 'width x height' format. Example 3x3")
                    self.player1Guess = input('')
                    parts = self.player1Guess.split('x')
                    #Restamos menos uno para ajustarlo al "array" de las tablas
                    guess1_x = int(parts[0]) - 1 
                    guess1_y = int(parts[1]) - 1
                    
                    #Posicion ajustada al "array de printTable()
                    guess1_index = guess1_y * self.anchoTablero + guess1_x
                    
                    #Mostramos el tablero con la primera eleccion
                    for i in range(self.altoTablero):
                        for h in range(self.anchoTablero):
                            current_index = i * self.anchoTablero + h
                            if current_index in self.posicionesAcertadas or current_index == guess1_index:
                                print(self.emojiMix[current_index][1], end=' ')
                            else:
                                print("□ ", end=' ')
                        print()

                    #Segunda eleccion
                    print('\nPLAYER 1 - 2º GUESS')
                    print("Remember to enter the answer in 'width x height' format. Example 3x3")
                    self.player1Guess = input('')
                    parts = self.player1Guess.split('x')
                    guess2_x = int(parts[0]) - 1
                    guess2_y = int(parts[1]) - 1
                    
                    guess2_index = guess2_y * self.anchoTablero + guess2_x
                    
                    #Mostramos el tabler con las dos posiciones adivinadas
                    for i in range(self.altoTablero):
                        for h in range(self.anchoTablero):
                            current_index = i * self.anchoTablero + h
                            if current_index in self.posicionesAcertadas or current_index == guess1_index or current_index == guess2_index:
                                print(self.emojiMix[current_index][1], end=' ')
                            else:
                                print("□ ", end=' ')
                        print()
                #Cambio de turno
                elif self.player2 == True:
                    #Primera elección
                    print("\n---------Player 2 TURN---------")
                    print('\nPLAYER 2 - 1º GUESS')
                    print("Remember to enter the answer in 'width x height' format. Example 3x3")
                    self.player2Guess = input('')
                    parts = self.player2Guess.split('x')
                    guess1_x = int(parts[0]) - 1 
                    guess1_y = int(parts[1]) - 1
                    
                    guess1_index = guess1_y * self.anchoTablero + guess1_x
                    
                    #Mostramos el tablero con la primera eleccion
                    for i in range(self.altoTablero):
                        for h in range(self.anchoTablero):
                            current_index = i * self.anchoTablero + h
                            if current_index in self.posicionesAcertadas or current_index == guess1_index:
                                print(self.emojiMix[current_index][1], end=' ')
                            else:
                                print("□ ", end=' ')
                        print()

                    print('\nPLAYER 2 - 2º GUESS')
                    print("Remember to enter the answer in 'width x height' format. Example 3x3")
                    self.player2Guess = input('')
                    parts = self.player2Guess.split('x')
                    guess2_x = int(parts[0]) - 1
                    guess2_y = int(parts[1]) - 1
                    
                    #Posicion ajustada al tablero de printTable()
                    guess2_index = guess2_y * self.anchoTablero + guess2_x
                    
                    #Mostramos el tabler con las dos posiciones adivinadas
                    for i in range(self.altoTablero):
                        for h in range(self.anchoTablero):
                            current_index = i * self.anchoTablero + h
                            if current_index in self.posicionesAcertadas or current_index == guess1_index or current_index == guess2_index:
                                print(self.emojiMix[current_index][1], end=' ')
                            else:
                                print("□ ", end=' ')
                        print()
                #Comprobamos las posiciones, si estas son correctas lo añadimos a un array con las posiciones acertadas, donde en paintTable() se printearan los emojis acertados siempre.
                if self.comprobarRespuesta(self.emojiMix[guess1_index][0], self.emojiMix[guess2_index][0]) == True:
                    self.posicionesAcertadas.append(guess1_index)
                    self.posicionesAcertadas.append(guess2_index)
                    self.paintTable() #Mostrar tablero actualizado con las coincidencias
                    self.isFinished() #Verificamos si el juego ha acabado
        
        #Fin del juego
        self.gameOver();
                
    #Funcion encargada de comporobar las posiciones (parejas del array), si estas son correctas devuelve true (osea no cambia el turno del jugador y sigue jugando el que ha acertado)
    #En caso de fallar, esta funcion se encarga de cambiar el turno y informar de que no hay coincidencia
    def comprobarRespuesta(self, guess1, guess2):
        if guess1 == guess2:
                print("\n*** MATCH FOUND ***")
                #Comprobar el jugador que ha acertado la pareja. Si player 1 es True y ha acertado la secuencia se le sumara un punto
                if self.player1 == True:
                    self.scorePlayer1 += 1;
                elif self.player2 == True:
                    self.scorePlayer2 += 1;
                
                return True;
        elif self.player1 == True:
            print("\n**+ NOT MATCH ***")
            self.player1 = False
            self.player2 = True
            return False;
        elif self.player2 == True:
            print("\n**+ NOT MATCH ***")
            self.player1 = True
            self.player2 = False
            return False;
                
        input("\nPress enter to continue...")
 
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

    #Funcion encargada de saber si el juego ha finalizado o no
    def isFinished(self):
        if len(self.posicionesAcertadas) == len(self.emojiMix):
            self.finalizado = True;

    #Funcion encargada de imprimir el score del juego
    def gameOver(self):
        print("\n\n\n\n\n\n---------Game is over----------\n\nResults are: ")
        print(f"\nPlayer 1: {self.scorePlayer1} pairs right")
        print(f"\nPlayer 2: {self.scorePlayer2} pairs right")
        print("\n----------FINAL SCORE-----------\n")
        if (self.scorePlayer1 > self.scorePlayer2):
            print("Player 1 WINS")
        elif (self.scorePlayer1 < self.scorePlayer2):
            print("Player 2 WINS")
        else: 
            print("DRAW")