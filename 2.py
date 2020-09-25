import turtle as tl
import numpy as np
a_0 = (0, 0, 0, 20, 90, 40, 90, 20, 90 ,40)
a_1 = (0, -20, -45, 20*np.sqrt(2), 135, 40)
a_2 = (0, 0, 0, 20, 90, 20, 45, 20*np.sqrt(2), -135, 20 )
a_3 = (0, 0, 0, 20, 135, 20*np.sqrt(2), -135, 20, 135, 20*np.sqrt(2))
a_4 = (0, 0, 90, 20, -90, 20, -90, 20, 180, 40)
a_5 = (20, 0, 180, 20, -90, 20, -90, 20, 90, 20, 90, 20)
a_6 = (20, 0, 135, 20*np.sqrt(2), -45, 20, -90, 20, -90, 20, -90, 20 )
a_7 = (0, 0, 0, 20, 135, 20*np.sqrt(2), -45, 20)
a_8 = (0, 0, 0, 20, 90, 40, 90, 20, 90, 40, 180, 20, -90, 20)
a_9 = (0, 0, 0, 20, 90, 20, 45, 20*np.sqrt(2), 180, 20*np.sqrt(2), -135, 20, 90, 20)
a = [a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7, a_8, a_9]
st = [1, 4, 1, 7, 0, 0]
print(len(a_0))
tl.penup()
tl.goto(-40, 0)
tl.pendown()
x = -40
y = 0

for j in range((len(st))):
	tl.penup()
	tl.goto(x + a[st[j]][0], y+ a[st[j]][1])
	tl.pendown()
	tl.seth(0)
	for i in range( len(a[st[j]])):
		if (i % 2 == 1) and (i >= 2):
			tl.forward(a[st[j]][i])
		if (i % 2 == 0 ) and (i >= 2):
			tl.right(a[st[j]][i])
	x += 30
tl.mainloop()