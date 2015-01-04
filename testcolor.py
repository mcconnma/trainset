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
	x = 0.5
	ctx.set_source_rgb(0.0, 0.0, 0.0)
	ctx.move_to (0, starty)
	ctx.line_to (startx, starty)
	currentx, currenty = ctx.get_current_point()
	print('current: ',currentx,currenty,currdeg)
	ctx.stroke_preserve()

	#ctx.move_to (currentx, currenty)
	ctx.set_source_rgb(1, 0, 0)
	ctx.line_to (startx, 0)
	currentx, currenty = ctx.get_current_point()
	print('current: ',currentx,currenty,currdeg)
	ctx.stroke ()
	surface.write_to_png ("example.png")
