class Shape:
  def area(self, a, b = 0):
    if b > 0:
      print(f"Area of a rectangle is: {a*b}")

    else:
      print(f"Area of a Square is: {a**2}")

square = Shape()
square.area(5)

rectangle = Shape()
rectangle.area(5,3)