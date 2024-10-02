# calculator_is218_f24

Youtube Videos Up Until this point
* [Part 1](https://youtu.be/lk-Ca7AnlDQ)
* [Part 2](https://youtu.be/QCI3slvy-WM)
* [Part 3](https://youtu.be/ZEhHAcjmlF8)
* [Updated Part 4,5, and first part of history](https://youtu.be/NGlJp_u20HU)

# Assignment 1

10-15 Slide PPT, Explaining all the concepts

Here’s a comprehensive list of all the programming and testing concepts demonstrated in the provided calculator program. I've included both small and large concepts to ensure nothing is left out.  Match the code with the concept below in the powerpoint, you should show the code and the concept in the powerpoint slide.

Review the Refactor GURU catalog of patterns: https://refactoring.guru/design-patterns/catalog

### Programming Concepts

1. **Modular Programming**: Functions and classes are organized into separate modules (`app.operations`, `app.calculation`), promoting code reusability and separation of concerns.

2. **Object-Oriented Programming (OOP)**:
   - **Classes and Objects**: The use of `Addition`, `Subtraction`, `Multiplication`, and `Division` classes for specific operations demonstrates OOP.
   - **Inheritance**: `Addition`, `Subtraction`, `Multiplication`, and `Division` inherit from the `Calculation` abstract base class.
   - **Encapsulation**: Each operation (e.g., addition, subtraction) is encapsulated within its respective class.
   - **Polymorphism**: The `compute` method is implemented differently for each subclass, allowing different behavior for each operation.
   - **Abstraction**: The `Calculation` class is an abstract base class, enforcing that subclasses must implement the `compute` method.

3. **Abstract Base Classes (ABC)**:
   - The `Calculation` class uses Python’s `abc` module to define abstract methods that must be implemented by subclasses.

4. **Factory Method Design Pattern**:
   - The `create` method in the `Calculator` class and `Calculation` subclasses uses the Factory Method Pattern to instantiate objects in a standardized way.

5. **Strategy Design Pattern**:
   - The `operations_map` dictionary maps string commands (e.g., 'add', 'subtract') to specific classes (`Addition`, `Subtraction`, etc.), enabling the program to select different algorithms (i.e., calculation operations) at runtime.

6. **Single Responsibility Principle (SRP)**:
   - Each function (e.g., `addition`, `subtraction`) and each class (e.g., `Addition`, `Division`) has a single responsibility, making the program more modular and maintainable.

7. **DRY (Don’t Repeat Yourself)**:
   - Functions and operations are implemented once and reused, avoiding code duplication.

8. **REPL (Read-Eval-Print Loop)**:
   - The main calculator interface uses a REPL pattern to continuously read user input, evaluate it, and print the result.

9. **Exception Handling**:
   - **ValueError**: Handled when invalid data (e.g., non-numeric input) is entered.
   - **ZeroDivisionError**: Specifically handled for division by zero.
   - **Generic Exception Handling**: The program catches any unforeseen errors using `except Exception as e`.

10. **EAFP (Easier to Ask Forgiveness than Permission)**:
    - Division by zero and type errors are handled using exceptions instead of pre-checking.

11. **LBYL (Look Before You Leap)**:
    - Input length and operation checks are done before attempting to parse or compute, ensuring valid input format before proceeding.

12. **Typing and Type Hints**:
    - `from typing import Dict, Type, Union`: The program uses Python’s type hinting to ensure better readability and maintainability.

13. **Command-line Interface (CLI)**:
    - The REPL acts as a command-line interface where users can enter commands to perform arithmetic operations.

14. **Data Validation**:
    - Input data is validated using both exception handling (`try-except` blocks) and type checking.

15. **Mathematical Operations**:
    - Basic arithmetic operations are implemented: addition, subtraction, multiplication, and division.

16. **Functions**:
    - Pure functions are used for arithmetic operations (`addition`, `subtraction`, etc.), adhering to functional programming concepts by avoiding side effects.

17. **Immutability**:
    - The calculator operations do not modify any external state and return results based on inputs.

18. **Control Flow**:
    - The program uses `if-elif-else` blocks to control logic and ensure correct execution paths.

19. **Iteration**:
    - The program uses an infinite `while` loop to continuously prompt the user for input in the REPL.

### Testing Concepts

1. **Unit Testing**:
   - The functions (`addition`, `subtraction`, etc.) and the classes (`Addition`, `Subtraction`, etc.) are tested using unit tests.
   
2. **Pytest Framework**:
   - The `pytest` library is used for writing and running tests, making it easy to parametrize tests and handle exceptions.

3. **Parameterized Testing**:
   - **@pytest.mark.parametrize**: Parameterized tests are used to test functions with multiple sets of input values. This reduces redundancy and increases test coverage.
   
4. **Fixtures**:
   - **@pytest.fixture**: Fixtures are used to set up common test scenarios, such as initializing the calculator instance or starting the REPL for integration testing.

5. **Test-driven Development (TDD)**:
   - The unit tests cover individual functions and methods, which could drive the development process by ensuring functionality works as expected before expanding code.

6. **Boundary and Edge Case Testing**:
   - Edge cases like adding or subtracting zero, dividing by zero, and handling negative numbers are explicitly tested.

7. **Exception Testing**:
   - The `pytest.raises()` method is used to ensure that exceptions, like `ZeroDivisionError` and `TypeError`, are correctly raised when invalid input is provided.

8. **Positive and Negative Test Cases**:
   - Both valid and invalid input are tested (e.g., testing for valid addition, but also invalid types or division by zero).

9. **Error Messages**:
   - The program returns helpful error messages when users input invalid commands or non-numeric data.

10. **Test Coverage**:
    - Tests ensure that all key parts of the application are covered, including valid operations, invalid inputs, and exception handling.

11. **Assertions**:
    - `assert` statements are used to compare the output of operations with expected results in tests.

12. **Code Documentation in Testing**:
    - Docstrings are used to explain what each test case is doing, improving readability and understanding of the test’s purpose.

### General Coding Best Practices

1. **Code Readability**:
   - The code uses clear variable names (`a`, `b`, `operations_map`) and comments/docstrings to improve readability.

2. **Function and Method Naming**:
   - Functions and methods are named descriptively (`addition`, `subtraction`, `compute`), making it clear what each function does.

3. **Documentation**:
   - Thorough comments and docstrings are used to explain the purpose of each function, class, and method.

4. **Code Reuse**:
   - The program maximizes reuse by importing functions (e.g., `addition`, `subtraction`) into multiple classes and contexts.

5. **Modifiability**:
   - The design makes it easy to add new arithmetic operations in the future by simply creating new classes or functions without modifying existing logic.

By identifying and using these concepts, students can understand and apply a wide range of programming principles and testing techniques, making their code more modular, maintainable, and well-tested.