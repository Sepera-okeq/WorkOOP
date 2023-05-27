from core.ngon import NGon
from core.point2d import Point2D
from core.tgon import TGon

class QGon(NGon):
	def __init__(self, p):
		self.n = 4
		self.p = p

	def __str__(self):
		st = f"QGon: "
		for i in range(len(self.p)):
			st += f"{str(self.p[i])}, "
		st = st[:len(st)-2]
		return st

	def square(self):
		a = [self.p[0], self.p[1], self.p[2]]
		b = [self.p[2], self.p[3], self.p[0]]
		return TGon(a).square() + TGon(b).square()