import math
import cairo

class TrackBuilder():

	def __init__(self, id):
		self.id = id
		self.r = 40.0
		self.WIDTH = 400; self.HEIGHT = 400 
		self.startx = self.WIDTH/2
		self.starty = self.HEIGHT/2
		self.currentx = 0.0
		self.currenty = 0.0
		self.currdeg = 270
		self.arcx = math.cos(math.radians(45)) * self.r
		self.arcy = math.sin(math.radians(45)) * self.r
		self.linewidth = 5
		self.surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, int(self.WIDTH), int(self.HEIGHT))
		self.ctx = cairo.Context (self.surface)
		self.ctx.move_to (self.startx, self.starty)
		self.currentx, self.currenty = self.ctx.get_current_point()
		self.initimage()

	def reset(self):
		pass

	def initimage(self):

		# draw a background
		def drawbackground(self):
			(x, y, z) = self.rgb(255,255,255)
			self.ctx.set_source_rgb(x, y, z)
			self.ctx.rectangle(0, 0, self.WIDTH, self.HEIGHT)
			self.ctx.fill()

		drawbackground(self)

		# draw a border 
		(x, y, z) = self.rgb(165, 165, 165)
		self.ctx.set_source_rgb(x, y, z)
		self.ctx.rectangle(0.0, 0.0, self.WIDTH, self.HEIGHT);
		self.ctx.stroke();

		# draw the id of the image
		self.ctx.move_to(5, 10)
		self.ctx.show_text(self.id)

		# draw point to represent starting point
		self.ctx.move_to (self.startx, self.starty)
		self.ctx.arc(self.startx, self.starty, 5, 0, 2*math.pi)
		self.ctx.set_source_rgb(0.3, 0.4, 0.6)
		self.ctx.fill()

		self.ctx.move_to (self.startx, self.starty)

	def rgb(self,x,y,z):
		return (x/255, y/255, z/255)

	def buildit(self, pieces):
		for p in pieces:
			self.add(p)

	def add(self,t):
		if t == 'cr':
			# new sub path required so arc doesn't close
			self.ctx.new_sub_path()
			if self.currdeg == 0:
				self.ctx.arc (self.currentx, self.currenty+self.r, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 45:
				self.ctx.arc (self.currentx - self.arcx, self.currenty + self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 90:
				self.ctx.arc (self.currentx - self.r, self.currenty, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 135:
				self.ctx.arc (self.currentx -self.arcx, self.currenty -self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 180:
				self.ctx.arc (self.currentx, self.currenty-self.r, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 225:
				self.ctx.arc (self.currentx+self.arcx, self.currenty-self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 270:
				self.ctx.arc (self.currentx+self.r, self.currenty, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 315:
				self.ctx.arc (self.currentx+self.arcx, self.currenty+self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))

			self.currdeg = self.currdeg + 45
			if self.currdeg == 360:
				self.currdeg = 0 

		if t == 'cl':
			# new sub path required so arc doesn't close
			self.ctx.new_sub_path()
			if self.currdeg == 0:
				self.ctx.arc_negative (self.currentx, self.currenty-self.r, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 45:
				self.ctx.arc_negative (self.currentx+self.arcx, self.currenty-self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 90:
				self.ctx.arc_negative (self.currentx+self.r, self.currenty, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 135:
				self.ctx.arc_negative (self.currentx+self.arcx, self.currenty+self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 180:
				self.ctx.arc_negative (self.currentx, self.currenty+self.r, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 225:
				self.ctx.arc_negative (self.currentx-self.arcx, self.currenty+self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 270:
				self.ctx.arc_negative (self.currentx-self.r, self.currenty, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 315:
				self.ctx.arc_negative (self.currentx-self.arcx, self.currenty-self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))

			if self.currdeg == 0:
				self.currdeg = 360
			self.currdeg = self.currdeg - 45

		elif t == 's':
			if self.currdeg == 0:
				self.ctx.line_to (self.currentx+self.r, self.currenty)
			elif self.currdeg == 45:
				self.ctx.line_to (self.currentx+math.sqrt(math.pow(self.r,2)/2), self.currenty+math.sqrt(math.pow(self.r,2)/2))
			elif self.currdeg == 90:
				self.ctx.line_to (self.currentx, self.currenty+self.r)
			elif self.currdeg == 135:
				self.ctx.line_to (self.currentx-math.sqrt(math.pow(self.r,2)/2), self.currenty+math.sqrt(math.pow(self.r,2)/2))
			elif self.currdeg == 180:
				self.ctx.line_to (self.currentx-self.r, self.currenty)
			elif self.currdeg == 225:
				self.ctx.line_to (self.currentx-math.sqrt(math.pow(self.r,2)/2), self.currenty-math.sqrt(math.pow(self.r,2)/2))
			elif self.currdeg == 270:
				self.ctx.line_to (self.currentx, self.currenty-self.r)
			elif self.currdeg == 315:
				self.ctx.line_to (self.currentx+math.sqrt(math.pow(self.r,2)/2), self.currenty-math.sqrt(math.pow(self.r,2)/2))

		self.currentx, self.currenty = self.ctx.get_current_point()

	def getCurrentPoint(self):
		return self.currentx, self.currenty

	def getCurrentDegree(self):
		return self.currdeg

	def createImage(self, id):
		self.ctx.stroke()
		# draw the id of the image
		self.ctx.move_to(5, 25)
		self.ctx.show_text(id)
		self.surface.write_to_png (str(id) + ".png")
