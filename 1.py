import turtle as tl
from random import *
x = 0
y = 0
go = 0
an = 0
for i in range(55):
	go = randint(10, 50)
	an = randint(-170, 170)
	tl.left(an)
	tl.forward(go)
tl.mainloop()