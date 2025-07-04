## Exercises

Here are five exercises that involve `TypeError`, type checking, the use of `try-except` for exception handling, and the use of the `if` conditional structure. These exercises progressively increase in difficulty and cover practical situations where you can apply these concepts.

### Exercise 21: Temperature Converter

Write a program that converts the temperature from Celsius to Fahrenheit. The program should prompt the user for the temperature in Celsius and, using `try-except`, ensure that the input is numeric, handling any `ValueError`. Print the result in Fahrenheit or an error message if the input is not valid.

### Exercise 22: Palindrome Checker

Write a program that checks whether a word or phrase is a palindrome (reads equally backwards, disregarding spaces and punctuation). Use `try-except` to ensure that the input is a string. Hint: Use the `isinstance()` function to check the type of the input.

### Exercise 23: Simple Calculator

Develop a simple calculator that accepts two numeric inputs and an operator (+, -, *, /) from the user. Use `try-except` to handle division by zero and non-numeric inputs. Use `if-elif-else` to perform the mathematical operation based on the given operator. Print the result or an appropriate error message.

### Exercise 24: Number Classifier

Write a program that prompts the user to enter a number. Use `try-except` to ensure that the input is numeric and use `if-elif-else` to classify the number as "positive", "negative", or "zero". Additionally, identify whether the number is "even" or "odd".

### Exercise 25: Type Conversion with Validation

Create a script that prompts the user for a list of numbers separated by commas. The program should convert the input string to a list of integers. Use `try-except` to handle the conversion of each number and validate that each element of the converted list is an integer. If the conversion fails or an element is not an integer, print an error message. If the conversion succeeds for all elements, print the list of integers.

## Solved Exercises

### Exercise 21: Temperature Converter

```python
try:
celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")
except ValueError:
print("Please enter a valid number for the temperature.")
```

### Exercise 22: Palindrome Checker

```python
input = input("Enter a word or phrase: ")
if isinstance(input, str):
formatted = input.replace(" ", "").lower()
if formatted == formatted[::-1]:
print("It's a palindrome.")
else:
print("It's not a palindrome.") palindrome.")
else:
print("Invalid input. Please enter a word or phrase.")
```

### Exercise 23: Simple Calculator

```python
try:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator == '+':
result = num1 + num2
elif operator == '-':
result = num1 - num2
elif operator == '*':
result = num1 * num2
elif operator == '/' and num2 != 0:
result = num1 / num2
else:
print("Invalid operator or division by zero.")
print("Result:", result)
except ValueError:
print("Error: Invalid input. Make sure to enter numbers.")
```

### Exercise 24: Number Sorter

```python
try:
number = int(input("Enter a number: "))
if number > 0:
print("Positive")
elif number < 0:
print("Negative")
else:
print("Zero")
if number % 2 == 0:
print("Even")
else:
print("Odd")
except ValueError:
print("Please enter a valid integer.")
```

### Exercise 25: Type Conversion with Validation

```python
list_input = input("Enter a comma-separated list of numbers: ")
str_numbers = list_input.split(",")
int_numbers = []
try:
for num in num_str:
num_int.append(int(num.strip()))
print("List of integers:", num_int)
except ValueError:
print("Error: Make sure all elements are valid integers.")
```