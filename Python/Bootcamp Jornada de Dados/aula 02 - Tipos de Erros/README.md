# TypeError, Type Check, and Type Conversion in Python

Python is a dynamic but strongly typed programming language, which means that it is not necessary to explicitly declare variable types, but the type of a variable is determined by the value it stores. This introduces the need to understand how Python handles different data types, especially when it comes to operations involving multiple types. We will explore three important concepts: `TypeError`, `type check`, and `type conversion`.

Ref: https://docs.python.org/3/library/exceptions.html

## TypeError

A `TypeError` occurs in Python when an operation or function is applied to an object of an inappropriate type. Python does not know how to apply the operation because the data types are not compatible.

### TypeError Example

A classic example is trying to use the `len()` function with an integer, which results in a `TypeError`, because `len()` expects an iterable object, such as a string, list, or tuple, not an integer.

```python
# Example that causes TypeError
try:
result = len(5)
except TypeError as e:
print(e) # Print the error message
```

The code above tries to get the length of an integer, which doesn't make sense, resulting in the error message: "object of type 'int' has no len()".

## Type Check

Type checking is the process of checking the type of a variable. This can be useful to ensure that operations or functions are applied only to compatible data types, avoiding runtime errors.

### Type Check Example

To check the type of a variable in Python, you can use the `type()` or `isinstance()` function.

```python
number = 10
if isinstance(number, int):
print("The variable is an integer.")
else:
print("The variable is not an integer.")
```

This code checks whether `number` is an instance of `int` and prints an appropriate message.

## Type Conversion

Type conversion, also known as casting, is the process of converting the value of a variable from one type to another. Python provides several built-in functions to perform explicit type conversions, such as `int()`, `float()`, `str()`, etc.

### Type Conversion Example

If you want to add an integer and a float, you may need to convert the integer to float or vice versa to ensure that the addition operation is performed correctly.

```python
integer_number = 5
float_number = 2.5
# Convert the integer to a float and perform the sum
sum = float(integer_number) + float_number
print(sum) # Result: 7.5
```

### try-except

The `try-except` structure is used for exception handling in Python. An exception is an error that occurs during program execution and, if left unhandled, interrupts the normal flow of the program and terminates its execution. Exception handling allows the program to handle errors gracefully, allowing it to continue execution or fail in a controlled manner.

* **try:** This block is the first in the exception handling structure. Python attempts to execute the code within this block.
* **except:** If an exception occurs in the `try` block, execution immediately jumps to the `except` block. You can specify specific exception types to catch and handle only those exceptions. If no exception type is specified, it catches all exceptions.

#### Try-except example

```python
try:
# Code that can throw an exception
result = 10 / 0
except ZeroDivisionError:
# Code that executes if the ZeroDivisionError exception is raised
print("Division by zero is not allowed.")
```

### if

The `if` is a control flow structure that allows the program to perform different actions based on different conditions. If the condition evaluated by the `if` is true (`True`), the indented block of code beneath it is executed. If the condition is false (`False`), the block of code is skipped.

* **if:** Evaluates a condition. If the condition is true, executes the associated block of code.
* **elif:** Short for "else if". Allows you to check multiple conditions in sequence. * **else:** Executes a block of code if all of the preceding conditions in the `if` and `elif` statements are false.

#### Example of if

```python
age = 20
if age < 18:
print("Underage")
elif age == 18:
print("Exactly 18 years old")
else:
print("Of legal age")
```

Both the `try-except` and `if` structures are fundamental to creating Python programs that are capable of handling unexpected situations (such as runtime errors) and making decisions based on conditions, thus allowing you to build more robust, flexible, and secure programs.