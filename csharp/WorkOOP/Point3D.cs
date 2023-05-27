using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    // Реализация класса Point3D – описывает точку в 3-мерном пространстве.
    internal class Point3D : Point
    {
        /*
         * Point3D – конструктор, описывающий инициализацию объекта.
         * 
         * Без аргументов – создаёт начало координат на плоскости.
         * 
         * Параметры:
         * None
         */
        public Point3D() : base(3) { }

        /*
         * Point3D – конструктор, описывающий инициализацию объекта.
         * 
         * Массив дробных чисел – создаёт точку на плоскости, значения координат берёт из массива дробных чисел.
         * 
         * Параметры:
         * double[] x
         */
        public Point3D(double[] x) : base(3, x) { }


        /*
         * (static) cross_prod – векторное произведение двух точек.
         */
        public static Point3D cross_prod(Point3D p1, Point3D p2) => new Point3D(new double[3]
            {p1.x[1] * p2.x[2] - p1.x[2] * p2.x[1],
            p1.x[2] * p2.x[0] - p1.x[0] * p2.x[2],
            p1.x[0] * p2.x[1] - p1.x[1] * p2.x[0]}
        );

        /*
         * cross_prod – векторное произведение двух точек.
         */
        public Point3D cross_prod(Point3D p)
        {
            Point3D point = cross_prod(this, p);
            x = point.x;
            dim = point.dim;
            return point;
        }

        /*
         * (static) mix_prod – смешанное произведение трёх точек.
         * 
         * (a*[b x c])
         */
        public static double mix_prod(Point3D p1, Point3D p2, Point3D p3) => mult(p1, cross_prod(p2, p3));


        /*
         * mix_prod – смешанное произведение трёх точек.
         * 
         * (a*[b x c])
         */
        public double mix_prod(Point3D p1, Point3D p2) => mix_prod(this, p1, p2);

    }
}
