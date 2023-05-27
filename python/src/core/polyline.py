from core.OpenFigure import OpenFigure
# from point import Point
# from point2d import Point2D
# from segment import Segment

class Polyline(OpenFigure):
	def __init__(self, n, p):
		self.n = n
		self.p = p

	def __str__(self):
		st = f"Polyline: size = {self.n}; "
		for i in range(len(self.p)):
			st += f"{str(self.p[i])}, "
		st = st[:len(st)-2]
		return st

	def getP(self, i = None):
		if i == None:
			return self.p
		else:
			return self.p[i]

	def setP(self, newP, i = None):
		if i == None:
			self.p = newP
		else:
			self.p[i] = newP

	def length(self):
		l = 0
		pprev = self.p[0]
		for point in self.p:
			l += Segment(pprev, point).length()
			pprev = point
		return l

	def shift(self, a):
		result = polyline(self.n, self.p)
		for ns in range(result.n):
			result.p[ns] = result.p[ns].add(a)
		return result

	def rot(self, phi):
		result = polyline(self.n, self.p)
		for ns in range(result.n):
			result.p[ns] = result.p[ns].rot(phi)
		return result

	def symAxis(self, i):
		if i < 0:
			raise Exception("Ошибка: отрицательное пространство")
		if self.p[0].dim < i:
			raise Exception("Ошибка: имеет пространство меньшее, чем нужное")
		result = Polyline(self.n, self.p)
		for ns in range(result.n):
			result.p[ns] = result.p[ns].symAxis(i)
		return result

	def cross(self, figure):
		pprev = self.p[0]
		for pt in self.p[1:]:
			if Segment(pprev, pt).cross(figure):
				return True
			pprev = pt
		return False