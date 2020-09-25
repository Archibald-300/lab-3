import turtle as tl
import numpy as np
input = open('3.txt', 'r' )
a= input.readlines()
st = [1, 4, 1, 7, 0, 0]
tl.penup()
tl.goto(-40, 0)
tl.pendown()
x = -40
y = 0

for j in range((len(st))):
	tl.penup()
	tl.goto(x + eval(a[st[j]])[0], y+ eval(a[st[j]])[1])
	tl.pendown()
	tl.seth(0)
	for i in range( len(eval(a[st[j]]))):
		if (i % 2 == 1) and (i >= 2):
			tl.forward(eval(a[st[j]])[i])
		if (i % 2 == 0 ) and (i >= 2):
			tl.right(eval(a[st[j]])[i])
	x += 30
tl.mainloop()
input.close()