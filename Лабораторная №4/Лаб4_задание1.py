class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # @staticmethod
    # def is_valid_side(side):
    #     try:
    #         side = float(side)
    #         return side > 0
    #     except ValueError:
    #         return False

    def is_triangle(self):
        return ((self.side1 + self.side2 > self.side3) and (self.side1 + self.side3 > self.side2) and
                (self.side3 + self.side2 > self.side1))

    def find_area(self):
        if not self.is_triangle():
            return "треугольник с такими сторонами не существует"

        poly_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = (poly_perimeter * (poly_perimeter - self.side1) *
                (poly_perimeter - self.side2) * (poly_perimeter - self.side3)) ** 0.5
        return area

    def find_perimeter(self):
        if not self.is_triangle():
            return "треугольник с такими сторонами не существует"

        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

while True:
    try:
        side1 = float(input("Введите длину первой стороны: "))
        side2 = float(input("Введите длину второй стороны: "))
        side3 = float(input("Введите длину третьей стороны: "))

        if not (side1 > 0 and side2 > 0 and side3 > 0):
            print("Длины должны быть положительными")
            continue

        triangle = Triangle(side1, side2, side3)

        if triangle.is_triangle():
            print(f"Площадь треугольника: {triangle.find_area()}")
            print(f"Периметр треугольника: {triangle.find_perimeter()}")
            break
        else:
            print("Треугольника с такими сторонами не существует")
    except ValueError:
        print("Введите корректные значения")
