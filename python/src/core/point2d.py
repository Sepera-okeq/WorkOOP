from core.point import Point

import math

class Point2D(Point):
	def __init__(self, *args):
		self.dim = 2
		if len(args) == 0:
			self.x = [0, 0]
		if len(args) == 1:
			self.x = args[0]

	def rot(point, phi, self = None):
		if self != None:
			result = Point(2, [0]*2)
			result.x[0] = round(self.x[0] * math.cos(phi) - self.x[1] * math.sin(phi), 2)
			result.x[1] = round(self.x[0] * math.sin(phi) + self.x[1] * math.cos(phi), 2)
			return result
		else:
			result = Point(2, [0]*2)
			result.x[0] = round(point.x[0] * math.cos(phi) - point.x[1] * math.sin(phi), 2)
			result.x[1] = round(point.x[0] * math.sin(phi) + point.x[1] * math.cos(phi), 2)
			return result