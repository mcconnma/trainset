

#include <cmath>
#include <string>
#include "cairo.h"

#define degtorad(angleDegrees) (angleDegrees * M_PI / 180.0)
#define radtodeg(angleRadians) (angleRadians * 180.0 / M_PI)

class TrackBuilder {

public:

	float getCurrentX() { return currentx; }
	float getCurrentY() { return  currenty; }
	int getCurrentDegree() { return  currdeg; }

/*
	void createImage (int imageid) {
		init(path)
		initimage()
		buildit(path)
		ctx.stroke()

		# draw the id of the image
		ctx.move_to(5, 25)
		ctx.show_text(imageid)
		surface.write_to_png (imageid + ".png")
*/

protected:

	void init(std::string path) {
		//path = path;
		//surface = cairo_image_surface_create (FORMAT_ARGB32, WIDTH, HEIGHT);
		//ctx = cairo.Context (surface)
		//ctx.move_to (startx, starty)
		//currentx = ctx.get_current_point()
	}

private:
	std::string path;
	float r = 40.0;
	const int WIDTH = 400;
	const int HEIGHT = 400;
	float startx = WIDTH/2;
	float starty = HEIGHT/2;
	float currentx = 0.0;
	float currenty = 0.0;
	int currdeg = 270;
	float arcx = cos(degtorad(45)) * r;
	float arcy = sin(degtorad(45)) * r;
	int linewidth = 5;
	cairo_surface_t *surface;

};


/*

	def initimage(:

		# draw a background
		(x, y, z) = rgb(255,255,255)
		ctx.set_source_rgb(x, y, z)
		ctx.rectangle(0, 0, WIDTH, HEIGHT)
		ctx.fill()

		# draw a border 
		(x, y, z) = rgb(165, 165, 165)
		ctx.set_source_rgb(x, y, z)
		ctx.rectangle(0.0, 0.0, WIDTH, HEIGHT);
		ctx.stroke();

		# draw the path of the image
		ctx.move_to(5, 10)
		ctx.show_text(str(path))

		# draw point to represent starting point
		ctx.move_to (startx, starty)
		ctx.arc(startx, starty, 5, 0, 2*math.pi)
		ctx.set_source_rgb(0.3, 0.4, 0.6)
		ctx.fill()

		ctx.move_to (startx, starty)

	def rgb(x,y,z):
		return (x/255, y/255, z/255)

	def buildit( pieces):
		for p in pieces:
			add(p)

	def add(t):
		if t == 'cr':
			# new sub path required so arc doesn't close
			ctx.new_sub_path()
			if currdeg == 0:
				ctx.arc (currentx, currenty+r, r, math.radians(currdeg-90), math.radians(currdeg+45-90))
			elif currdeg == 45:
				ctx.arc (currentx - arcx, currenty + arcy, r, math.radians(currdeg-90), math.radians(currdeg+45-90))
			elif currdeg == 90:
				ctx.arc (currentx - r, currenty, r, math.radians(currdeg-90), math.radians(currdeg+45-90))
			elif currdeg == 135:
				ctx.arc (currentx -arcx, currenty -arcy, r, math.radians(currdeg-90), math.radians(currdeg+45-90))
			elif currdeg == 180:
				ctx.arc (currentx, currenty-r, r, math.radians(currdeg-90), math.radians(currdeg+45-90))
			elif currdeg == 225:
				ctx.arc (currentx+arcx, currenty-arcy, r, math.radians(currdeg-90), math.radians(currdeg+45-90))
			elif currdeg == 270:
				ctx.arc (currentx+r, currenty, r, math.radians(currdeg-90), math.radians(currdeg+45-90))
			elif currdeg == 315:
				ctx.arc (currentx+arcx, currenty+arcy, r, math.radians(currdeg-90), math.radians(currdeg+45-90))

			currdeg = currdeg + 45
			if currdeg == 360:
				currdeg = 0 

		if t == 'cl':
			# new sub path required so arc doesn't close
			ctx.new_sub_path()
			if currdeg == 0:
				ctx.arc_negative (currentx, currenty-r, r, math.radians(currdeg+90), math.radians(currdeg-45+90))
			elif currdeg == 45:
				ctx.arc_negative (currentx+arcx, currenty-arcy, r, math.radians(currdeg+90), math.radians(currdeg-45+90))
			elif currdeg == 90:
				ctx.arc_negative (currentx+r, currenty, r, math.radians(currdeg+90), math.radians(currdeg-45+90))
			elif currdeg == 135:
				ctx.arc_negative (currentx+arcx, currenty+arcy, r, math.radians(currdeg+90), math.radians(currdeg-45+90))
			elif currdeg == 180:
				ctx.arc_negative (currentx, currenty+r, r, math.radians(currdeg+90), math.radians(currdeg-45+90))
			elif currdeg == 225:
				ctx.arc_negative (currentx-arcx, currenty+arcy, r, math.radians(currdeg+90), math.radians(currdeg-45+90))
			elif currdeg == 270:
				ctx.arc_negative (currentx-r, currenty, r, math.radians(currdeg+90), math.radians(currdeg-45+90))
			elif currdeg == 315:
				ctx.arc_negative (currentx-arcx, currenty-arcy, r, math.radians(currdeg+90), math.radians(currdeg-45+90))

			if currdeg == 0:
				currdeg = 360
			currdeg = currdeg - 45

		elif t == 's':
			if currdeg == 0:
				ctx.line_to (currentx+r, currenty)
			elif currdeg == 45:
				ctx.line_to (currentx+math.sqrt(math.pow(r,2)/2), currenty+math.sqrt(math.pow(r,2)/2))
			elif currdeg == 90:
				ctx.line_to (currentx, currenty+r)
			elif currdeg == 135:
				ctx.line_to (currentx-math.sqrt(math.pow(r,2)/2), currenty+math.sqrt(math.pow(r,2)/2))
			elif currdeg == 180:
				ctx.line_to (currentx-r, currenty)
			elif currdeg == 225:
				ctx.line_to (currentx-math.sqrt(math.pow(r,2)/2), currenty-math.sqrt(math.pow(r,2)/2))
			elif currdeg == 270:
				ctx.line_to (currentx, currenty-r)
			elif currdeg == 315:
				ctx.line_to (currentx+math.sqrt(math.pow(r,2)/2), currenty-math.sqrt(math.pow(r,2)/2))

		currentx, currenty = ctx.get_current_point()

*/
