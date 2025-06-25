# Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

validos = [usuario for usuario in usuarios if usuario["email"]]

print(validos)