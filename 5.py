import turtle as tl
import numpy as np
from random import *
n = 25
s = 100
tl.speed(0)
tl.penup()
tl.goto(-200, 200)
tl.pendown()
x = []
y = []

for i in range(4):
	tl.forward(400)
	tl.right(90)
tl.ht()
pool = [tl.Turtle( shape = 'circle' ) for i in  range (n)]
for unit in pool:
	unit.penup()
	unit.shapesize(0.8)
	unit.speed(100)
	unit.goto(int(randint(-190, 190)), int(randint(-190, 190)))
	unit.left(randint(-180, 180))
	
print(np.arctan(0))	
k = 0
vx = []
vy = []
for i in range(n):
	vx.insert(i, randint(-3, 3))
	vy.insert(i, randint(-3, 3))
while (True):
	k = -1
	for unit in pool:
		k += 1
		t = unit.position() 
		x.insert(k,int( t[0]))
		y.insert(k, t[1])
		unit.goto(x[k] + vx[k], y[k] + vy[k])
		if ((t[0] + vx[k]) >= 200) :
			vx.insert(k, - vx[k])
			x.insert(k, 198)
		if ((t[0] + vx[k]) <= -200) :
			vx.insert(k, - vx[k])
			x.insert(k, -198)					
		elif (t[1] + vy[k])>= 200:
			vy.insert(k, -vy[k])
			y.insert(k, 198)
		elif (t[1] + vy[k])<= -200:
			vy.insert(k, -vy[k])
