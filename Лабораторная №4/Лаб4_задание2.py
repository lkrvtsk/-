class Room:
    def __init__(self, length, width, height, windows, doors):
        self.length = length
        self.width = width
        self.height = height
        self.windows = windows
        self.doors = doors

    def wall_area(self):
        room_perimeter = 2 * (self.length + self.width)
        wall_area = room_perimeter * self.height
        return wall_area - (self.windows * 4) - (self.doors * 2)

    @staticmethod
    def is_valid_side(side):
        try:
            side = float(side)
            return side > 0
        except ValueError:
            return False

    @staticmethod
    def is_valid_quantity(quantity):
        try:
            quantity = int(quantity)
            return quantity >= 0
        except ValueError:
            return False


def main():
    while True:
        try:
            length = float(input("Длина: "))
            width = float(input("Ширина: "))
            height = float(input("Высота: "))
            windows = int(input("Количество окон: "))
            doors = int(input("Количество дверей: "))

            if not (length > 0 and width > 0 and height > 0):
                print("Длины должны быть положительными")
                continue

            if not (windows >= 0 and doors >= 0):
                print("Кол-во окон или дверей должны быть неотрицательными")
                continue

            room = Room(length, width, height, windows, doors)
            wall_area = room.wall_area()

            print(f"Площадь, которую нужно обклеить: {wall_area} кв. м")
            break

        except ValueError:
            print("Введите корректные значения")


if __name__ == "__main__":
    main()
