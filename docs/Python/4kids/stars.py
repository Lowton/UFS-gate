import turtle


t = turtle.Pen()
t.clear
#t.ht()

def circle_centre(a, b, c):
    pass


def draw_star(size, points):
	for x in range(points):
		t.fd(size)
		if points % 2 == 1: t.rt(180-180/points)
		elif points % 4 == 0: t.rt(180-360/points)
		elif points % 4 == 0: pass
		else: t.rt(90-180/points)

draw_star(150, 38)
