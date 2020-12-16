import turtle
import time 
import random

posponer = 0.1

# Marcador
score = 0
high_score = 0

# Ventana
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0) # Para que se vea más fluido

# Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("grey")
cabeza.penup() # Quita el rastro
cabeza.goto(0,0) # Spawn
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# FUNCIONES
def up():
	cabeza.direction = "up"
def down():
	cabeza.direction = "down"
def right():
	cabeza.direction = "right"
def left():
	cabeza.direction = "left"

def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)

# Teclado
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

# Segmentos
Segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write(f"Score: {score}    High Score: {high_score}", align = "center", font = ("Courier", 14, "normal"))



while (True):
	wn.update()

	#Colision bordes
	if cabeza.xcor() > 280 or cabeza.ycor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"

		#Esconder los objetos

		for segmento in Segmentos:
			segmento.goto(1000,1000)

		Segmentos.clear()
		texto.clear()
		score = 0
		texto.write(f"Score: {score}    High Score: {high_score}", align = "center", font = ("Courier", 14, "normal"))


	# Colisiones comida
	if cabeza.distance(comida) < 20:
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		comida.goto(x,y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.color("green")
		nuevo_segmento.penup() # Quita el rastro

		Segmentos.append(nuevo_segmento)

		score += 10
		if score > high_score:
			high_score = score

		texto.clear()
		texto.write(f"Score: {score}    High Score: {high_score}", align = "center", font = ("Courier", 14, "normal"))



	# Mover cuerpo
	totalSeg = len(Segmentos) # Te da el valor del 1 a n

	for i in range(totalSeg -1, 0, -1): #start, stop, steps ...5,4,3,2,1. 
		x = Segmentos[i - 1].xcor()
		y = Segmentos[i - 1].ycor()
		Segmentos[i].goto(x,y)

	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		Segmentos[0].goto(x,y)

	mov()

	# Colisiones con el cuerpo

	for segmento in Segmentos:
		if cabeza.distance(segmento) < 20:

			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"
			texto.clear()
			score = 0
			texto.write(f"Score: {score}    High Score: {high_score}", align = "center", font = ("Courier", 14, "normal"))

			for segmento in Segmentos:

				segmento.goto(1000,1000)
			
			Segmentos.clear()



	time.sleep(posponer)
