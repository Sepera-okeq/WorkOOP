from point import Point

import math

class Point3D(Point):
	def __init__(self, *args):
		self.dim = 3
		if len(args) == 0:
			self.x = [0, 0, 0]
		if len(args) == 1:
			self.x = args[0]

	def cross_prod(point1, point2 = None, self = None):
		if self != None:
			result = Point(3, [0]*3)
			result.x[0] = self.x[1] * point1.x[2] - self.x[2] * point1.x[1]
			result.x[1] = self.x[2] * point1.x[0] - self.x[0] * point1.x[2]
			result.x[1] = self.x[0] * point1.x[1] - self.x[1] * point1.x[0]
			return result
		else:
			result = Point(3, [0]*3)
			result.x[0] = point1.x[1] * point2.x[2] - point1.x[2] * point2.x[1]
			result.x[1] = point1.x[2] * point2.x[0] - point1.x[0] * point2.x[2]
			result.x[2] = point1.x[0] * point2.x[1] - point1.x[1] * point2.x[0]
			return result

	def mix_prod(point1, point2, point3, self = None):
		if self != None:
			result = self.x[0] * (point1.x[1] * point2.x[2] - point2.x[1] * point1.x[2]) + self.x[1] * (point1.x[2] * point2.x[0] - point2.x[2] * point1.x[0]) + self.x[2] * (point1.x[0] * point2.x[1] - point2.x[0] * point1.x[1])
		else:
			result = point1.x[0] * (point2.x[1] * point3.x[2] - point3.x[1] * point2.x[2]) + point1.x[1] * (point2.x[2] * point3.x[0] - point3.x[2] * point2.x[0]) + point1.x[2] * (point2.x[0] * point3.x[1] - point3.x[0] * point2.x[1])
		return result

p1 = Point3D([1, 1, -2])
p2 = Point3D([2, 2, 3])
p3 = Point3D([2, 3, 1])

print(Point3D.mix_prod(p1, p2, p3))