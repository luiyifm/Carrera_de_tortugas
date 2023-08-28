import turtle
import random
#Crear pantalla
s=turtle.Screen()
s.title("Carrera Tortugas")
#Crear personajes
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
    print("Ha avanzado {} pasos".format(turno2))
    if t1.pos() >= (200, 150) and t2.pos() >= (200, -100):
        empate=True
        print("Empate")
        break
    elif t1.pos() >= (200, 150):
        SW= True
        print("Jugador verde ha ganado")
        s.bgcolor("green")
        break
    elif t2.pos() >= (200, -100):
        SW= True
        print("Jugador Azul ha ganado")
        s.bgcolor("blue")
        break

print("Fin del juego")



turtle.done()