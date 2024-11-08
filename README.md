---

# 🧠 Consola Memory Game

¡Bienvenidos al increíble juego de memoria en consola! Este proyecto es parte de la asignatura **Sistemas de Gestión Empresarial** de 2DAM y está desarrollado en Python. 🎓 Este README te guiará para comprender, ejecutar y disfrutar (con moderación) del juego. 

## 🎯 Objetivo del juego

Desarrollado para desafiar la memoria visual en cada jugador, este juego clásico de memoria consiste en encontrar pares de emojis ocultos en una cuadrícula. Gana el jugador que descubra más pares al final de la partida.

---

## 🛠️ Instalación y ejecución

1. **Descarga o clona el repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/consola-memory-game.git
    ```
   
2. **Navega hasta la carpeta del proyecto**:
    ```bash
    cd Project
    ```

3. **Ejecuta el juego**:
    ```bash
    python3 main.py
    ```

4. **¡Empieza a jugar y reta a tus amigos o a la máquina!**

---

## 🚀 Instrucciones de juego

1. **Elige el modo de juego** desde el menú principal:
    - `1` - **Player 1 vs Player 2**: Modo clásico donde dos jugadores se enfrentan en turnos.
    - `2` - **Player vs Machine**: Elige entre varios niveles de dificultad para retar a la IA.
    - `3` - **Machine vs Machine**: Observa cómo dos máquinas compiten por la gloria.
    - `4` - **Exit**: Cierra el juego (cuando la partida está muy intensa y necesitas un descanso...).

2. **Configura la dificultad**: Al seleccionar un enfrentamiento contra la máquina, puedes elegir entre varios niveles de dificultad:
    - **Easy**: La máquina tiene memoria selectiva (casi inexistente).
    - **Medium**: Memoria algo más desarrollada.
    - **Hard**: Memoria fotográfica — ¡más vale que tengas buena suerte!

3. **Selecciona el tamaño del tablero**: Introduce las dimensiones del tablero en el formato `Ancho x Alto` (por ejemplo, `4x4`). **Importante:** el área debe ser un número par para que se puedan formar parejas. Las dimensiones máximas permitidas son `5x6`.

---

## 📝 Reglas del juego

- El jugador selecciona dos posiciones para descubrir los emojis escondidos.
- Si los emojis coinciden, el jugador gana un punto y retiene el turno.
- Si no coinciden, el turno pasa al siguiente jugador.
- La partida termina cuando todos los pares están descubiertos.

---

## 📊 Resultados

Cuando termina el juego, los resultados muestran:
- El número de pares que cada jugador ha acertado.
- El ganador basado en la puntuación total.

¿Empate? Sí, es posible. ¡En ese caso, habrá que desempatar en otra partida!

---

## 📂 Estructura del Proyecto

El proyecto se organiza en los siguientes archivos y carpetas:

- `engine.py`: Contiene la clase `Engine` que define la lógica del juego.
- `main.py`: Archivo principal que inicia el juego y administra el menú.
- `README.md`: Este archivo que estás leyendo (¡Hola!).

---

## 📚 Ejemplo de Uso

```plaintext
========= Welcome to Memory =========

=========== Menu ===========
1. Player 1 vs Player 2
2. Player vs Machine
3. Machine 1 vs Machine 2
4. Exit
Select an option (1-4):
```

---

## ⚠️ Notas Importantes

- **Error Handling**: Si introduces un tamaño de tablero incorrecto o una opción inválida, el juego te guiará para hacer una mejor elección (a prueba de errores humanos).
- **Límites de Tablero**: Las dimensiones máximas del tablero son 5x6. Mayor que eso y el cerebro de la máquina se sobrecalienta.
- **El juego es solo para consola**: Así que no te sorprendas si no ves gráficos ni emojis a color.

---

## 🏆 Créditos y Contribuciones

Este proyecto fue desarrollado como parte del curso de **2DAM**. Gracias a los valientes que probaron el juego y a los pacientes que leyeron hasta aquí. 😄

---

¡Que empiece el reto de memoria!
