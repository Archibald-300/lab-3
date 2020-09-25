import turtle as tl
import numpy as np
Vx = 10
Vy = 60
dt = 0.1
y = 0
x = -300
tl.speed(0)
tl.goto(1000, 0)
tl.goto(-300, 0)
tl.speed(2)
while Vy > 9:
	while y > -0.5:
		tl.goto(x,y)
		x += Vx * dt
		y += Vy * dt - (9.8)*dt ** 2/2
		Vy -= 9.8 * dt
		if Vx > 0.5:
			Vx -= 0.1 * dt
		else:
			Vx = 0

	y = 0
	Vx = 0.8 * Vx
	Vy = (-0.8) * Vy
	#x += Vx * dt
	#y += Vy * dt - (9.8)*dt ** 2/2
	#Vy -= 9.8*dt
	