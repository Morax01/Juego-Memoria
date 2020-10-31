# Importación de Librerías
from random import *
from turtle import *
from freegames import path
import time

# Integrantes del equipo:
# Juan Angel Mora Moreno | A00517141
# Isaac Arredondo Padrón | A00828359

# Cargamos la imagen de fondo
car = path('car.gif')
# Hacemos una lista con los numeros del 1 al 32 dos veces
tiles = list(range(32)) * 2
# Inicializamos diccionarios
state = {'mark': None}
contador = {'tarjetas': 0}
hide = [True] * 64

# Dibuja un cuadrado blanco con un contorno negro en (x, y)
def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    # Genera linea por linea del cuadrado
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
    
# Convertir coordenadas (x, y) en índice de mosaicos
def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Convertir el recuento de mosaicos en coordenadas (x, y).
def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# La siguiente funcion se activa al tocar un mosaico
def tap(x, y):
    # Se utiliza la estructura global para los taps 
    global taps
    # Marca de actualización y mosaicos ocultos según el toque.
    spot = index(x, y)
    mark = state['mark']
    
    # Este condicional entra si las tarjetas son diferentes
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        # Se incrementa en 1 los taps y se despliega
        taps += 1
        print("Taps ejecutados: ",taps)
    # Entra aqui si las tarjetas son iguales
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        # Contabilizamos los pares de tarjetas volteados
        contador['tarjetas'] += 1
# Dibuja imagen y mosaicos.
def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    
    # Cada 100 milisegundos dibuja los cuadros
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
    
    # Valor default para inicializar tarjetas
    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # Aqui centramos los digitos en los cuadros
        if tiles[mark] > 9:
          goto(x + 2, y)
        else:
          goto(x + 15, y)
        # Imprimimos digitos en pantalla
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
    
    # Actualizamos pantalla
    update()
    ontimer(draw, 100)
    
    # Aqui detectamos cuando todos los cuadros se han volteado
    if contador['tarjetas'] == 32:
      color("blue")
      begin_fill()
      # Dibujamos un rectangulo de fondo azul
      goto(-200,0)
      forward(400)
      left(90)
      forward(50)
      left(90)
      forward(400)
      left(90)
      forward(50)
      left(90)
      end_fill()
      goto(195,10)
      color("yellow")
      # Escribimos sobre el rectangulo la frase final
      write("¡Felicidades has ganado!", False,
          "right", ("arial", 20, "bold italic"))
      time.sleep(5)
      # Salimos del juego
      exit()

# En este punto inicializamos lo mas importante del juego
# por ejemplo, la interfaz, los taps, la funcion principal, etc
taps = 0 
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

# Inciso 4:
# Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude
# a tener mejor memoria ?
# Respuesta al inciso 4:
# Como idea se nos ocurre cambiar los pares de los números por letras e inclusive por pares de
# colores para que los usarios se les facilité a la hora de recordar cada casilla volteada.
