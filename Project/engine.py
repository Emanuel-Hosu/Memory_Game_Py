# engine.py
import random

"""La clase Engine es el núcleo del juego de memoria en el que dos jugadores o máquinas intentan encontrar pares de emojis ocultos en un tablero. A continuación, se explica el propósito y 
    funcionamiento de cada método y atributo importante en esta clase."""
class Engine:
    def __init__(self):
        self.emoji = {
            '1': '🍊',
            '2': '🍋',
            '3': '🍈',
            '4': '🍓',
            '5': '🍌',
            '6': '🍍',
            '7': '🍒',
            '8': '🥥',
            '9': '🥝',
            '10': '🍉',
            '11': '🍇',
            '12': '🥭',
            '13': '🥑',
            '14': '🍑',
            '15': '🍏'
        }
        self.emojiMix = [] #Array encargado de generar las parejas de emoji, tambien los guardad e forma random.
        self.finalizado = False
        self.player1 = True; #Variable booleana que se encarga de ir cambiando, en caso de que sea Ture, es el turno del player que tenga la variable true
        self.player2 = False; #Lo mismo que el comentario de arriba
        self.anchoTablero = 0;
        self.altoTablero = 0;
        self.tableroVacio = True; #este pasas a ser false en paint table al crear el tablero
        self.posicionesAcertadas = []; #Array que guarda las posiciones acertadas 
        self.scorePlayer1 = 0;
        self.scorePlayer2 = 0;
        self.gameMode = 0
        self.emojisAcertado = []; #Array que guarda los emojis acertados
        self.machineDifficult = 0; 
        self.machineMemory = []; #Array que dependiendo el modo de la maquina guarda una copia de el self.emojiMix en caso de que sea self.gameMode 3 y en caso de que sea el 2, tiene una memoria volátil que cuando esta maquina acierta y hay un MATCH, esta borra la memoria
        self.machineGuess = False; #True en caso de que la maquina vaya a hacer el guess 2, y False en caso de que la maquina vaya a hacer el guess 1

    """Funcion encargada de enseñar el menu pirncipal"""
    def menu(self):
        user = ""
        if self.tableroVacio == True:
            print("========Welcome to Memory========")
            print("\n===========Menu===========")
            print("\nChoose the game mode")
            print("\n1. Play - Player 1 vs Player 2")
            print("\n2. Play - Player vs Machine")
            print("\n3. Play - Machine 1 vs Machine 2")
            print("\n4. Exit")

    """Funcion encargada de enseñar el menu de dificultad en caso de que en el menu principal se haya elegido: Player vs Machine"""
    def difficulty_menu(self):
        user = ""
        if self.tableroVacio == True:
            print("\n=======Difficulty Menu===========")
            print("\nChoose machine difficulty")
            print("\n1. Easy")
            print("\n2. Medium")
            print("\n3. Hard")
            print("\n4. Exit")

    """Menu encargado de recoger los datos y evitar el fallo de la funcion del menu principal"""
    def get_menu_choice(self):
        while True:
            opcion = int(input("\nSelect a option(1-4): "))
            if 1 <= opcion <= 4:
                self.gameMode = opcion
                break
            else:
                print("Please, select a valid option (1-4)")

    """Menu encargado de recoger los datos y evitar el fallo de la funcion de difficulty_menu()"""
    def get_machine_difficulty(self):
        while True:
            opcion = int(input("\nSelect a option(1-3): "))
            if 1 <= opcion <= 3:
                self.machineDifficult = opcion
                break
            else:
                print("Please, select a valid option (1-3)")

    """
    Start()
    Controla el flujo principal del juego, incluyendo los turnos y las interacciones 
    de los jugadores o máquinas, dependiendo del modo de juego seleccionado.
    """
    def start(self):
        while not self.finalizado:
            #PLAYER VS PLAYER
            if self.gameMode == 1:
                if self.player1:
                    current_player = "Player 1"
                elif self.player2:
                    current_player = "Player 2"
                
                print(f"\n========{current_player} TURN========")
                self.paint_table()

                # Obtener primer guess
                guess1_index = self.get_valid_guess(current_player, 1)

                # Mostrar tablero con el primer guess
                self.show_guess([guess1_index])

                # Obtener segundo guess
                while True:
                    guess2_index = self.get_valid_guess(current_player, 2)
                    if guess2_index == guess1_index:
                        print("Cannot select the same position twice, please choose again.")
                    else:
                        break

                # Mostrar tablero con ambos guesses
                self.show_guess([guess1_index, guess2_index])
            #PLAYER VS MACHINE EASY
            elif self.gameMode == 2:
                if self.machineDifficult == 0:
                    self.difficulty_menu()
                    self.get_machine_difficulty()
                if self.player1:
                    current_player = "Player 1"
                elif self.player2:
                    if self.machineDifficult == 1:
                        current_player = "Machine"
                    elif self.machineDifficult == 2:
                        #En get_valid_guest() programamos la inteligencia de las maquinas
                        current_player = "Inteligent Machine"
                    else:
                        current_player = "Super Inteligen Machine"
                
                print(f"\n========{current_player} TURN========")
                self.paint_table()

                if self.player1:
                    guess1_index = self.get_valid_guess(current_player, 1)

                    self.show_guess([guess1_index])

                    #Entramos en bucle hasta que el player 2 ponga una posicion válida
                    while True:
                        guess2_index = self.get_valid_guess(current_player, 2)
                        if guess2_index == guess1_index:
                            print("Cannot select the same position twice, please choose again.")
                        else:
                            break
                    self.show_guess([guess1_index, guess2_index])
                #Turno de Machine
                else:
                    #Ajustarlo al guess, como si fuera un 2x2 pues pasa a ser 3
                    while True:
                        guess1_index = self.get_valid_guess(current_player, 1)

                        #Si el guess1 de la maquina no esta en posiciones acertadas, entonces salimos del while y pintamos la seleccin correcta
                        if guess1_index not in self.posicionesAcertadas or self.gameMode == 3: #Pasamos de todo si la maquina es super inteligente
                            break
                        else:
                            print("Cannot select the same position twice, please choose again.")
                    
                    self.show_guess([guess1_index])
                    print(f"\n{current_player} has select: {self.emojiMix[guess1_index][1]}")

                    while True:
                        #Se le pasa por parametro el pklayer y su turno para que el metodo get_valid_guess se encargue decidir si el random esta bien hecho :)
                        guess2_index = self.get_valid_guess(current_player, 2)
                        #print(f"\nGuess 2 selected: {guess2_index}\n")

                        #Si el guess2 de la maquina no esta en posiciones acertadas, entonces salimos del while y pintamos la seleccin correcta y adenas si no es igual a la guess1
                        if guess1_index == guess2_index:
                            print("Cannot select the same position twice, please choose again.")
                        else:
                            break
            
                    self.show_guess([guess1_index, guess2_index])
                    print(f"\n{current_player} has select the pairs: {self.emojiMix[guess1_index][1]} and {self.emojiMix[guess2_index][1]}")
            #MACHINE VS MACHINE
            elif self.gameMode == 3:
                if self.player1:
                    current_player = "Machine 1"
                elif self.player2:
                    current_player = "Machine 2"

                print(f"\n========{current_player} TURN========")
                self.paint_table()

                while True:
                    guess1_index = self.get_valid_guess(current_player, 1)

                    #Si el guess1 de la maquina no esta en posiciones acertadas, entonces salimos del while y pintamos la seleccin correcta
                    if guess1_index not in self.posicionesAcertadas:
                        break
                    else:
                        print("Cannot select the same position twice, please choose again.")
                    
                self.show_guess([guess1_index])
                print(f"\n{current_player} has select: {self.emojiMix[guess1_index][1]}")

                while True:
                    #Se le pasa por parametro el pklayer y su turno para que el metodo get_valid_guess se encargue decidir si el random esta bien hecho :)
                    guess2_index = self.get_valid_guess(current_player, 2)
                    #print(f"\nGuess 2 selected: {guess2_index}\n")

                    #Si el guess2 de la maquina no esta en posiciones acertadas, entonces salimos del while y pintamos la seleccin correcta y adenas si no es igual a la guess1
                    if guess1_index == guess2_index:
                        print("Cannot select the same position twice, please choose again.")
                    else:
                        break
        
                self.show_guess([guess1_index, guess2_index])
                print(f"\n{current_player} has select the pairs: {self.emojiMix[guess1_index][1]} and {self.emojiMix[guess2_index][1]}")

            #Comprobamos las posiciones, si estas son correctas las añadimos a posicionesAcertadas []
            if self.find_out_response(self.emojiMix[guess1_index][0], self.emojiMix[guess2_index][0]):
                self.posicionesAcertadas.extend([guess1_index, guess2_index])
                self.paint_table()
                self.is_finished()
            else:
                #Cambio de turno si find_out_response() retorna false
                if self.player1:
                    self.player1 = False
                    self.player2 = True
                else:
                    #print("Guess 1 index: ", guess1_index, "\nGuess 2 index: ", guess2_index)
                    self.player2 = False
                    self.player1 = True;

        #Fin del juego si is_finished() da true
        if self.finalizado:
            if self.gameMode == 1:
                player_names = ["Player 1", "Player 2"]
            elif self.gameMode == 2:
                player_names = ["Player 1", "Machine"]
            elif self.gameMode == 3:
                player_names = ["Machine 1", "Machine 2"]
            else:
                player_names = ["Player 1", "Player 2"]

        self.game_over(player_names)
    """get_valid_guess()
    Funcion encargada de obtener y validar las posiciones de los jugadores y máquinas, dependiendo del modo de juego seleccionado.
    """
    def get_valid_guess(self, player, guess_num):
        while True:
            print(f'\n========{player} - {guess_num}º GUESS========\n')
            #En caso de que sea un Player
            if player[0] == "P":
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
            #En caso de que el guess sea una Machine
            else:
                #index ajustado a que no se salga del array, por ejemplo si el tablero es un 2x2 esto es = 4 - 1, osea la maquina solo puede elegir numeros de 0 a 3, para que no se salga del array
                if self.machineDifficult == 1 or player[0] == "M": #En caso de que la maquina sea "tonta"
                    index = random.randint(0, self.altoTablero * self.anchoTablero - 1);
                
                if self.machineDifficult == 2: #En caso de que la maquina sea inteligente (al final de este metodo se contruye la inteligencia de la maquina)
                    encontrado = False;
                    index = 0
                    if len(self.machineMemory) >= 3:
                        value = 0
                        negativeValue = -1;
                        mitad = len(self.machineMemory) // 2
                        while encontrado == False:
                            while value < mitad:
                                #print(f"280 Valor positivo: {self.emojiMix[self.machineMemory[value]][0]}")
                                #print(f"280 Valor negativo: {self.emojiMix[self.machineMemory[negativeValue]][0]}")
                                if self.emojiMix[self.machineMemory[value]][0] == self.emojiMix[self.machineMemory[negativeValue]][0]:
                                    if self.machineGuess == False:
                                        index = self.machineMemory[value]
                                        self.machineGuess = True
                                    else:
                                        index = self.machineMemory[negativeValue]
                                        if index == self.guess1_index:#Evitamos en caso de que la maquina acierte el primer valor quen o repita el segundo
                                            index = self.machineMemory[value]
                                    #Y el guess 2 deberia ser el negativo
                                    encontrado = True
                                    break
                                if len(self.machineMemory) % 2 != 0:
                                    index = 0
                                    valor_medio = self.machineMemory[mitad] // 2
                                    #if (0 <= self.machineMemory[value] < len(self.emojiMix) and 0 <= self.machineMemory[valor_medio] < len(self.emojiMix) and 0 <= self.machineMemory[negativeValue] < len(self.emojiMix)):
                                    """print("Indices medios value: ", self.emojiMix[self.machineMemory[value]][0], 
                                            "\nIndices medios valor_medio: ", self.emojiMix[self.machineMemory[valor_medio]][0], 
                                            "\nIndices medios negativo: ", self.emojiMix[self.machineMemory[negativeValue]][0])"""
                                    if (self.emojiMix[self.machineMemory[value]][0] == self.emojiMix[self.machineMemory[valor_medio]][0] or 
                                        self.emojiMix[self.machineMemory[negativeValue]][0] == self.emojiMix[self.machineMemory[valor_medio]][0]): #ayuda
                                        index = self.machineMemory[mitad]
                                        encontrado = True
                                        break
                                value += 1
                            else:
                                if abs(negativeValue) >= mitad:
                                    break
                                negativeValue -= 1
                                value = 0  
                                

                    elif encontrado == False:
                        index = random.randint(0, self.altoTablero * self.anchoTablero - 1);
                    else:
                        index = random.randint(0, self.altoTablero * self.anchoTablero - 1);
                
                if self.machineDifficult == 3: #Tercera opcion es la maquina super inteligente.
                    if len(self.machineMemory) == 0:
                        self.machineMemory = self.emojiMix.copy();#Evitamos que apunten al mismo espacio de memoria
                    
                    #print("ID emoji: ", self.machineMemory[0], "Indice: ", self.machineMemory.index(self.machineMemory[0]))
                    value = 1
                    encontrado = False;

                    while not encontrado:
                        if self.machineMemory.index(self.machineMemory[0]) == self.machineMemory.index(self.machineMemory[value]):
                            if self.machineGuess == False:
                                #print("Index es: ", self.emojiMix.index(self.machineMemory[0]))
                                index = self.emojiMix.index(self.machineMemory[0]);
                                encontrado = True;
                                self.machineGuess = True
                            else:
                                primer_indice = self.emojiMix.index(self.machineMemory[0])
                                index = self.emojiMix.index(self.machineMemory[value], primer_indice + 1)
                                #print("Maquina super inteligente elige el index: ", index)
                                encontrado = True
                                self.machineGuess = False
                                #print("Eliminando valor ", self.machineMemory[value], " y valor ", self.machineMemory[0])
                                del self.machineMemory[value]
                                del self.machineMemory[0]
                        else:
                            value += 1
                             
                
                #Lo que hacemos aqui es que nos aseguramos de que la maquina no diga posiciones ya adivinadas o repetri los mismos numeros en guess1 y guess2
                if guess_num == 2:
                    if self.machineDifficult == 1:
                        while index in self.posicionesAcertadas or index == self.guess1_index:
                            index = random.randint(0, self.altoTablero * self.anchoTablero - 1);
                    if self.machineDifficult == 2 and encontrado == False: #Evitamos que la maquina repita los numero de slef.machineMemory: #Evitamos que la maquina repita los numero de slef.machineMemory
                        self.machineGuess = False
                        while index in self.posicionesAcertadas or index == self.guess1_index or index in self.machineMemory:
                            index = random.randint(0, self.altoTablero * self.anchoTablero - 1);
                else:
                    if self.machineDifficult == 1:
                        while index in self.posicionesAcertadas:
                            index = random.randint(0, self.anchoTablero * self.altoTablero - 1)
                    if self.machineDifficult == 2 and encontrado == False: #Evitamos que la maquina repita los numero de slef.machineMemory
                        self.machineGuess = True #Cambio de turno despues de que machin haya dado una respuesta
                        while index in self.posicionesAcertadas or index in self.machineMemory or index in self.machineMemory:
                            index = random.randint(0, self.altoTablero * self.anchoTablero - 1);

            if index not in self.posicionesAcertadas:
                if guess_num == 1:
                    #Variable global de la clase para guardar el indice correcto
                    self.guess1_index = index
                    #En caso de que haya pasado las pruebas el indicie, se añade a la inteligencia de la maquina
                if self.machineDifficult == 2:
                    if index not in self.machineMemory:
                        self.machineMemory.append(index) #CAMBIAR ESTO, Y HAY QUE JUGAR CON EL EMOJI MIX, RECUERDALO EMI
                return index;
            if self.machineDifficult == 3:
                return index
            
    """
    data_table()
    Funcion que se encarga de recoger los datos del alumno y crear una lista de emojis randoms usando la funcion radnomEmoji
    Por ultimo esta función llama a printTable que esta se encargara de crear la tabla con lo necesitado
    """
    def data_table(self):
        print("\n===============GAME STARTS===============")
        print("============PLAYER VS PLAYER============")
        print("\nPlease, enter the board size in the format 'width x height'. Example: 5x6")
        print("The maximum allowed size is 5x6")
        #En caso de que el usuario añada un tamaño de tablero incorrecto
        while True:
            user = input('')
            parts = user.split('x')

            #Validar si el formato es correcto
            if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
                print("\nInvalid format. Please use 'width x height' (e.g., 3x3).")
                continue

            ancho, alto = int(parts[0]), int(parts[1])

            if ancho > 5 or alto > 6:
                print("\nThe maximum allowed size is 5x6. Please enter values within this range.")
                continue

            #Validamos si el tablero es par
            if (ancho * alto) % 2 != 0:
                print("\nThe board area must be an even number to form pairs. Please try again.")
                continue

            self.anchoTablero = ancho
            self.altoTablero = alto
            break

        #Calculamos el numro de emoji que vamos a usar en el tablero
        nrEmoji = int(self.anchoTablero * self.altoTablero) // 2  #Dejamos preparado que cada emoji tenga su pareja
        self.random_emoji(nrEmoji) #Randomizamos los emoji
        self.start()

       
    """
    paint_table()
    Funcion que se encarga de pintar el tablero, tambien cuadno hay una pareja acertada, que esta se comprueba en el metodo find_out_response(), 
    este se encarga de printear las parejas acertadas
    """
    def paint_table(self):
        index = 0

        print("\n")
        for i in range(self.altoTablero):
            for h in range(self.anchoTablero):
                current_index = i * self.anchoTablero + h
                if current_index in self.posicionesAcertadas:
                    #Si se encuentra en posicionesAcertadas, este pinta el emoji
                    print(self.emojiMix[current_index][1], end=' ')
                else:
                    #Si no se acierta la respuesta pinta un cuadrado en blanco.
                    print("□ ", end=' ')
                index += 1
            print()
        
        self.tableroVacio = False

    """
    show_guess()
    Funcion encargada de enseñar los emojis que estan en las posiciones acertadas, y los nuevos emojis acertados que entran por parametro
    """
    def show_guess(self, indices):
        for i in range(self.altoTablero):
            for h in range(self.anchoTablero):
                current_index = i * self.anchoTablero + h
                if current_index in self.posicionesAcertadas or current_index in indices:
                    print(self.emojiMix[current_index][1], end=' ')
                else:
                    print("□ ", end=' ')
            print()

                
    """
    find_out_response()
    Funcion encargada de comporobar las posiciones (parejas del array), si estas son correctas devuelve true (osea no cambia el turno del jugador y sigue jugando el que ha acertado)
    En caso de fallar, esta funcion se encarga de cambiar el turno y informar de que no hay coincidencia
    """
    def find_out_response(self, guess1, guess2):
        #guess1 y guess2 son iguales a emojis, por eso tenemos emojisAcertados y solo guardamos un guess1, es como si contara por los dos emojis :>
        #print(f"Guess 1: {guess1}\nGuess 2: {guess2}\nPosiciones acertadas: {self.posicionesAcertadas}")
        if guess1 == guess2 and guess1 not in self.emojisAcertado and guess2 not in self.emojisAcertado:
            print("\n*** MATCH FOUND ***")
            if self.machineGuess == True:
                self.machineMemory.clear()
                self.machineGuess = False
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
 
    """
    random_emoji()
    Genera un emjoji randome dpendiendo del resultado que ha introducido el usuario / 2 por ejemplo si el tablero es
    5x6 este es un 30, entonces lo dividimos entre 2 y el resultado es el numero de emojis que vamos a usar. Este
    ES DIVIDIDO EN EL METODO DATA TABLE.
    """
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

    """
    game_over()
    Funcion encargada de imprimir el score del juego
    """
    def game_over(self, players):
        print("\n\n\n\n========GAME IS OVER========\n\nResults are: ")
        print(f"\n{players[0]}: has matched {self.scorePlayer1} pairs - Total Score: {self.scorePlayer1 * 2}")
        print(f"\n{players[1]}: has matched {self.scorePlayer2} pairs - Total Score: {self.scorePlayer2 * 2}")
        print("\n========WINNER========\n")
        if (self.scorePlayer1 > self.scorePlayer2):
            print(f"{players[0]} WINS")
            print(f"\n{players[0]} TOTAL SCORE: {self.scorePlayer1 * 2}")
        elif (self.scorePlayer1 < self.scorePlayer2):
            print(f"{players[1]} WINS")
            print(f"\n{players[1]} TOTAL SCORE: {self.scorePlayer2 * 2}")
        else: 
            print(f"\n{players[0]} SCORE: {self.scorePlayer1 * 2}")
            print(f"{players[1]} SCORE: {self.scorePlayer2 * 2}")
            print("\nDRAW")