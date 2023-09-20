class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    def __init__(self, width, height):
        self.width = width
        self.height = height



    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"

    def __str__(self):
        return f'A rectangle with width {self.width} and height {self.height}'




    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    def __verify_input__(self):
        return self.width and self.height >= 0 



    # Create the "area" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.

    def area(self):
        if self.width is None or self.height is None:
            return False
        else:
            return self.width * self.height


    # Create the "perimeter" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    # YOUR CODE HERE

    def perimeter(self):
        if self.width is None or self.height is None:
            return False
        else:
            return self.width * 2 + self.height * 2

    


def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()