using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    // Реализация базового класса точки в N пространстве.
    internal class Point
    {

        protected int dim;          // Размерность пространства.
        protected double[] x;       // Массив координат размерности dim.

        /*
         * Конструктор, описывающий инициализацию объекта.
         * 
         * Одно целое число – размерность пространства. Создаёт начало координат в пространстве указанной размерности.
         * 
         * Параметры:
         * int dim
         */
        public Point(int dim)
        {
            this.dim = dim;
            x = new double[dim];
        }

        /*
         * Конструктор, описывающий инициализацию объекта.
         * 
         * Целое число и массив дробных чисел – создаёт точку в пространстве указанной размерности, значения координат берёт из массива дробных чисел.
         * 
         * Параметры:
         * int dim, double[] x
         */
        public Point(int dim, double[] x)
        {
            if(dim != x.Length)
                throw new Exception("Array Length != Dim size!");
            this.dim = dim;
            this.x = x;
        }

        /* 
         * Из методички:
         * 
         * Для каждого внутреннего параметра должен быть реализован get-метод.
         * Для каждого внутреннего параметра, кроме количества точек и размерности пространства, должен быть реализован set-метод.
         * 
         * TODO: переписать как свойства.
         */
        public int getDim() => dim;
        public double[] getX() => this.x;
        public void setX(double[] x) => this.x = x;
        public void setX(double x, int i) => this.x[i] = x;


        /*
         * Возвращает модуль точки (расстояние до начала координат).
         */
        public double abs() { 
            double sum = 0; 
            foreach (double i in x)
                sum += i * i; 
            return Math.Sqrt(sum); 
        }

        /*
         * (static) Cкладывает по координатам две точки.
         */
        public static Point add(Point a, Point b) {
            int dim = Convert.ToInt32(Math.Max(a.getDim(), b.getDim()));
            double[] x = new double[dim];
            for (int i = 0; i < dim; i++) { 
                if (i < a.dim) x[i] += a.x[i];
                if (i < b.dim) x[i] += b.x[i];
            }
            return new Point(dim, x);
        }

        /*
         * Cкладывает по координатам две точки.
         */
        public Point add(Point b) { 
            Point point = add(this, b);
            x = point.x;
            dim = point.dim;
            return point;
        }

        /*
         * (static) Находит разность по координатам двух точек.
         */
        public static Point sub(Point a, Point b)
        {
            int dim = Convert.ToInt32(Math.Max(a.getDim(), b.getDim()));
            double[] x = new double[dim];
            for (int i = 0; i < dim; i++)
            {
                if (i < a.dim)
                    x[i] += a.x[i];
                if (i < b.dim)
                    x[i] -= b.x[i];
            };
            return new Point(dim, x);
        }

        /*
         * Находит разность по координатам двух точек.
         */
        public Point sub(Point b)
        {            
            Point point = sub(this, b);
            x = point.x;
            dim = point.dim;
            return point;
        }

        /*
         * (static) Умножение точки на дробное число – произведение по координатам.
         */
        public static Point mult(Point a, double r)
        {
            double[] x = new double[a.dim];
            for (int i = 0; i < a.dim; i++)
                x[i] = r * a.x[i];
            return new Point(a.dim, x);
        }

        /*
         * Умножение точки на дробное число – произведение по координатам.
         */
        public Point mult(double r)
        {
            Point point = mult(this, r);
            x = point.x;
            dim = point.dim;
            return point;
        }

        /*
         * (static) Умножение точки на точку – скалярное произведение двух точек.
         */
        public static double mult(Point a, Point b) {
            double result = 0;
            for (int i = 0; i < Math.Min(a.x.Length, b.x.Length); i++)
                result += a.x[i] * b.x[i];
            return result;
        }

        /*
         * Умножение точки на точку – скалярное произведение двух точек.
         */
        public double mult(Point b) => mult(this, b);

        /*
         * (static) Cимметрия точки относительно оси под заданным номером.
         */
        public static Point symAxis(Point a, int i)
        {
            double[] x = new double[a.dim];
            for (int j = 0; j < a.dim; j++)
            {
                x[j] = -a.x[j];
            }
            x[i] = a.x[i];
            return new Point(a.dim, x);
        }

        /*
         * Cимметрия точки относительно оси под заданным номером.
         */
        public Point symAxis(int i)
        {
            Point point = symAxis(this, i);
            x = point.x;
            dim = point.dim;
            return point;
        }

        /*
         * Из методички:
         * Нужно переопределить toString для всех классов, в которых указан, чтобы выводил все внутренние параметры.
         */
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.Append("( ");
            foreach (double coord in x)
                sb.Append(coord.ToString() + " ");
            sb.Append(")");
            return sb.ToString();
        }
    }
}
