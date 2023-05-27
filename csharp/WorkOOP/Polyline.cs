using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WorkOOP
{
    // Реализация класса Polyline – ломаная линия
    internal class Polyline: OpenFigure
    {
        protected int n;        // n – количество точек.
        protected Point2D[] p;  // p – массив двумерных точек.

        /*
         * Polyline – конструктор, описывающий инициализацию объекта.
         * 
         * На вход принимает массив точек в порядке обхода по ломаной.
         */
        public Polyline(Point2D[] p) {
            if (p.Length == 0)
                throw new Exception("No zero array polyline!!");
            n = p.Length;
            this.p = p; 
        }

        /*
         * Реализация всех функций из OpenFigure, кроме square() 
         */
        public int getN() => n;
        public Point2D[] getP() => p;
        public Point2D getP(int i) => p[i];
        public void setP(Point2D[] p) { this.p = p; n = p.Length; }
        public void setP(Point2D p, int i) => this.p[i] = p;

        public override double length() {
            double l = 0;
            Point2D prevp = p[0];
            foreach (Point2D point in p) { l += new Segment(prevp, point).length(); prevp = point; }
            return l;
        }

        public override Polyline shift(Point2D a) {
            foreach (Point2D e in p)
                e.add(a);
            return this; 
        }

        public override Polyline rot(double phi) {
            foreach (Point2D e in p)
                e.rot(phi);
            return this; 
        }

        public override Polyline symAxis(int i) {
            foreach (Point2D e in p)
                e.symAxis(i);
            return this; 
        }

        public override bool cross(IShape i) {
            Point2D prev = p[0];
            foreach (Point2D pt in p)
            {
                if (new Segment(prev, pt).cross(i))
                    return true;
                prev = pt;
            }
            return false;
        }

        public override String toString() { 
            StringBuilder sb = new StringBuilder(); sb.Append("Size: " + n + "\nPoints: [ ");
            foreach (Point2D e in p)
                sb.Append(e.toString() + " ");
            sb.Append(" ]");
            return sb.ToString();
        }
    }
}
