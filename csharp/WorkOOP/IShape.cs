using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    /*
     * IShape – интерфейс, описывающий поведение фигур на плоскости.
     */
    internal interface IShape
    {
        /*
         * square – возвращает площадь фигуры.
         */
        public double square();

        /*
         * length – возвращает длину/периметр фигуры.
         */
        public double length();

        /*
         * shift – сдвиг фигуры на вектор заданный объектом класса Point2D (вектор от начала координат до указанной точки)
         */
        public IShape shift(Point2D a);

        /*
         * rot – поворот фигуры на угол phi в радианах относительно начала координат. Положительное направление – против часовой стрелки.
         */
        public IShape rot(double phi);

        /*
         * symAxis – симметрия точки относительно оси под заданным номером (0 – Ox, 1 – Oy, 2 – Oz, …).
         */
        public IShape symAxis(int i);

        /*
         * cross – проверяет пересекаются ли фигуры (true – пересекаются, false – нет).
         */
        public bool cross(IShape i);

        /*
         * toString?
         */
        public String toString();
    }
}
