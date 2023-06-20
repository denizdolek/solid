# Single Responsibility Principle (SRP)
# Each class has a single responsibility.

class Shape:
    def area(self):
        pass

# Open/Closed Principle (OCP)
# The Shape class is open for extension but closed for modification.
# New shapes can be added without changing the existing code.


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius

# Liskov Substitution Principle (LSP)
# The Rectangle and Circle classes are substitutable for the Shape class.
# They implement the same methods and can be used interchangeably.

class AreaCalculator:
    def total_area(self, shapes):
        total = 0
        for shape in shapes:
            total += shape.area()
        return total

class AreaPrinter:
    def print_area(self, area):
        print(f"The total area is {area}")


# Interface Segregation Principle (ISP)
# There is no explicit interface segregation in this example,
# but the Shape class acts as a common interface that is implemented by the derived classes.

# Dependency Inversion Principle (DIP)
# The AreaCalculator and AreaPrinter classes depend on abstractions (Shape)
# rather than concrete implementations (Rectangle, Circle).

# Client code
shapes = [Rectangle(4, 5), Circle(3), Rectangle(2, 6)]
calculator = AreaCalculator()
printer = AreaPrinter()

total_area = calculator.total_area(shapes)
printer.print_area(total_area)