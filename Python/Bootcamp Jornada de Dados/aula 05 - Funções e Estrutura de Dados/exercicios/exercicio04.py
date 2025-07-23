# Converter Celsius para Fahrenheit em uma Lista

def celsius_para_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius *1.8) + 32
    return fahrenheit

temp_1 = 25
print(celsius_para_fahrenheit(temp_1))