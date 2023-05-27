using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    // Реализация класса Rectangle – прямоугольник.
    internal class Rectangle: QGon
    {
        /*
         * Rectangle – конструктор, описывающий инициализацию объекта. 
         * 
         * На вход принимает массив точек в порядке обхода по прямоугольнику.
         */
        public Rectangle(Point2D[] p) : base(p) { }

        /*
         * Переопределение под прямоугольник функции square()
         */
        new public double square() => Point2D.sub(p[1], p[0]).abs() * Point2D.sub(p[2], p[1]).abs();
    }
}
