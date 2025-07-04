## Control Flow Structures

The if statement is a fundamental conditional structure in Python that evaluates whether a condition is true and, if so, executes a block of code. If the initial condition is not true, you can use elif (else if) to check for additional conditions, and else to execute a block of code when none of the previous conditions are true.

Probably the best-known control flow statement is the if statement. For example:

```python
x = int(input("Please enter an integer: "))

if x < 0:
x = 0
print('Negative changed to zero')
elif x == 0:
print('Zero')
elif x == 1:
print('Single')
else:
print('More')
```

### Exercise 1: Data Quality Check

You are analyzing a sales data set and need to ensure that all records have positive values ​​for `quantity` and `price`. Write a program that checks these fields and prints "Valid data" if both are positive or "Invalid data" otherwise.

```python
quantity = 10 # Example value, replace with user input if necessary
price = 20 # Example value, replace with user input if necessary

if quantity > 0 and price > 0:
print("Valid data")
else:
print("Invalid data")
```

### Exercise 2: Classifying Sensor Data

Imagine you are working with IoT sensor data. The data includes temperature measurements. You need to classify each reading as 'Low', 'Normal', or 'High'. Considering that:

* Temperature < 18°C ​​is 'Low'
* Temperature >= 18°C ​​and <= 26°C is 'Normal'
* Temperature > 26°C is 'High'

```python
temperature = 22 # Example value, replace with user input if necessary

if temperature < 18:
print("Low")
elif 18 <= temperature <= 26:
print("Normal")
else:
print("High")
```

### Exercise 3: Filtering Logs by Severity

You are analyzing logs from an application and need to filter messages with severity 'ERROR'. Given a log record in dictionary format as `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failed'}`, write a program that prints the message if the severity is 'ERROR'.

```python
log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Connection failed'}

if log['level'] == 'ERROR':
print(log['message'])
```

### Exercise 4: Input Data Validation

Before processing user data in a recommendation system, you need to ensure that each user is between the ages of 18 and 65 and has provided a valid email address. Write a program that validates these conditions and prints "Valid user data" or the specific error encountered.

```python
age = 25 # Example value, replace with user input if necessary
email = "user@example.com" # Example value, replace with user input if necessary

if not 18 <= age <= 65:
print("Age outside the allowed range")
elif "@" not in email or "." not in email:
print("Invalid email")
else:
print("Valid user data")
```

### Exercise 5: Detecting Anomalies in Transaction Data

You are working on a fraud detection system and need to identify suspicious transactions. A transaction is considered suspicious if the amount is greater than R$10,000 or if it occurs outside business hours (before 9 am or after 6 pm). Given a transaction like `transaction = {'value': 12000, 'time': 20}`, check if it is suspicious.

```python
transaction = {'value': 12000, 'time': 20}

if transaction['value'] > 10000 or transaction['time'] < 9 or transaction['time'] > 18:
print("Suspicious transaction")
else:
print("Normal transaction")
```

### FOR

O loop `for` é utilizado para iterar sobre os itens de qualquer sequência, como listas, strings, ou objetos de dicionário, e executar um bloco de código para cada item. É especialmente útil quando você precisa executar uma operação para cada elemento de uma coleção.

O comando for em Python é um pouco diferente do que costuma ser em C ou Pascal. Ao invés de sempre iterar sobre uma progressão aritmética de números (como no Pascal), ou permitir ao usuário definir o passo de iteração e a condição de parada (como C), o comando for do Python itera sobre os itens de qualquer sequência (seja uma lista ou uma string), na ordem que aparecem na sequência. Por exemplo:

```python
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
```

```python
# Measure some strings:
nome = ['Luciano']
for letra in nome:
    print(letra)
```

Se você precisa iterar sobre sequências numéricas, a função embutida `range()` é a resposta. Ela gera progressões aritméticas:


```python
for i in range(5):
    print(i)
```

O ponto de parada fornecido nunca é incluído na lista; range(10) gera uma lista com 10 valores, exatamente os índices válidos para uma sequência de comprimento 10. É possível iniciar o intervalo com outro número, ou alterar a razão da progressão (inclusive com passo negativo):


```python
list(range(5, 10))
[5, 6, 7, 8, 9]

list(range(0, 10, 3))
[0, 3, 6, 9]

list(range(-10, -100, -30))
[-10, -40, -70]
```

Para iterar sobre os índices de uma sequência, combine range() e len() da seguinte forma:

```python
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
```

[Material sobre Dicionários](https://www.youtube.com/watch?v=ZWj8o692qGY)

#### 6. Contagem de Palavras em Textos

**Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

```python
texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)
```

#### 7. Normalização de Dados

**Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

```python
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)
```

#### 8. Filtragem de Dados Faltantes

**Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

```python
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

print(usuarios_validos)
```

#### 9. Extração de Subconjuntos de Dados

**Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

```python
numeros = range(1, 11)
pares = [x for x in numeros if x % 2 == 0]

print(pares)
```

#### 10. Agregação de Dados por Categoria

**Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

```python
vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}
for venda in vendas:
    categoria = venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

print(total_por_categoria)
```

### Exercises with WHILE

The while loop is a fundamental flow control structure in Python, allowing you to execute a block of code repeatedly while a specified condition evaluates to True. In data engineering, the use of while can be extremely useful for several tasks, such as continuous monitoring of data sources, execution of ETL (Extract, Transform, Load) processes until there is no more data to process, or even to implement automatic reconnection attempts to services or databases when the first attempt fails.

#### Example of Using while in Data Engineering
A common scenario in data engineering is the need to execute a task periodically, such as checking for new data in a directory, polling an API for new responses, or monitoring changes in a database. In these cases, a while loop can be used to keep the script running continuously or until a specific condition is met (for example, a shutdown signal or an error condition).

#### Practical Example: while True with Pause

A straightforward example of using while True in Python is to create an infinite loop that performs an action at a defined interval, such as printing a message every 10 seconds. This can be useful for monitoring processes or data in real time with a periodic check.

```python
import time

while True:
print("Checking for new data...")
# Here you can add code to check for new data,
# for example, checking for new files in a directory,
# making a query to a database or API, etc.

time.sleep(10) # Pauses the loop for 10 seconds
```
In this example, while True creates an infinite loop, which is a powerful way to keep a script running continuously. print simulates the action of checking for new data, and time.sleep(10) pauses the loop for 10 seconds before the next iteration. This approach is simple but effective for many data engineering monitoring and polling scenarios, allowing the script to perform a check or task periodically.

However, it is important to use infinite loops with caution to avoid creating conditions where the script may consume unnecessary resources or become difficult to terminate in a controlled manner. In production environments, other approaches such as task scheduling (e.g. using cron jobs on Unix systems) or the use of message queuing systems and database triggers may be more suitable for some of these tasks.

#### 11. Reading Data Until Flag

**Objective:** Read input data until a specific keyword ("exit") is given.

```python
data = []
input = ""
while input.lower() != "exit":
input = input("Enter a value (or 'exit' to finish): ")
if input.lower() != "exit":
```

#### 12. Input Validation

**Objective:** Prompt the user for a number within a specific range until the input is valid.

```python
number = int(input("Please enter a number between 1 and 10: "))
while number < 1 or number > 10:
print("Number out of range!")
number = int(input("Please enter a number between 1 and 10: "))

print("Valid number!")
```

#### 13. Simulated API Consumption

**Objective:** Simulate the consumption of a paginated API, where each "page" of data is processed in a loop until there are no more pages.

```python
current_page = 1
total_pages = 5 # Simulation, in practice, this would come from the API

while current_page <= total_pages:
print(f"Processing page {current_page} of {total_pages}")
# Here would be the code to process the page data
current_page += 1

print("All pages have been processed.")
```

#### 14. Connection Attempts

**Objective:** Simulate reconnection attempts to a service with a maximum limit of attempts.

```python
maximum_attempts = 5
attempt = 1

while attempt <= maximum_attempts:
print(f"Attempt {attempt} of {maximum_attempts}")
# Simulating a connection attempt
# Here would be the code to attempt to connect
if True: # Assume the connection was successful
print("Connection successful!")
break
attempt += 1
else:
print("Failed to connect after multiple attempts.")
```

#### 15. Data Processing with Stopping Condition

**Objective:** Process items in a list until a specific value is found that indicates stopping.

```python
items = [1, 2, 3, "stop", 4, 5]

i = 0
while i < len(items):
if items[i] == "stop":
print("Stop found, ending processing.")
break
# Process the item
print(f"Processing item: {items[i]}")
i += 1
```