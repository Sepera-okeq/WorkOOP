using WorkOOP;
using System.Runtime.ExceptionServices;

// Функция создания массива точек
Point2D[] createPointArray(int numberOfPoints)
{
    Point2D[] p = new Point2D[numberOfPoints];
    for (int j = 0; j < numberOfPoints; j++)
    {
        double[] xy = new double[2];
        Console.WriteLine((j + 1).ToString() + " point. Coordinate X:");
        xy[0] = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine((j + 1).ToString() + " point. Coordinate Y:");
        xy[1] = Convert.ToDouble(Console.ReadLine());
        p[j] = new Point2D(xy);   
    }
    return p;
}

// Функция выбора типа фигуры
IShape newShape(string type) {
    IShape shape;
    if (type == "polyline")
    {
        Console.WriteLine("Number of points: ");
        int numberOfPoints = Convert.ToInt32(Console.ReadLine());
        shape = new Polyline(createPointArray(numberOfPoints));
    }
    else if (type == "ngon")
    {
        Console.WriteLine("Number of points: ");
        int numberOfPoints = Convert.ToInt32(Console.ReadLine());
        shape = new NGon(createPointArray(numberOfPoints));
    }
    else if (type == "qgon")
    {
        shape = new QGon(createPointArray(4));
    }
    else if (type == "tgon")
    {
        shape = new TGon(createPointArray(3));
    }
    else if (type == "trapeze")
    {
        shape = new Trapeze(createPointArray(4));
    }
    else if (type == "rectangle")
    {
        shape = new Rectangle(createPointArray(4));
    }
    else if (type == "segment")
    {
        double[] start = new double[2];
        Console.WriteLine("Start X coordinate: ");
        start[0] = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Start Y coordinate: ");
        start[1] = Convert.ToDouble(Console.ReadLine());
        double[] finish = new double[2];
        Console.WriteLine("Finish X coordinate: ");
        finish[0] = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Finish Y coordinate: ");
        finish[1] = Convert.ToDouble(Console.ReadLine());
        shape = new Segment(new Point2D(start), new Point2D(finish));
    }
    else if (type == "circle")
    {
        double[] center = new double[2];
        Console.WriteLine("Center X coordinate: ");
        center[0] = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Center Y coordinate: ");
        center[1] = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Radius: ");
        double radius = Convert.ToDouble(Console.ReadLine());
        shape = new Circle(new Point2D(center), radius);
    }
    else throw new Exception("Inexistent shape type");
    return shape;
}



// Создать переменную типа List<IShape>.
List<IShape> figures = new List<IShape>();

// Ввести количество фигур.
Console.WriteLine("Number of Shapes: ");
int numberOfShapes = Convert.ToInt32(Console.ReadLine());

/* Для каждой фигуры:
*  a.Ввести её тип (окружность, треугольник, отрезок, …).
*  b.Ввести все её параметры (точки, радиус, …).
*  c.Сохранить в списке.
*/

for (int i = 0; i < numberOfShapes; i++)
{
    Console.WriteLine((i + 1).ToString() + " Shape type: ");
    string type = Console.ReadLine().ToLower();
    figures.Add(newShape(type));
}
figures.ForEach(f => { Console.WriteLine(f.toString()); });

/*
 * Вывести на экран:
 * a. Суммарная площадь всех фигур.
 * b. Суммарная длина всех фигур.
 * c. Средняя площадь по всем фигурам.
*/
double totalSquare = 0, totalLength = 0;
figures.ForEach(f => { totalLength += f.length(); totalSquare += f.square(); });
Console.WriteLine("Total square of shapes: " + totalSquare);
Console.WriteLine("Total length of shapes: " + totalLength);
Console.WriteLine("Average square of a shape: " + totalSquare / numberOfShapes);

/*
 * Второй цикл размером по количеству фигур:
 * a. Создаёте новую фигуру:
 * i. Тип вводимой фигуры соответствует типу фигуры из списка под тем же номером.
 * ii. Ввести все её параметры (точки, радиус, …).
 * b. Вывести пересекаются ли введённая фигура с фигурой из списка.
 * c. Определить движение введённой фигуры:
 * i. Ввести тип движения (поворот, сдвиг, симметрия).
 * ii. Ввести параметры движения (угол, вектор, …).
 * d. Вывести пересекаются ли введённая фигура с фигурой из списка.
*/
Console.WriteLine("Input ugly twins for preceding shapes. ");
for (int i = 0; i < numberOfShapes; i++)
{ 
    Type t = figures[i].GetType();
    Console.WriteLine((i + 1).ToString() + " Shape type: " + t);
    IShape shape = null;    
    if (t == typeof(Segment)) shape = newShape("segment");
    else if (t == typeof(Polyline)) shape = newShape("polyline");
    else if (t == typeof(Circle)) shape = newShape("circle");
    else if (t == typeof(NGon)) shape = newShape("ngon");
    else if (t == typeof(QGon)) shape = newShape("qgon");
    else if (t == typeof(TGon)) shape = newShape("tgon");
    else if (t == typeof(Trapeze)) shape = newShape("trapeze");
    else if (t == typeof(Rectangle)) shape = newShape("rectangle");
    Console.WriteLine("Does the shape cross figure with the same index?");
    if (shape.cross(figures[i])) Console.WriteLine("YES");
    else Console.WriteLine("NO");
    Console.WriteLine("Now its time to skrew these shapes. ");
    Console.WriteLine("Movement type: ");
    string movementType = Console.ReadLine().ToLower();
    if (movementType == "shift")
    {
        double[] movementVector = new double[2];
        Console.WriteLine("Shift vector X coordinate: ");
        movementVector[0] = Convert.ToDouble(Console.ReadLine());
        Console.WriteLine("Shift vector Y coordinate: ");
        movementVector[1] = Convert.ToDouble(Console.ReadLine());
        shape.shift(new Point2D(movementVector));
    }
    else if (movementType == "rot")
    {
        Console.WriteLine("Rotation angle (counterclockwise): ");
        double angle = Convert.ToDouble(Console.ReadLine());
        shape.rot(angle);
    }
    else if (movementType == "symaxis")
    {
        Console.WriteLine("Axis index: ");
        int axisOfSymmetryIndex = Convert.ToInt32(Console.ReadLine());
        shape.symAxis(axisOfSymmetryIndex);
    }
    else throw new Exception("Such movement is not applicable");
    Console.WriteLine("Movement parameters: ");
    Console.WriteLine(shape.toString());
    Console.WriteLine("Does the shifted shape cross figure with the same index?");
    if (shape.cross(figures[i]))
        Console.WriteLine("YES");
    else
        Console.WriteLine("NO");
}
