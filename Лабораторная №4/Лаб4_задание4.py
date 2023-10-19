class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    @staticmethod
    def info():
        print("Точки имеют координаты x y")

    @classmethod
    def func(cls):
        return cls(5,4)

    def show_coor(self):
        print(f"Координата х: {self.x} Координата у: {self.y} ")


a = Point(2,3)
a.info()
b = a.func()
a.show_coor()
b.show_coor()
