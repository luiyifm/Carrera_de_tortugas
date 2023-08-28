## Carrera de Tortugas

### Descripción

Este es un juego de carreras de tortugas en Python. El juego se desarrolla en una pantalla de 500x500 píxeles. Hay dos tortugas, una verde y una azul. El objetivo del juego es que cada tortuga llegue a su destino antes que la otra.

### Instrucciones

Para jugar, primero debe importar las bibliotecas necesarias. Luego, debe crear la pantalla y los personajes. A continuación, debe definir las funciones que se utilizarán en el juego. Finalmente, debe iniciar el juego. cada paso se da presionando la tecla enter.

### Código

A continuación se muestra el código del juego:

```python
import turtle
import random

# Crear pantalla
s = turtle.Screen()
s.title("Carrera Tortugas")

# Crear personajes
t1 = turtle.Turtle(shape="turtle")  
t1.color("green", "green")
t1.shapesize(1.5,1.5,1.5)

t2 = turtle.Turtle(shape="turtle")
t2.color("blue", "blue")
t2.shapesize(1.5,1.5,1.5)

t2.speed(10.5)
t1.speed(10.5)
t1.penup()
t2.penup()

t1.goto(250,100)
t2.goto(250,-150)
t1.pendown()
t2.pendown()
t1.circle(50)
t2.circle(50)

t1.penup()
t2.penup()

t1.goto(-250, 150)
t2.goto(-250, -100)

t1.pendown()
t2.pendown()

dado=[6]
empate=False
SW=False
while SW==False or empate==False:
    turno1=input("Juador Verde: Oprima enter")
    turno1=random.choice(dado)*20
    t1.forward(turno1)
    print("Ha avanzado {} pasos".format(turno1))
    turno2=input("Oprima enter")
    turno2=random.choice(dado)*20
    t2.forward(turno2)
