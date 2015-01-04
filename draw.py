#!/usr/bin/env python3

import math
import cairo

#def math.radians(d):
#	return d * (math.pi / 180)

r = 100.0
WIDTH, HEIGHT = 10*r, 10*r
startx = 5*r
starty = 5*r
currentx = 0.0
currenty = 0.0
currdeg = 0
arcx = math.cos(math.radians(45)) * r
arcy = math.sin(math.radians(45)) * r
surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, int(WIDTH), int(HEIGHT))
ctx = cairo.Context (surface)

def add(t):
	global currentx, currenty, currdeg
	if t == 'cr':
		ctx.new_sub_path()
		if currdeg == 0:
			ctx.arc (currentx-r, currenty, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 45:
			ctx.arc (currentx - arcx, currenty - arcy, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 90:
			ctx.arc (currentx, currenty-r, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 135:
			ctx.arc (currentx + arcx, currenty - arcy, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 180:
			ctx.arc (currentx+r, currenty, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 225:
			ctx.arc (currentx+arcx, currenty+arcy, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 270:
			ctx.arc (currentx, currenty+r, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 315:
			ctx.arc (currentx - arcx, currenty + arcy, r, math.radians(currdeg), math.radians(currdeg+45))
		elif currdeg == 360:
			ctx.arc (currentx-r, currenty, r, math.radians(currdeg), math.radians(currdeg+45))

		if currdeg == 360:
			currdeg = 45
		else:
			currdeg = currdeg + 45
	if t == 'cl':
		ctx.new_sub_path()
		if currdeg == 0:
			ctx.arc_negative (currentx+r, currenty, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 45:
			ctx.arc_negative (currentx + arcx, currenty + arcy, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 90:
			ctx.arc_negative (currentx, currenty+r, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 135:
			ctx.arc_negative (currentx - arcx, currenty + arcy, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 180:
			ctx.arc_negative (currentx-r, currenty, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 225:
			ctx.arc_negative (currentx -arcx, currenty-arcy, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 270:
			ctx.arc_negative (currentx, currenty-r, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 315:
			ctx.arc_negative (currentx + arcx, currenty - arcy, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		elif currdeg == 360:
			ctx.arc_negative (currentx, currenty, r, math.radians(currdeg-180), math.radians(currdeg-180-45))
		currdeg = currdeg - 45 
	elif t == 's':
		if currdeg == 0:
			ctx.line_to (currentx, currenty+r)
		elif currdeg == 45:
			ctx.line_to (currentx, currenty+r)
		elif currdeg == 90:
			ctx.line_to (currentx, currenty+r)
		elif currdeg == 135:
			ctx.line_to (currentx, currenty+r)
		elif currdeg == 180:
			ctx.line_to (currentx, currenty-r)
		elif currdeg == 225:
			ctx.line_to (currentx, currenty+r)
		elif currdeg == 270:
			ctx.line_to (currentx+r, currenty)
		elif currdeg == 315:
			ctx.line_to (currentx+math.sqrt(math.pow(r,2)/2), currenty+math.sqrt(math.pow(r,2)/2))
		elif currdeg == 360:
			ctx.line_to (currentx, currenty+r)

	currentx, currenty = ctx.get_current_point()

#  drawarc(4,True)
#  drawarc(1,False)
#  drawarc(3,True)
#  goforward(1)
#  drawarc(3,True)
#  drawarc(1,False)

#  drawarc(4,True)
#  goforward(2)
#  drawarc(3,True)
#  goforward(1)
#  drawarc(2,True)
#  drawarc(1,False)



if __name__ == "__main__":
	#pieces = "cr cr cr cr cr cr s s cl cl cl cl cl cl s s".split()
	#pieces = "cr cr cr cr cr cr s s cl cl cl cl cl cl s s".split()
	pieces = "cr cr cr cr cl cr cr cr s cr cr cr cl".split() # doesnt get back
	#pieces = "cr cr cr cr s s cr cr cr s cr cr cl".split() # doesnt get back
	#pieces = "c c c c c c c c ".split()
	#pieces = "c c c c s c c c c s".split()
	#pieces = "c c".split()
	print(pieces)
	if ctx.has_current_point():
		print("has current")
	else:
		print("has no current")
	ctx.move_to (0, starty)
	ctx.line_to (startx, starty)
	currentx, currenty = ctx.get_current_point()
	print('current: ',currentx,currenty,currdeg)
	x = 0.0
	for p in pieces:
		if x == 1.0:
			x = 0.0
		else:
			x = 1.0
		print('x: ', x)
		#ctx.save()
		ctx.set_source_rgb(0.0, x, x)
		print(p)
		add(p)
		#ctx.restore()
		print('current: ',currentx,currenty,currdeg)
	ctx.stroke ()
	surface.write_to_png ("example.png")
