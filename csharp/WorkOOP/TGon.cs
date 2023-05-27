using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    // Реализация класса TGon – треугольник.
    internal class TGon : NGon
    {
        /*
         * TGon – конструктор, описывающий инициализацию объекта. 
         * 
         * На вход принимает массив точек в порядке обхода по треугольнику.
         */
        public TGon(Point2D[] p) : base(p) { }

        /*
         * Переопределение под треугольник функции square()
         */
        new public double square()
        {
            double ab = Point2D.sub(p[1], p[0]).abs(), 
                bc = Point2D.sub(p[2], p[1]).abs(),
                ca = Point2D.sub(p[0], p[2]).abs(),
                pp = (ab + bc + ca)/2;
            return Math.Sqrt(pp * (pp - ab)*(pp - bc)*(pp - ca));
        }
    }
}
