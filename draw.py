#!/usr/bin/env python3

import math
import cairo

class TrackBuilder():

	def __init__(self):
		self.r = 100.0
		self.WIDTH, self.HEIGHT = 10*self.r, 10*self.r
		self.startx = 5*self.r
		self.starty = 5*self.r
		self.currentx = 0.0
		self.currenty = 0.0
		self.currdeg = 0
		self.arcx = math.cos(math.radians(45)) * self.r
		self.arcy = math.sin(math.radians(45)) * self.r
		self.surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, int(self.WIDTH), int(self.HEIGHT))
		self.ctx = cairo.Context (self.surface)
		self.ctx.move_to (self.startx, self.starty)
		self.ctx.arc(self.startx, self.starty, 5, 0, 2*math.pi)
		self.ctx.set_source_rgb(0.3, 0.4, 0.6)
		self.ctx.fill()
		self.ctx.move_to (self.startx, self.starty)
		self.currentx, self.currenty = self.ctx.get_current_point()

	def buildit(self, pieces):
		for p in pieces:
			self.add(p)
		self.finish()

	def add(self,t):
		if t == 'cr':
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
			elif self.currdeg == 360:
				self.ctx.arc (self.currentx, self.currenty+self.r, self.r, math.radians(self.currdeg-90), math.radians(self.currdeg+45-90))

			if self.currdeg == 360:
				self.currdeg = 45
			else:
				self.currdeg = self.currdeg + 45

		if t == 'cl':
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
			elif self.currdeg == 360:
				self.ctx.arc_negative (self.currentx, self.currenty, self.r, math.radians(self.currdeg+90), math.radians(self.currdeg-45+90))

			if self.currdeg == 0:
				self.currdeg = 315
			else:
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
			elif self.currdeg == 360:
				self.ctx.line_to (self.currentx+self.r, self.currenty)

		self.currentx, self.currenty = self.ctx.get_current_point()

	def getCurrentPoint(self):
		return self.currentx, self.currenty

	def finish(self):
		self.ctx.stroke()
		self.surface.write_to_png ("example.png")
