from math import sqrt
import math

class Point:
	def __init__(self, *args):
		if len(args) == 1:
			self.dim = args[0]
			self.x = [0]*args[0]
		if len(args) == 2:
			self.dim = args[0]
			self.x = args[1]

	def __str__(self):
		return f"{self.x}"

	def getDim(self):
		return self.dim

	def getX(self, i = None):
		if i != None:
			return self.x[i]
		else:
			return self.x

	def setX(self, newX, i = None):
		result = Point(self.dim, self.x)
		if i != None:
			if i > self.dim or i < 0:
				raise Exception("Ошибка: новый индекс за пределами существующей точки")

			result.x[i] = newX[i]
		else:
			result.x = newX
		return result

	def abs(self):
		sum = 0
		for i in self.x:
			sum += i * i
		return sqrt(sum)

	def add(point1, point2 = None, self = None):
		if self != None:
			if point1.dim != self.dim:
				raise Exception("Ошибка: не совпадают размерности точек")
			p1 = Point(self.dim, self.x)
			for i in range(p1.dim):
				p1.x[i] += point1.x[i]
			return p1
		else:
			if point1.dim != point2.dim:
				raise Exception("Ошибка: не совпадают размерности точек")

			pointRes = Point(point1.dim, [0]*point1.dim)
			for i in range(point1.dim):
				pointRes.x[i] = point1.x[i] + point2.x[i]
			return pointRes

	def sub(point1, point2 = None, self = None):
		if self != None:
			if point1.dim != self.dim:
				raise Exception("Ошибка: не совпадают размерности точек")
			p1 = Point(self.dim, self.x)
			for i in range(p1.dim):
				p1.x[i] -= point1.x[i]
			return p1
		else:
			if point1.dim != point2.dim:
				raise Exception("Ошибка: не совпадают размерности точек")

			pointRes = Point(point1.dim, [0]*point1.dim)
			for i in range(point1.dim):
				pointRes.x[i] = point1.x[i] - point2.x[i]
			return pointRes

	def mult(point, r, self = None):
		if isinstance(r, Point):
			if point.dim != r.dim:
				raise Exception("Ошибка: не совпадают размерности точек")

			result = 0
			for i in range(point.dim):
				result += point.x[i] * r.x[i]
			return result
		elif self != None:
			p1 = Point(self.dim, self.x)
			for i in range(self.dim):
				p1.x[i] *= r
			return p1
		else:
			for i in range(point.dim):
				point.x[i] *= r
			return point

	
	def symAxis(point, i, self = None):
		if i < 0:
			raise Exception("Ошибка: отрицательное пространство")
		if self != None:
			if self.dim < i:
				raise Exception("Ошибка: имеет пространство меньшее, чем нужное")
			p1 = Point(self.dim, self.x)
			newX = [0]*p1.dim
			for j in range(p1.dim):
				newX[j] = -p1.x[j]
			newX[i] = p1.x[i]
			return Point(p1.dim, newX)
		else:
			if point.dim < i:
				raise Exception("Ошибка: имеет пространство меньшее, чем нужное")
			newX = [0]*point.dim
			for j in range(point.dim):
				newX[j] = -point.x[j]
			newX[i] = point.x[i]
			return Point(point.dim, newX)

	def rot(point, phi, self = None):
		phi = phi
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