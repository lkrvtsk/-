import math as m

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return m.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def get_positive(sm):
    while True:
        try:
            value = float(input(sm))
            if value >= 0:
                return value
            else:
                print("введите неотрицательное число")
        except ValueError:
            print("введите корректное число.")



def main():
    while True:
        try:
            shape_type = input("выберите фигуру (круг, квадрат, прямоугольник): ").lower()

            if shape_type == "круг":
                radius = get_positive("введите радиус круга:")
                shape = Circle(radius)
            elif shape_type == "квадрат":
                side = get_positive("введите сторону квадрата:")
                shape = Square(side)
            elif shape_type == "прямоугольник":
                length = get_positive("введите длину прямоугольника:")
                width = get_positive("введите ширину прямоугольника:")
                shape = Rectangle(length, width)
            else:
                print("некорректный выбор фигуры")
                continue

            area = shape.area()
            print(f"Площадь выбранной фигуры: {area} кв. ед.")
            break
        except ValueError:
            print("Введите корректные значения")

if __name__ == "__main__":
    main()
