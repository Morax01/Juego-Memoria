# Importación de Librerías
from random import *
from turtle import *
from freegames import path
import time

# Integrantes del equipo:
# Juan Angel Mora Moreno | A00517141
# Nombre y matricula

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
contador = {'tarjetas': 0}
hide = [True] * 64

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    # Se utiliza la estructura global para los taps 
    global taps
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        # Se incrementa en 1 los taps y se despliega
        taps += 1
        print("Taps ejecutados: ",taps)
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        contador['tarjetas'] += 1

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)
    # Aqui detectamos cuando todos los cuadros se han volteado
    if contador['tarjetas'] == 32:
      color("blue")
      begin_fill()
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
      write("!Felicidades has ganado¡", False,
          "right", ("arial", 20, "bold italic"))
      time.sleep(5)
      exit()

# Inicializador de los taps ejecutados
taps = 0 
shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

# Respuesta al inciso 4:
# Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?
# Como idea se nos ocurre cambiar los pares de los números por letras e inclusive por pares de colores para que los uusarios se les facilité a la hora de recordar cada casilla volteada.
