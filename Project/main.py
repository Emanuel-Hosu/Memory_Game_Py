# main.py
from engine import Engine  # Importa la clase Engine

#Importamos la clase main y instanciamos una variable llamada engine
engine = Engine()

#Mensaje de bienvenida
#engine.welcome()
engine.menu();
engine.get_menu_choice()

#Recogemos el input del usuario y hacemos un split, donde en la misma clase de este vamos a crear el tablero
engine.data_table()
