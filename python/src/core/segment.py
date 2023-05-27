from core.OpenFigure import OpenFigure
from core.point import Point
from core.point2d import Point2D

class Segment(OpenFigure):
	def __init__(self, point1, point2):
		self.start = point1
		self.finish = point2

	def __str__(self):
		return "Segment: start = {0}; finish = {1}.".format(self.start, self.finish)

	def getStart(self):
		return self.start

	def getFinish(self):
		return self.finish

	def setStart(self, newStart):
		result = Segment(self.start, self.finish)
		result.start = newStart
		return result

	def setFinish(self, newFinish):
		result = Segment(self.start, self.finish)
		result.start = newFinish
		return result

	def length(self):
		return Point.abs(Point2D.sub(self.finish, self.start))

	def shift(self, point):
		result = Segment(self.start, self.finish)
		result.start = result.start.add(point)
		result.finish = result.finish.add(point)
		return result

	def rot(self, phi):
		result = Segment(self.start, self.finish)
		result.start = result.start.rot(phi)
		result.finish = result.finish.rot(phi)
		return result

	def symAxis(self, i):
		if i < 0:
			raise Exception("Ошибка: отрицательное пространство")
		if self.start.dim < i:
			raise Exception("Ошибка: имеет пространство меньшее, чем нужное")
		result = Segment(self.start, self.finish)
		result.start = result.start.symAxis(i)
		result.finish = result.finish.symAxis(i)
		return result

	def intersectSeg(seg1, seg2):
		a = seg1.start
		b = seg1.finish
		c = seg2.start
		d = seg2.finish
		def ccw(a, b, c):
			return (c.getX(1) - a.getX(1)) * (b.getX(0) - a.getX(0)) > (b.getX(1) - a.getX(1)) * (c.getX(0) - a.getX(0))
		return ccw(a, c, d) != ccw(b, c, d) and ccw(a, b, c) != ccw(a, b, d)

	def intersectCir(seg, cir):
		return Point2D.sub(seg.start, cir.getP()).abs() < cir.getR() or Point2D.sub(seg.finish, cir.getP()).abs() < cir.getR()

	def cross(self, figure):
		if figure.__class__.__name__ == "Segment":
			return Segment.intersectSeg(self, figure)
		elif figure.__class__.__name__ == "Circle":
			return Segment.intersectCir(self, figure)
		elif figure.__class__.__name__ == "Polyline":
			pprev = figure.p[0]
			for point in figure.p[1:]:
				seg = Segment(pprev, point)
				if self.cross(seg):
					return True
				pprev = point
			return False