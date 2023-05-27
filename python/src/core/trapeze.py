from core.qgon import QGon
from core.point2d import Point2D

class Trapeze(QGon):
	def __init__(self, p):
		self.n = 4
		self.p = p

	def __str__(self):
		st = f"Trapeze: "
		for i in range(len(self.p)):
			st += f"{str(self.p[i])}, "
		st = st[:len(st)-2]
		return st

	def square(self):
		return QGon(self.p).square()