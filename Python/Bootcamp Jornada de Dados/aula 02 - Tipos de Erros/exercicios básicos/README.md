### Exercises

#### Integers (`int`)

1. Write a program that adds two integers entered by the user.
2. Create a program that receives a number from the user and calculates the remainder of the division of that number by 5.
3. Develop a program that multiplies two numbers provided by the user and displays the result.
4. Write a program that asks for two integers and prints the integer division of the first by the second.
5. Write a program that calculates the square of a number provided by the user.

#### Floating Point Numbers (`float`)

6. Write a program that receives two floating point numbers and performs their addition.
7. Create a program that calculates the average of two floating point numbers provided by the user.
8. Develop a program that calculates the power of a number (base and exponent provided by the user). 9. Write a program that converts the temperature from Celsius to Fahrenheit.

10. Write a program that calculates the area of ​​a circle, given the radius as input.

#### Strings (`str`)

11. Write a program that takes a string from the user and converts it to uppercase.

12. Write a program that takes the user's full name and prints the name in all lowercase letters.

13. Write a program that asks the user to enter a sentence and then prints that sentence without leading or trailing spaces.

14. Write a program that asks the user to enter a date in the format "dd/mm/yyyy" and then prints the day, month, and year separately.

15. Write a program that concatenates two strings provided by the user.

#### Booleans (`bool`)

16. Write a program that evaluates two Boolean expressions entered by the user and returns the result of the AND operation between them.

17. Write a program that receives two Boolean values ​​from the user and returns the result of the OR operation.

18. Write a program that asks the user to enter a Boolean value and then inverts that value.

19. Write a program that compares whether two numbers entered by the user are equal.

20. Write a program that checks whether two numbers entered by the user are different.

### Exercises Resolution

### Exercise 1: Sum of Two Integers

```python
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
num1 = 8 # Input example
num2 = 12 # Input example
result_sum = num1 + num2
print("The sum is:", result_sum)
```

### Exercise 2: Remainder of Division by 5

```python
# num = int(input("Enter a number: "))
num = 18 # Input example
result_remainder = num % 5
print("The remainder of division by 5 is:", result_remainder)
```

### Exercise 3: Multiplication of Two Numbers

```python
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
num1 = 5 # Input example
num2 = 7 # Input example
resultado_multiplicacao = num1 * num2
print("The result of multiplication is:", multiplication_result)
```

### Exercise 4: Integer Division of the First Number by the Second Number

```python
# num1 = int(input("Enter the first integer: "))
# num2 = int(input("Enter the second integer: "))
num1 = 20 # Input example
num2 = 3 # Input example
resultado_divisao_ineira = num1 // num2
print("The result of integer division is:", integer_division_result)
```

### Exercise 5: Squaring a Number

```python
# num = int(input("Enter a number: "))
num = 6 # Example input
squared_result = num ** 2
print("The square of the number is:", squared_result)
```

### Exercise 6: Addition of Two Floating Numbers

```python
# num1 = float(input("Enter the first floating number: "))
# num2 = float(input("Enter the second floating number: "))
num1 = 2.5 # Example input
num2 = 4.5 # Example input
sum_result = num1 + num2
print("The sum is:", sum_result)
```

### Exercise 7: Average of Two Numbers Floats

```python
# num1 = float(input("Enter the first float: "))
# num2 = float(input("Enter the second float: "))
num1 = 3.5 # Input example
num2 = 7.5 # Input example
average = (num1 + num2) / 2
print("The average is:", average)
```

### Exercise 8: Power of a Number

```python
# base = float(input("Enter the base: "))
# exponent = float(input("Enter the exponent: "))
base = 2.0 # Input example
exponent = 3.0 # Input example
power = base ** exponent
print("The result of the power is:", power)
```

### Exercise 9: Converting from Celsius to Celsius Fahrenheit

```python
# celsius = float(input("Enter the temperature in Celsius: "))
celsius = 30.0 # Example input
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
```

### Exercise 10: Area of ​​a Circle

```python
# radius = float(input("Enter the radius of the circle: "))
radius = 5.0 # Example input
area = 3.14159 * radius ** 2
print("The area of ​​the circle is:", area)
```

### Exercício 11: Converter String para Maiúsculas

```python
# texto = input("Digite um texto: ")
texto = "Olá, mundo!"  # Exemplo de entrada
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)
```

### Exercício 12: Imprimir Nome Completo em Minúsculas

```python
# nome_completo = input("Digite seu nome completo: ")
nome_completo = "Fulano de Tal"  # Exemplo de entrada
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)
```

### Exercício 13: Remover Espaços em Branco de uma Frase

```python
# frase = input("Digite uma frase: ")
frase = "  Olá, mundo!  "  # Exemplo de entrada
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)
```

### Exercício 14: Separar Dia, Mês e Ano de uma Data

```python
# data = input("Digite uma data no formato dd/mm/aaaa: ")
data = "01/01/2024"  # Exemplo de entrada
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
```

### Exercício 15: Concatenar Duas Strings

```python
# parte1 = input("Digite a primeira parte do texto: ")
# parte2 = input("Digite a segunda parte do texto: ")
parte1 = "Olá,"  # Exemplo de entrada
parte2 = " mundo!"  # Exemplo de entrada
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)
```

#### Exercício 16. Operador `and` (E lógico)

```python
# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)
```

#### Exercício 17. Operador `or` (OU lógico)

```python
# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)
```

#### Exercício  18. Operador `not` (NÃO lógico)

```python
# Exemplo de entrada
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)
```

#### Exercício 19. Operador `==` (Igualdade)

```python
# Exemplo de entrada
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)
```

#### Exercício 20. Operador `!=` (Diferença)

```python
# Exemplo de entrada
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)
```
### Exercise 11: Convert String to Uppercase

```python
# text = input("Enter some text: ")
text = "Hello, world!" # Example input
text_upper = text.upper()
print("Text in uppercase:", text_upper)
```

### Exercise 12: Print Full Name in Lowercase

```python
# full_name = input("Enter your full name: ")
full_name = "So-and-So" # Example input
name_lower = full_name.lower()
print("Name in lowercase:", name_lower)
```

### Exercise 13: Remove Whitespace from a Sentence

```python
# sentence = input("Enter a sentence: ")
sentence = "Hello, world!" # Example input
sentence_without_spaces = sentence.strip()
print("Sentence without spaces at the beginning and end:", phrase_without_spaces)
```

### Exercise 14: Separate Day, Month and Year from a Date

```python
# data = input("Enter a date in dd/mm/yyyy format: ")
date = "01/01/2024" # Example input
day, month, year = data.split("/")
print("Day:", day)
print("Month:", month)
print("Year:", year)
```

### Exercise 15: Concatenate Two Strings

```python
# part1 = input("Enter the first part of the text: ")
# part2 = input("Enter the second part of the text: ")
part1 = "Hello," # Example input
part2 = " world!" # Input example
concatenated_text = part1 + part2
print("Concatenated text:", concatenated_text)
```

#### Exercise 16. `and` operator (logical AND)

```python
# Input example
value1 = True
value2 = False
and_result = value1 and value2
print("Logical AND result:", and_result)
```

#### Exercise 17. `or` operator (logical OR)

```python
# Input example
or_result = value1 or value2
print("Logical OR result:", or_result)
```

#### Exercise 18. `not` operator (logical NOT)

```python
# Input example
not_result = not value1
print("Logical NOT result:", result_not)
```

#### Exercise 19. Operator `==` (Equality)

```python
# Input example
num1 = 5
num2 = 5
result_equality = (num1 == num2)
print("Result of equality:", result_equality)
```

#### Exercise 20. Operator `!=` (Difference)

```python
# Input example
result_difference = (num1 != num2)
print("Result of difference:", result_difference)
```