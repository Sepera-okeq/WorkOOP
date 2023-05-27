from core.IShape import IShape
from core.point2d import Point2D
from core.segment import Segment
from core.polyline import Polyline

class NGon(IShape):
	def __init__(self, p):
		self.p = p
		self.n = len(p)

	def __str__(self):
		st = f"NGon: {len(self.p)} points: "
		for i in range(len(self.p)):
			st += f"{str(self.p[i])}, "
		st = st[:len(st)-2]
		return st

	def getP(self):
		return self.p

	def setP(self, newP, i = None):
		result = NGon(self.p)
		if i == None:
			result.p = newP
		else:
			result.p[i] = newP

	def getN(self):
		return self.n

	def square(self):
		a = 0
		j = self.n - 1
		for i in range(self.n):
			a += (self.p[j].x[0] + self.p[i].x[0]) * (self.p[j].x[1] - self.p[i].x[1])
			j = i
		return abs(a/2.0)

	def length(self):
		l = 0
		pprev = self.p[0]
		for point in self.p:
			l += Segment(pprev, point).length()
			pprev = point
		l += Segment(self.p[0], self.p[self.getN() - 1]).length()
		return l

	def shift(self, point):
		result = NGon(self.p)
		for i in range(self.n):
			result.p[i] = result.p[i].add(point)
		return result

	def rot(self, phi):
		result = NGon(self.p)
		for i in range(self.n):
			result.p[i] = result.p[i].rot(phi)
		return result

	def symAxis(self, i):
		if i < 0:
			raise Exception("Ошибка: отрицательное пространство")
		if self.p[0].dim < i:
			raise Exception("Ошибка: имеет пространство меньшее, чем нужное")
		result = NGon(self.p)
		for j in range(self.n):
			result.p[i] = result.p[j].symAxis(i)
		return result

	def cross(self, figure):
		plln = Polyline(figure.n, figure.p)
		pprev = self.p[0]
		for pt in self.p[1:]:
			if Segment(pprev, pt).cross(plln):
				return True
			pprev = pt
		if Segment(self.p[0], self.p[self.n - 1]).cross(plln):
			return True
		return False