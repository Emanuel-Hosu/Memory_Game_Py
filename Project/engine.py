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
        self.emojisAcertado = [];

    #En proceso... creada hoy jeje
    def menu(self):
        user = ""
        if self.tableroVacio == True:
            print("========----Welcome to Memory========----")
            print("\n========----Menu========----")
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
        print("\n===============GAME STARTS===============")
        print("============PLAYER VS PLAYER============")
        print("\nPlease, enter the board size in the format 'width x height'. Example: 5x6")
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
        self.random_emoji(nrEmoji) #Randomeamos los emojis
        #print(self.emojiMix) #BORRAR EN UN FUTUOR, solo la utilizo para pruebas
        self.start()

       
    #Funcion que se encarga de pintar el tablero, tambien cuadno hay una pareja acertada, que esta se comprueba en el metodo find_out_response(), 
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
        while not self.finalizado:
            #PLAYER VS PLAYER
            if self.gameMode == 1:
                if self.player1:
                    current_player = "Player 1"
                elif self.player2:
                    current_player = "Player 2"
                
                print(f"\n========{current_player} TURN========")
                self.paintTable()

                # Obtener primer guess
                guess1_index = self.get_valid_guess(current_player, 1)

                # Mostrar tablero con el primer guess
                self.show_guess(guess1_index)

                # Obtener segundo guess
                while True:
                    guess2_index = self.get_valid_guess(current_player, 2)
                    if guess2_index == guess1_index:
                        print("Cannot select the same position twice, please choose again.")
                    else:
                        break

                # Mostrar tablero con ambos guesses
                self.show_guess(guess1_index, guess2_index)

                # Comprobar si los emojis coinciden
                if self.find_out_response(self.emojiMix[guess1_index][0], self.emojiMix[guess2_index][0]):
                    self.posicionesAcertadas.extend([guess1_index, guess2_index])
                    self.paintTable()
                    self.is_finished()
                else:
                    #Cambio de turno si find_out_response() retorna false
                    if self.player1:
                        self.player1 = False
                        self.player2 = True
                    else:
                        self.player2 = False
                        self.player1 = True;
            #PLAYER VS MACHINE EASY
            elif self.gameMode == 2:
                if self.player1:
                    current_player = "Player 1"
                elif self.player2:
                    current_player = "Machine"
                
                print(f"\n========{current_player} TURN========")
                self.paintTable()

                if self.player1:
                    guess1_index = self.get_valid_guess(current_player, 1)

                    self.show_guess(guess1_index)

                    #Entramos en bucle hasta que el player 2 ponga una posicion válida
                    while True:
                        guess2_index = self.get_valid_guess(current_player, 2)
                        if guess2_index == guess1_index:
                            print("Cannot select the same position twice, please choose again.")
                        else:
                            break
                    self.show_guess(guess1_index, guess2_index)
                #EMI TE HAS QUEDADO AQUI
                #Turno de Machine
                else:
                    #Ajustarlo al guess, como si fuera un 2x2 pues pasa a ser 3
                    while True:
                        print(f'\n========Machine - 1º GUESS========\n')
                        guess1_index = random.randint(0, self.altoTablero * self.anchoTablero - 1)
                        print(f"\nGuess 1 selected: {guess2_index}\n")
                        if guess1_index not in self.posicionesAcertadas:
                            print("Cannot select the same position twice, please choose again.")
                        else:
                            break
                    
                    self.show_guess(guess1_index)

                    while True:
                        print(f'\n========Machine - 2º GUESS========\n')
                        guess2_index = random.randint(0, self.altoTablero * self.anchoTablero - 1)
                        print(f"\nGuess 2 selected: {guess2_index}\n")
                        if guess2_index == guess1_index and guess2_index not in self.posicionesAcertadas:
                            print("Cannot select the same position twice, please choose again.")
                        else:
                            break

                    self.show_guess(guess1_index, guess2_index)

                #Comprobamos las posiciones, si estas son correctas las añadimos a posicionesAcertadas []
                if self.find_out_response(self.emojiMix[guess1_index][0], self.emojiMix[guess2_index][0]):
                    self.posicionesAcertadas.extend([guess1_index, guess2_index])
                    self.paintTable()
                    self.is_finished()
                else:
                    #Cambio de turno si find_out_response() retorna false
                    if self.player1:
                        self.player1 = False
                        self.player2 = True
                    else:
                        self.player2 = False
                        self.player1 = True;
        #Fin del juego si is_finished() da true
        self.gameOver()

    def get_valid_guess(self, player, guess_num):
        while True:
            print(f'\n========{player} - {guess_num}º GUESS========\n')
            print("Enter the answer in 'width x height' format (e.g., 3x3):")
            user_input = input('')

            #Validamos el formato correcto (tiene una 'x' y es de dos partes)
            if 'x' not in user_input:
                print("\nInvalid format. Please use 'width x height' (e.g., 3x3).")
                continue

            parts = user_input.split('x')
            if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                print("\nInvalid format. Please use 'width x height' (e.g., 3x3).")
                continue
            
            #Restamos menos uno para ajustarlo al "array" de las tablas
            x = int(parts[0]) - 1
            y = int(parts[1]) - 1
            index = y * self.anchoTablero + x

            #Nos aseguramos de que la posicion puesta por el usuario no se sale del array.
            if x < 0 or x >= self.anchoTablero or y < 0 or y >= self.altoTablero:
                print("\nPosition out of bounds. Choose a position within the board size.")
                continue

            #Si lo que inserta el jugador ya se ha puesto anteriormente, este este le dice que esta incorrecto
            if index in self.posicionesAcertadas:
                print("\nPosition already guessed, please choose a different one.")
            else:
                return index


    def show_guess(self, *indices):
        for i in range(self.altoTablero):
            for h in range(self.anchoTablero):
                current_index = i * self.anchoTablero + h
                if current_index in self.posicionesAcertadas or current_index in indices:
                    print(self.emojiMix[current_index][1], end=' ')
                else:
                    print("□ ", end=' ')
            print()

                
    #Funcion encargada de comporobar las posiciones (parejas del array), si estas son correctas devuelve true (osea no cambia el turno del jugador y sigue jugando el que ha acertado)
    #En caso de fallar, esta funcion se encarga de cambiar el turno y informar de que no hay coincidencia
    def find_out_response(self, guess1, guess2):
        #print(f"Guess 1: {guess1}\nGuess 2: {guess2}\nPosiciones acertadas: {self.posicionesAcertadas}")
        if guess1 == guess2 and guess1 not in self.emojisAcertado and guess2 not in self.emojisAcertado:
            print("\n*** MATCH FOUND ***")
            # Comprobar el jugador que ha acertado la pareja. Si player 1 es True y ha acertado la secuencia se le sumara un punto
            self.emojisAcertado.append(guess1);
            if self.player1:
                self.scorePlayer1 += 1
            elif self.player2:
                self.scorePlayer2 += 1
            return True
        elif self.player1:
            print("\n**+ NOT MATCH ***")
            return False
        elif self.player2:
            print("\n**+ NOT MATCH ***")
            return False
 
    #Ggenera un emjoji randome dpendiendo del resultado que ha introducido el usuario / 2 por ejemplo si el tablero es
    #5x6 este es un 30, entonces lo dividimos entre 2 y el resultado es el numero de emojis que vamos a usar. Este
    #ES DIVIDIDO EN EL METODO DATA TABLE.
    def random_emoji(self, number):
        pair1 = []
        pair2 = []
        #Recogemos el nr max de emojis que vamos a utilizar
        emojisUsados = random.sample(list(self.emoji.items()), k=int(number))
        
        for valor_aleatorio in emojisUsados:
            pair1.append(valor_aleatorio)
            pair2.append(valor_aleatorio)
        
        pair1.extend(pair2);
        #print(pair1)
        self.emojiMix = random.sample(pair1, k=int(number * 2))

    #Funcion encargada de saber si el juego ha finalizado o no
    def is_finished(self):
        if len(self.posicionesAcertadas) == len(self.emojiMix):
            self.finalizado = True;

    #Funcion encargada de imprimir el score del juego
    def gameOver(self):
        print("\n\n\n\n\n\n========Game is over========\n\nResults are: ")
        print(f"\nPlayer 1: {self.scorePlayer1} pairs right")
        print(f"\nPlayer 2: {self.scorePlayer2} pairs right")
        print("\n========FINAL SCORE========-\n")
        if (self.scorePlayer1 > self.scorePlayer2):
            print("Player 1 WINS")
        elif (self.scorePlayer1 < self.scorePlayer2):
            print("Player 2 WINS")
        else: 
            print("DRAW")