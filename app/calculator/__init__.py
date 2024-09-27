# Importing necessary functions from the app.operations module
# These functions (addition, subtraction, multiplication, division) perform the core arithmetic operations.
from app.operations import addition, subtraction, multiplication, division

# Defining the Calculator class which acts as an interface to perform arithmetic operations.
class Calculator:

    @classmethod
    def create(cls):
        """
        Factory Method: This method provides a way to instantiate the Calculator class.
        Using a class method here allows us to follow the Factory Method pattern, 
        which can be beneficial if additional setup or subclassing is needed in the future.
        """
        return cls()  # Returns an instance of the Calculator class.

    def add(self, a, b):
        """
        Add Method: This method performs the addition of two numbers.
        
        Arguments:
        a -- the first number (float or int)
        b -- the second number (float or int)
        
        The method calls the external addition function imported from app.operations.
        This keeps the core functionality modular and reusable.
        """
        return addition(a, b)  # Delegates the addition to the addition function.

    def subtract(self, a, b):
        """
        Subtract Method: This method performs the subtraction of two numbers.
        
        Arguments:
        a -- the first number (float or int)
        b -- the second number (float or int)
        
        The method calls the external subtraction function imported from app.operations.
        """
        return subtraction(a, b)  # Delegates the subtraction to the subtraction function.

    def multiply(self, a, b):
        """
        Multiply Method: This method performs the multiplication of two numbers.
        
        Arguments:
        a -- the first number (float or int)
        b -- the second number (float or int)
        
        The method calls the external multiplication function imported from app.operations.
        """
        return multiplication(a, b)  # Delegates the multiplication to the multiplication function.

    def divide(self, a, b):
        """
        Divide Method: This method performs the division of two numbers.
        
        Arguments:
        a -- the first number (float or int)
        b -- the second number (float or int)
        
        The method calls the external division function imported from app.operations.
        It may need additional error handling for cases like division by zero, 
        which can be handled at the operation level.
        """
        return division(a, b)  # Delegates the division to the division function.
