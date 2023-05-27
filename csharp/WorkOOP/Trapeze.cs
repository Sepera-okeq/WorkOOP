using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    // Реализация класса Trapeze – трапеция.
    internal class Trapeze : QGon
    {
        /*
         * Trapeze – конструктор, описывающий инициализацию объекта. 
         * 
         * На вход принимает массив точек в порядке обхода по трапеции.
         */
        public Trapeze(Point2D[] p) : base(p) { }

        /*
         * Переопредение функции square под трапецию.
         */
        new public double square() => base.square();   
    }
}
