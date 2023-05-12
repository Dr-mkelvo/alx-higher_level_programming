class Polygon:
    def render(self):
        print("Rendering polygon")


class Square(Polygon):
    def render(self):
        print("Rendering Square")


class Circle(Polygon):
    def render(self):
        print("Rendering Circle")

c = Circle()
c.render()

s =Square()
s.render()