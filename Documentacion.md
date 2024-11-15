# Documentación del Juego de Memoria

## Descripción General
Este proyecto implementa un juego de memoria con emojis que soporta tres modos de juego diferentes:
- Jugador vs Jugador
- Jugador vs Máquina
- Máquina vs Máquina

El juego está implementado en Python y utiliza una arquitectura basada en clases con dos archivos principales:
- `main.py`: Punto de entrada del programa
- `engine.py`: Contiene la lógica principal del juego

## Estructura del Código

### Clase Engine
La clase principal que maneja toda la lógica del juego.

#### Atributos Principales
- `emoji`: Diccionario que almacena los emojis disponibles
- `emojiMix`: Lista de emojis mezclados para el tablero actual
- `finalizado`: Estado de finalización del juego
- `player1`, `player2`: Control de turnos
- `anchoTablero`, `altoTablero`: Dimensiones del tablero
- `posicionesAcertadas`: Lista de posiciones ya encontradas
- `scorePlayer1`, `scorePlayer2`: Puntuaciones
- `gameMode`: Modo de juego seleccionado
- `machineDifficult`: Nivel de dificultad de la máquina
- `machineMemory`: Memoria de la máquina para modos inteligentes

#### Métodos Principales

1. `menu()` y `difficulty_menu()`
   - Muestran las opciones de juego y dificultad
   - Permiten la selección del modo de juego y nivel de dificultad

2. `data_table()`
   - Inicializa el tablero de juego
   - Valida las dimensiones introducidas
   - Asegura que el área del tablero sea par

3. `start()`
   - Método principal que controla el flujo del juego
   - Maneja los turnos y la lógica de cada modo de juego
   - Implementa las diferentes estrategias de la máquina

4. `get_valid_guess()`
   - Obtiene y valida las jugadas de jugadores y máquinas
   - Implementa la inteligencia artificial en diferentes niveles:
     - Nivel 1 (Fácil): Selección aleatoria
     - Nivel 2 (Medio): Memoria temporal
     - Nivel 3 (Difícil): Memoria completa

5. `paint_table()` y `show_guess()`
   - Manejan la visualización del tablero
   - Muestran las cartas descubiertas y ocultas

## Características Avanzadas

### Inteligencia Artificial
El juego implementa tres niveles de IA:
1. **Fácil**: Selecciones completamente aleatorias
2. **Medio**: Memoria temporal que recuerda jugadas previas
3. **Difícil**: Memoria completa del tablero

### Validación de Entrada
- Comprueba dimensiones máximas (5x6)
- Asegura área par para parejas válidas
- Previene selección de posiciones ya descubiertas

## Esquemas de Prueba

### Prueba 1: Creación del Tablero
```python
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 1

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
4x4

========Player 1 TURN========


□  □  □  □  
□  □  □  □  
□  □  □  □  
□  □  □  □  

```

### Prueba 2: Modo Jugador vs Jugador
```python
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 1

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
3x2

========Player 1 TURN========


□  □  □  
□  □  □  

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x1
🍉 □  □  
□  □  □  

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
3x2
🍉 □  □  
□  □  🍇 

**+ NOT MATCH ***

========Player 2 TURN========


□  □  □  
□  □  □  

========Player 2 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x2
□  □  □  
□  🥑 □  

========Player 2 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
3x1
□  □  🥑 
□  🥑 □  

*** MATCH FOUND ***


□  □  🥑 
□  🥑 □  

========Player 2 TURN========


□  □  🥑 
□  🥑 □  

========Player 2 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x1
□  🍉 🥑 
□  🥑 □  

========Player 2 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x1
🍉 🍉 🥑 
□  🥑 □  

*** MATCH FOUND ***


🍉 🍉 🥑 
□  🥑 □  

========Player 2 TURN========


🍉 🍉 🥑 
□  🥑 □  

========Player 2 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x2
🍉 🍉 🥑 
🍇 🥑 □  

========Player 2 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
3x2
🍉 🍉 🥑 
🍇 🥑 🍇 

*** MATCH FOUND ***


🍉 🍉 🥑 
🍇 🥑 🍇 




========GAME IS OVER========

Results are: 

Player 1: has matched 0 pairs - Total Score: 0

Player 2: has matched 3 pairs - Total Score: 6

========WINNER========

Player 2 WINS

Player 2 TOTAL SCORE: 6
```

### Prueba 3: Modo Jugador vs Máquina
```python
//Prueba 3 - Modo Jugador vs Máquina Super Inteligente
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 2

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
2x3

=======Difficulty Menu===========

Choose machine difficulty

1. Easy

2. Medium

3. Hard

4. Exit

Select a option(1-3): 3

========Player 1 TURN========


□  □  
□  □  
□  □  

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x1
🍒 □  
□  □  
□  □  

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x2
🍒 □  
□  🥑 
□  □  

**+ NOT MATCH ***

========Super Inteligen Machine TURN========


□  □  
□  □  
□  □  

========Super Inteligen Machine - 1º GUESS========

🍒 □  
□  □  
□  □  

Super Inteligen Machine has select: 🍒

========Super Inteligen Machine - 2º GUESS========

🍒 □  
□  □  
□  🍒 

Super Inteligen Machine has select the pairs: 🍒 and 🍒

*** MATCH FOUND ***


🍒 □  
□  □  
□  🍒 

========Super Inteligen Machine TURN========


🍒 □  
□  □  
□  🍒 

========Super Inteligen Machine - 1º GUESS========

🍒 🍓 
□  □  
□  🍒 

Super Inteligen Machine has select: 🍓

========Super Inteligen Machine - 2º GUESS========

🍒 🍓 
🍓 □  
□  🍒 

Super Inteligen Machine has select the pairs: 🍓 and 🍓

*** MATCH FOUND ***


🍒 🍓 
🍓 □  
□  🍒 

========Super Inteligen Machine TURN========


🍒 🍓 
🍓 □  
□  🍒 

========Super Inteligen Machine - 1º GUESS========

🍒 🍓 
🍓 🥑 
□  🍒 

Super Inteligen Machine has select: 🥑

========Super Inteligen Machine - 2º GUESS========

🍒 🍓 
🍓 🥑 
🥑 🍒 

Super Inteligen Machine has select the pairs: 🥑 and 🥑

*** MATCH FOUND ***


🍒 🍓 
🍓 🥑 
🥑 🍒 




========GAME IS OVER========

Results are: 

Player 1: has matched 0 pairs - Total Score: 0

Machine: has matched 3 pairs - Total Score: 6

========WINNER========

Machine WINS

Machine TOTAL SCORE: 6
```

### Prueba 4: Modo Máquina vs Máquina
```python
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 3

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
3x2

========Machine 1 TURN========


□  □  □  
□  □  □  

========Machine 1 - 1º GUESS========

□  □  □  
□  □  🍍 

Machine 1 has select: 🍍

========Machine 1 - 2º GUESS========

Cannot select the same position twice, please choose again.

========Machine 1 - 2º GUESS========

🍉 □  □  
□  □  🍍 

Machine 1 has select the pairs: 🍍 and 🍉

**+ NOT MATCH ***

========Machine 2 TURN========


□  □  □  
□  □  □  

========Machine 2 - 1º GUESS========

□  □  □  
□  🍉 □  

Machine 2 has select: 🍉

========Machine 2 - 2º GUESS========

□  🍍 □  
□  🍉 □  

Machine 2 has select the pairs: 🍉 and 🍍

**+ NOT MATCH ***

========Machine 1 TURN========


□  □  □  
□  □  □  

========Machine 1 - 1º GUESS========

□  □  □  
🥭 □  □  

Machine 1 has select: 🥭

========Machine 1 - 2º GUESS========

□  □  □  
🥭 □  🍍 

Machine 1 has select the pairs: 🥭 and 🍍

**+ NOT MATCH ***

========Machine 2 TURN========


□  □  □  
□  □  □  

========Machine 2 - 1º GUESS========

□  □  □  
□  □  🍍 

Machine 2 has select: 🍍

========Machine 2 - 2º GUESS========

□  □  □  
🥭 □  🍍 

Machine 2 has select the pairs: 🍍 and 🥭

**+ NOT MATCH ***

========Machine 1 TURN========


□  □  □  
□  □  □  

========Machine 1 - 1º GUESS========

□  □  🥭 
□  □  □  

Machine 1 has select: 🥭

========Machine 1 - 2º GUESS========

□  □  🥭 
🥭 □  □  

Machine 1 has select the pairs: 🥭 and 🥭

*** MATCH FOUND ***


□  □  🥭 
🥭 □  □  

========Machine 1 TURN========


□  □  🥭 
🥭 □  □  

========Machine 1 - 1º GUESS========


========Machine 1 - 1º GUESS========


========Machine 1 - 1º GUESS========

□  □  🥭 
🥭 □  🍍 

Machine 1 has select: 🍍

========Machine 1 - 2º GUESS========

Cannot select the same position twice, please choose again.

========Machine 1 - 2º GUESS========

🍉 □  🥭 
🥭 □  🍍 

Machine 1 has select the pairs: 🍍 and 🍉

**+ NOT MATCH ***

========Machine 2 TURN========


□  □  🥭 
🥭 □  □  

========Machine 2 - 1º GUESS========

🍉 □  🥭 
🥭 □  □  

Machine 2 has select: 🍉

========Machine 2 - 2º GUESS========

🍉 □  🥭 
🥭 🍉 □  

Machine 2 has select the pairs: 🍉 and 🍉

*** MATCH FOUND ***


🍉 □  🥭 
🥭 🍉 □  

========Machine 2 TURN========


🍉 □  🥭 
🥭 🍉 □  

========Machine 2 - 1º GUESS========


========Machine 2 - 1º GUESS========


========Machine 2 - 1º GUESS========


========Machine 2 - 1º GUESS========


========Machine 2 - 1º GUESS========

🍉 □  🥭 
🥭 🍉 🍍 

Machine 2 has select: 🍍

========Machine 2 - 2º GUESS========


========Machine 2 - 2º GUESS========

🍉 🍍 🥭 
🥭 🍉 🍍 

Machine 2 has select the pairs: 🍍 and 🍍

*** MATCH FOUND ***


🍉 🍍 🥭 
🥭 🍉 🍍 




========GAME IS OVER========

Results are: 

Machine 1: has matched 1 pairs - Total Score: 2

Machine 2: has matched 2 pairs - Total Score: 4

========WINNER========

Machine 2 WINS

Machine 2 TOTAL SCORE: 4
```

### Prueba 5: Validación de Entrada
```python
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 1

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
5x7

The maximum allowed size is 5x6. Please enter values within this range.
5-6

Invalid format. Please use 'width x height' (e.g., 3x3).
3 

Invalid format. Please use 'width x height' (e.g., 3x3).
5 6 

Invalid format. Please use 'width x height' (e.g., 3x3).
5x6

========Player 1 TURN========


□  □  □  □  □  
□  □  □  □  □  
□  □  □  □  □  
□  □  □  □  □  
□  □  □  □  □  
□  □  □  □  □  

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
```

### Prueba 6: Niveles de Dificultad - Fácil
```python
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 2

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
2x3

=======Difficulty Menu===========

Choose machine difficulty

1. Easy

2. Medium

3. Hard

4. Exit

Select a option(1-3): 1

========Player 1 TURN========


□  □  
□  □  
□  □  

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x1
🍒 □  
□  □  
□  □  

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x2
🍒 □  
□  🍋 
□  □  

**+ NOT MATCH ***

========Machine TURN========


□  □  
□  □  
□  □  

========Machine - 1º GUESS========

□  □  
□  🍋 
□  □  

Machine has select: 🍋

========Machine - 2º GUESS========

□  □  
□  🍋 
🍌 □  

Machine has select the pairs: 🍋 and 🍌

**+ NOT MATCH ***

========Player 1 TURN========


□  □  
□  □  
□  □  

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x3
□  □  
□  □  
□  🍒 

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x1
🍒 □  
□  □  
□  🍒 

*** MATCH FOUND ***


🍒 □  
□  □  
□  🍒 

========Player 1 TURN========


🍒 □  
□  □  
□  🍒 

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x1
🍒 🍌 
□  □  
□  🍒 

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x2
🍒 🍌 
□  🍋 
□  🍒 

**+ NOT MATCH ***

========Machine TURN========


🍒 □  
□  □  
□  🍒 

========Machine - 1º GUESS========

🍒 🍌 
□  □  
□  🍒 

Machine has select: 🍌

========Machine - 2º GUESS========

🍒 🍌 
🍋 □  
□  🍒 

Machine has select the pairs: 🍌 and 🍋

**+ NOT MATCH ***

========Player 1 TURN========


🍒 □  
□  □  
□  🍒 

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x1
🍒 🍌 
□  □  
□  🍒 

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x3
🍒 🍌 
□  □  
🍌 🍒 

*** MATCH FOUND ***


🍒 🍌 
□  □  
🍌 🍒 

========Player 1 TURN========


🍒 🍌 
□  □  
🍌 🍒 

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x2
🍒 🍌 
□  🍋 
🍌 🍒 

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x2
🍒 🍌 
🍋 🍋 
🍌 🍒 

*** MATCH FOUND ***


🍒 🍌 
🍋 🍋 
🍌 🍒 




========GAME IS OVER========

Results are: 

Player 1: has matched 3 pairs - Total Score: 6

Machine: has matched 0 pairs - Total Score: 0

========WINNER========

Player 1 WINS

Player 1 TOTAL SCORE: 6
```

### Prueba 6: Niveles de Dificultad - Intermedio
```python
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 2

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
2x3

=======Difficulty Menu===========

Choose machine difficulty

1. Easy

2. Medium

3. Hard

4. Exit

Select a option(1-3): 2

========Player 1 TURN========


□  □  
□  □  
□  □  

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x1
🍋 □  
□  □  
□  □  

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x2
🍋 □  
□  🥭 
□  □  

**+ NOT MATCH ***

========Inteligent Machine TURN========


□  □  
□  □  
□  □  

========Inteligent Machine - 1º GUESS========

□  □  
□  □  
🍌 □  

Inteligent Machine has select: 🍌

========Inteligent Machine - 2º GUESS========

□  🍌 
□  □  
🍌 □  

Inteligent Machine has select the pairs: 🍌 and 🍌

*** MATCH FOUND ***


□  🍌 
□  □  
🍌 □  

========Inteligent Machine TURN========


□  🍌 
□  □  
🍌 □  

========Inteligent Machine - 1º GUESS========

□  🍌 
🥭 □  
🍌 □  

Inteligent Machine has select: 🥭

========Inteligent Machine - 2º GUESS========

□  🍌 
🥭 🥭 
🍌 □  

Inteligent Machine has select the pairs: 🥭 and 🥭

*** MATCH FOUND ***


□  🍌 
🥭 🥭 
🍌 □  

========Inteligent Machine TURN========


□  🍌 
🥭 🥭 
🍌 □  

========Inteligent Machine - 1º GUESS========

□  🍌 
🥭 🥭 
🍌 🍋 

Inteligent Machine has select: 🍋

========Inteligent Machine - 2º GUESS========

🍋 🍌 
🥭 🥭 
🍌 🍋 

Inteligent Machine has select the pairs: 🍋 and 🍋

*** MATCH FOUND ***


🍋 🍌 
🥭 🥭 
🍌 🍋 




========GAME IS OVER========

Results are: 

Player 1: has matched 0 pairs - Total Score: 0

Machine: has matched 3 pairs - Total Score: 6

========WINNER========

Machine WINS

Machine TOTAL SCORE: 6
```

### Prueba 6: Niveles de Dificultad - Difícil
```python
========Welcome to Memory========

===========Menu===========

Choose the game mode

1. Play - Player 1 vs Player 2

2. Play - Player vs Machine

3. Play - Machine 1 vs Machine 2

4. Exit

Select a option(1-4): 2

===============GAME STARTS===============
============PLAYER VS PLAYER============

Please, enter the board size in the format 'width x height'. Example: 5x6
The maximum allowed size is 5x6
2x3

=======Difficulty Menu===========

Choose machine difficulty

1. Easy

2. Medium

3. Hard

4. Exit

Select a option(1-3): 3

========Player 1 TURN========


□  □  
□  □  
□  □  

========Player 1 - 1º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
1x1
🍊 □  
□  □  
□  □  

========Player 1 - 2º GUESS========

Enter the answer in 'width x height' format (e.g., 3x3):
2x1
🍊 🍒 
□  □  
□  □  

**+ NOT MATCH ***

========Super Inteligen Machine TURN========


□  □  
□  □  
□  □  

========Super Inteligen Machine - 1º GUESS========

🍊 □  
□  □  
□  □  

Super Inteligen Machine has select: 🍊

========Super Inteligen Machine - 2º GUESS========

🍊 □  
□  □  
□  🍊 

Super Inteligen Machine has select the pairs: 🍊 and 🍊

*** MATCH FOUND ***


🍊 □  
□  □  
□  🍊 

========Super Inteligen Machine TURN========


🍊 □  
□  □  
□  🍊 

========Super Inteligen Machine - 1º GUESS========

🍊 🍒 
□  □  
□  🍊 

Super Inteligen Machine has select: 🍒

========Super Inteligen Machine - 2º GUESS========

🍊 🍒 
□  □  
🍒 🍊 

Super Inteligen Machine has select the pairs: 🍒 and 🍒

*** MATCH FOUND ***


🍊 🍒 
□  □  
🍒 🍊 

========Super Inteligen Machine TURN========


🍊 🍒 
□  □  
🍒 🍊 

========Super Inteligen Machine - 1º GUESS========

🍊 🍒 
🍋 □  
🍒 🍊 

Super Inteligen Machine has select: 🍋

========Super Inteligen Machine - 2º GUESS========

🍊 🍒 
🍋 🍋 
🍒 🍊 

Super Inteligen Machine has select the pairs: 🍋 and 🍋

*** MATCH FOUND ***


🍊 🍒 
🍋 🍋 
🍒 🍊 




========GAME IS OVER========

Results are: 

Player 1: has matched 0 pairs - Total Score: 0

Machine: has matched 3 pairs - Total Score: 6

========WINNER========

Machine WINS

Machine TOTAL SCORE: 6
```

## Criterios de Evaluación Cumplidos

ETAPA 1: Creación del tablero (20%)
- Implementación completa de la lógica de tablero
- Validación de dimensiones y paridad
- Distribución aleatoria de emojis

ETAPA 2: Modo Persona vs Persona (25%)
- Sistema de turnos funcionando
- Validación de jugadas
- Conteo de puntuación

ETAPA 3: Modo Persona vs Máquina (15%)
- Tres niveles de dificultad
- Inteligencia artificial implementada
- Interacción jugador-máquina

ETAPA 4: Modo Máquina vs Máquina (10%)
- Funcionamiento automático
- Visualización de jugadas
- Resultado final correcto

ETAPA 5: Diseño y Optimización (10%)
- Código modular y organizado
- Manejo de errores
- Interfaz clara y usable

DOCUMENTACIÓN Y PRUEBAS
- Documentación detallada
- Pruebas exhaustivas
- Comentarios explicativos