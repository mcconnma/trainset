import math
import cairo

NUM_CL = 6
NUM_CR = 6
NUM_S = 4


class TrackBuilder(object):

	#__slots__ = ['path', 'surface', 'ctx', 'currentx', 'currenty']

	def __init__(self, path):

		self.r = 40.0
		self.WIDTH = 400
		self.HEIGHT = 400
		self.startx = self.WIDTH/2
		self.starty = self.HEIGHT/2
		self.currentx = 0.0
		self.currenty = 0.0
		self.currdeg = 270
		self.arcx = math.cos(math.radians(45)) * self.r
		self.arcy = math.sin(math.radians(45)) * self.r
		self.linewidth = 5


	def set_path(self, path):
		# setup cairo drawing surface
		self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, int(self.WIDTH), int(self.HEIGHT))
		self.ctx = cairo.Context(self.surface)
		self.ctx.move_to(self.startx, self.starty)
		self.path = path

	def is_valid_path(self):

		assert self.path is not None

		t1 = True
		# check for valid use of 's'
		if self.path.count('s') >= 3:
			l2 = ''.join(self.path * 2)
			if l2.find('ss') == -1:
				t1 = False
		# the curves are reversible so we need to check that number <= cl + cr
		t2 = (self.path.count('cl') + self.path.count('cr') <= NUM_CL + NUM_CR) and self.path.count('s') <= NUM_S
		return t1 and t2

	def did_complete(self):
		end_point = self.getCurrentPoint()
		end_deg = self.getCurrentDegree()
		return self.start_point == end_point and self.start_deg == end_deg


	def buildit(self):
		assert self.path is not None
		for p in self.path:
			self.add(p)

	def add(self, t):
		if t == 'cr':
			# new sub path required so arc doesn't close
			self.ctx.new_sub_path()
			if self.currdeg == 0:
				self.ctx.arc(self.currentx, self.currenty+self.r, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 45:
				self.ctx.arc(self.currentx - self.arcx, self.currenty + self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 90:
				self.ctx.arc(self.currentx - self.r, self.currenty, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 135:
				self.ctx.arc(self.currentx - self.arcx, self.currenty - self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 180:
				self.ctx.arc(self.currentx, self.currenty-self.r, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 225:
				self.ctx.arc(self.currentx+self.arcx, self.currenty-self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 270:
				self.ctx.arc(self.currentx+self.r, self.currenty, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))
			elif self.currdeg == 315:
				self.ctx.arc(self.currentx+self.arcx, self.currenty+self.arcy, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))

			self.currdeg = self.currdeg + 45
			if self.currdeg == 360:
				self.currdeg = 0 

		if t == 'cl':
			# new sub path required so arc doesn't close
			self.ctx.new_sub_path()
			if self.currdeg == 0:
				self.ctx.arc_negative(self.currentx, self.currenty-self.r, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 45:
				self.ctx.arc_negative(self.currentx+self.arcx, self.currenty-self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 90:
				self.ctx.arc_negative(self.currentx+self.r, self.currenty, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 135:
				self.ctx.arc_negative(self.currentx+self.arcx, self.currenty+self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 180:
				self.ctx.arc_negative(self.currentx, self.currenty+self.r, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 225:
				self.ctx.arc_negative(self.currentx-self.arcx, self.currenty+self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 270:
				self.ctx.arc_negative(self.currentx-self.r, self.currenty, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))
			elif self.currdeg == 315:
				self.ctx.arc_negative(self.currentx-self.arcx, self.currenty-self.arcy, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))

			if self.currdeg == 0:
				self.currdeg = 360
			self.currdeg = self.currdeg - 45

		elif t == 's':
			if self.currdeg == 0:
				self.ctx.line_to(self.currentx+self.r, self.currenty)
			elif self.currdeg == 45:
				self.ctx.line_to(self.currentx+math.sqrt(math.pow(self.r, 2)/2), self.currenty+math.sqrt(math.pow(self.r, 2)/2))
			elif self.currdeg == 90:
				self.ctx.line_to(self.currentx, self.currenty+self.r)
			elif self.currdeg == 135:
				self.ctx.line_to(self.currentx-math.sqrt(math.pow(self.r, 2)/2), self.currenty+math.sqrt(math.pow(self.r, 2)/2))
			elif self.currdeg == 180:
				self.ctx.line_to(self.currentx-self.r, self.currenty)
			elif self.currdeg == 225:
				self.ctx.line_to(self.currentx-math.sqrt(math.pow(self.r, 2)/2), self.currenty-math.sqrt(math.pow(self.r, 2)/2))
			elif self.currdeg == 270:
				self.ctx.line_to(self.currentx, self.currenty-self.r)
			elif self.currdeg == 315:
				self.ctx.line_to(self.currentx+math.sqrt(math.pow(self.r, 2)/2), self.currenty-math.sqrt(math.pow(self.r, 2)/2))

		self.currentx, self.currenty = self.ctx.get_current_point()

	def getCurrentPoint(self):
		return self.currentx, self.currenty

	def getCurrentDegree(self):
		return self.currdeg


	def initimage(self):

		# draw a background
		(x, y, z) = self.rgb(255, 255, 255)
		self.ctx.set_source_rgb(x, y, z)
		self.ctx.rectangle(0, 0, self.WIDTH, self.HEIGHT)
		self.ctx.fill()

		# draw a border
		(x, y, z) = self.rgb(165, 165, 165)
		self.ctx.set_source_rgb(x, y, z)
		self.ctx.rectangle(0.0, 0.0, self.WIDTH, self.HEIGHT)
		self.ctx.stroke()

		# draw the path of the image
		self.ctx.move_to(5, 10)
		self.ctx.show_text(str(self.path))

		# draw point to represent starting point
		self.ctx.move_to(self.startx, self.starty)
		self.ctx.arc(self.startx, self.starty, 5, 0, 2*math.pi)
		self.ctx.set_source_rgb(0.3, 0.4, 0.6)
		self.ctx.fill()

		self.ctx.move_to(self.startx, self.starty)

	def rgb(self, x, y, z):
		return x/255, y/255, z/255

	def createImage(self, imageid):

		self.initimage()
		self.buildit()
		self.ctx.stroke()

		# draw the id of the image
		self.ctx.move_to(5, 25)
		self.ctx.show_text(imageid)
		self.surface.write_to_png(imageid + ".png")
