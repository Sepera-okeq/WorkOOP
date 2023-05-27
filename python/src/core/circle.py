from core.IShape import IShape
from core.point import Point
from core.point2d import Point2D

from math import pi

class Circle(IShape):
	def __init__(self, p, r):
		self.p = p
		self.r = r

	def __str__(self):
		return f"Circle: center: {self.p}; radius: {self.r}"

	def getR(self):
		return self.r

	def setR(self, newR):
		result = Circle(self.p, self.r)
		result.r = newR
		return result

	def getP(self):
		return self.p

	def setP(self, newP):
		result = Circle(self.p, self.r)
		result.p = newP
		return result

	def square(self):
		return pi * self.r * self.r

	def length(self):
		return 2 * pi * self.r

	def shift(self, point):
		result = Circle(self.p, self.r)
		result.p = result.p.add(point)
		return result

	def rot(self, phi):
		result = Circle(self.p, self.r)
		result.p = result.p.rot(phi)
		return result

	def symAxis(self, i):
		if i < 0:
			raise Exception("Ошибка: отрицательное пространство")
		if self.p.dim < i:
			raise Exception("Ошибка: имеет пространство меньшее, чем нужное")
		result = Circle(self.p, self.r)
		result.p = result.p.symAxis(i)
		return result

	def cross(self, figure):
		if figure.__class__.__name__ == "Circle":
			if Point2D.sub(self.getP(), figure.getP()).abs() <= self.getR() + figure.getR():
				return True
			else:
				return False
		return False