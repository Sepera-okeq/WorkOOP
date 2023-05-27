using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    // Реализация класса Point2D на основе Point – описывает точку на плоскости.
    internal class Point2D : Point
    {
        /*
         * Point2D – конструктор, описывающий инициализацию объекта.
         * 
         * Без аргументов – создаёт начало координат на плоскости.
         * 
         * Параметры:
         * None
         */
        public Point2D() : base(2) { }

        /*
         * Point2D – конструктор, описывающий инициализацию объекта.
         * 
         * Массив дробных чисел – создаёт точку на плоскости, значения координат берёт из массива дробных чисел.
         * 
         * Параметры:
         * double[] x
         */
        public Point2D(double[] x): base(2,x) {  }

        /*
         * (static) Функция поворота точки на угол phi в радианах относительно начала координат. Положительное направление – против часовой стрелки.
         */
        public static Point2D rot(Point2D p, double phi) => new Point2D(new double[2] { p.x[0] * Math.Cos(phi) - p.x[1] * Math.Sin(phi), p.x[0] * Math.Sin(phi) + p.x[1] * Math.Cos(phi)});

        /*
         * Функция поворота точки на угол phi в радианах относительно начала координат. Положительное направление – против часовой стрелки.
         */
        public Point2D rot(double phi)
        {
            Point2D point = rot(this, phi); 
            x = point.x;
            dim = point.dim;
            return point;
        }
    }
}
