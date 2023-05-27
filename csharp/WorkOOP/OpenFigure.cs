using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    /*
     *  Реализация абстрактного класса OpenFigure – класс незамкнутых фигур.
     */
    internal abstract class OpenFigure: IShape
    {
        /*
         * Стандартная реализация функции square из интерфейса.
         */
        public double square() => 0;
        public abstract double length();
        public abstract IShape shift(Point2D a);
        public abstract IShape rot(double phi);
        public abstract IShape symAxis(int i);
        public abstract bool cross(IShape i);
        public abstract String toString();
    }
}
