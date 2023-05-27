from point import Point
from point2d import Point2D
from circle import Circle
from segment import Segment
from polyline import Polyline
from ngon import NGon
from tgon import TGon
from qgon import QGon
from rectangle import Rectangle
from trapeze import Trapeze

n = int(input("Введите количество фигур: "))
figures = [""]*n
figures2 = [""]*n
figures3 = [""]*n
for i in range(n):
	print(f"Ввод фигуры {i+1}/{n}:")
	typeF = input("Класс фигуры: ")

	if typeF == "Circle":
		x = float(input("Координата x центра круга: "))
		y = float(input("Координата y центра круга: "))
		p = Point2D([x, y])
		r = float(input("Радиус круга: "))
		figures[i] = Circle(p, r)

	if typeF == "Segment":
		stX = float(input("Координата x начала отрезка: "))
		stY = float(input("Координата y начала отрезка: "))
		st = Point2D([stX, stY])
		fiX = float(input("Координата x конца отрезка: "))
		fiY = float(input("Координата y конца отрезка: "))
		fi = Point2D([fiX, fiY])
		figures[i] = Segment(st, fi)

	if typeF == "Polyline":
		leN = int(input("Введите количество точек: "))
		p = [0]*leN
		for j in range(leN):
			x = float(input(f"Координата x {j+1}/{leN} точки: "))
			y = float(input(f"Координата y {j+1}/{leN} точки: "))
			p[j] = Point2D([x, y])
		figures[i] = Polyline(leN, p)

	if typeF == "NGon":
		leN = int(input("Введите количество точек: "))
		p = [0]*leN
		for j in range(leN):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures[i] = NGon(p)

	if typeF == "TGon":
		p = [0]*3
		for j in range(3):
			x = float(input(f"Координата x {j+1}/{3} точки: "))
			y = float(input(f"Координата y {j+1}/{3} точки: "))
			p[j] = Point2D([x, y])
		figures[i] = TGon(p)

	if typeF == "QGon":
		p = [0]*4
		for j in range(4):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures[i] = QGon(p)

	if typeF == "Rectangle":
		p = [0]*4
		for j in range(4):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures[i] = Rectangle(p)

	if typeF == "Trapeze":
		p = [0]*4
		for j in range(4):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures[i] = Trapeze(p)

sq = 0
ln = 0
for i in range(n):
	sq += figures[i].square()
	ln += figures[i].length()
	print(f"\nФигура {i+1}. Площадь: {figures[i].square()}, длина: {figures[i].length()}")

print(f"\nСуммарная площадь: {sq}")
print(f"Суммарная длина: {ln}")
print(f"Средняя площадь: {sq/n}\n")

for i in range(n):
	typeF = figures[i].__class__.__name__

	if typeF == "Circle":
		x = float(input("Координата x центра круга: "))
		y = float(input("Координата y центра круга: "))
		p = Point2D([x, y])
		r = float(input("Радиус круга: "))
		figures2[i] = Circle(p, r)

	if typeF == "Segment":
		stX = float(input("Координата x начала отрезка: "))
		stY = float(input("Координата y начала отрезка: "))
		st = Point2D([stX, stY])
		fiX = float(input("Координата x конца отрезка: "))
		fiY = float(input("Координата y конца отрезка: "))
		fi = Point2D([fiX, fiY])
		figures2[i] = Segment(st, fi)

	if typeF == "Polyline":
		leN = int(input("Введите количество точек: "))
		p = [0]*leN
		for j in range(leN):
			x = float(input(f"Координата x {j+1}/{leN} точки: "))
			y = float(input(f"Координата y {j+1}/{leN} точки: "))
			p[j] = Point2D([x, y])
		figures2[i] = Polyline(leN, p)

	if typeF == "NGon":
		leN = int(input("Введите количество точек: "))
		p = [0]*leN
		for j in range(leN):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures2[i] = NGon(p)

	if typeF == "TGon":
		p = [0]*3
		for j in range(3):
			x = float(input(f"Координата x {j+1}/{3} точки: "))
			y = float(input(f"Координата y {j+1}/{3} точки: "))
			p[j] = Point2D([x, y])	
		figures2[i] = TGon(p)

	if typeF == "QGon":
		p = [0]*4
		for j in range(4):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures2[i] = QGon(p)

	if typeF == "Rectangle":
		p = [0]*4
		for j in range(4):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures2[i] = Rectangle(p)

	if typeF == "Trapeze":
		p = [0]*4
		for j in range(4):
			x = float(input(f"Координата x {j+1}/{4} точки: "))
			y = float(input(f"Координата y {j+1}/{4} точки: "))
			p[j] = Point2D([x, y])
		figures2[i] = Trapeze(p)

print("\n\nПроверка 1:")
for i in range(n):
	if figures[i].cross(figures2[i]):
		print(f"Фигуры {i+1} пересекаются")
	else:
		print(f"Фигуры {i+1} НЕ пересекаются")

for i in range(n):

	move = input(f"\nКакое действие совершить с фигурой {i+1}: ")

	if move == "Shift":
		shX = float(input("Сдвиг по X: "))
		shY = float(input("Сдвиг по Y: "))
		sh = Point2D([shX, shY])
		figures3[i] = figures2[i].shift(sh)

	if move == "Rot":
		ph = float(input("Угол поворота: "))
		figures3[i] = figures2[i].rot(ph)

	if move == "SymAxis":
		ind = int(input("Симметрия относительно оси: "))
		figures3[i] = figures2[i].symAxis(ind)

print("\n\nПроверка 2:")
for i in range(n):
	if figures[i].cross(figures3[i]):
		print(f"Фигуры {i+1} пересекаются")
	else:
		print(f"Фигуры {i+1} НЕ пересекаются")