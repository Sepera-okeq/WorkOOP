from core.ngon import NGon
from core.point2d import Point2D

from math import sqrt

class TGon(NGon):
	def __init__(self, p):
		self.n = 3
		self.p = p

	def __str__(self):
		st = f"TGon: "
		for i in range(len(self.p)):
			st += f"{str(self.p[i])}, "
		st = st[:len(st)-2]
		return st

	def square(self):
		ab = Point2D.sub(self.p[1], self.p[0]).abs()
		bc = Point2D.sub(self.p[2], self.p[1]).abs()
		ca = Point2D.sub(self.p[0], self.p[2]).abs()
		pp = (ab + bc + ca)/2
		return sqrt(pp * (pp-ab) * (pp-bc) * (pp - ca))