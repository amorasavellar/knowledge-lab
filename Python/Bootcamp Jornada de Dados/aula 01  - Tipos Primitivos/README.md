# Primeiros Comandos com Python

Nessa aula foi ensinado como aplicar os primeiros comandos em Python, desde print() até a declaração de Tipos Primitivos de dados. Além disso foi ensinado como instalar de forma correta o Python, VS Code, Git e por fim, como utilizar o Github, possibilitando que os scripts desenvolvidos pudessem ser versionados e compartilhados no GitHub.

# Principais Pontos da Aula:

**Tipos de Dados**

Python suporta vários tipos de dados, incluindo, mas não se limitando a:

* Inteiros (`int`)
* Números de ponto flutuante (`float`)
* Strings (`str`)
* Listas (`list`)
* Tuplas (`tuple`)
* Dicionários (`dict`)
* Booleanos (`bool`)

A linguagem determina o tipo de dados de uma variável no momento da atribuição, o que permite grande flexibilidade, mas também exige atenção para evitar erros de tipo.

**Nomes de Variáveis**

Python tem algumas regras e convenções para nomes de variáveis:

* Os nomes podem conter letras, números e sublinhados (`_`), mas não podem começar com um número.
* Os nomes de variáveis são _case-sensitive_, o que significa que `variavel`, `Variavel`, e `VARIaVEL` são consideradas três variáveis diferentes.
* Existem algumas palavras reservadas que não podem ser usadas como nomes de variáveis, como `if`, `for`, `class`, entre outras.
* É recomendado seguir a convenção _snake_case_ para nomes de variáveis que consistem em mais de uma palavra, como `nome_usuario` ou `total_pedidos`.

**Dinamismo e Reatribuição**

Uma característica importante das variáveis em Python é a possibilidade de reatribuí-las a diferentes tipos de dados:

```python
x = 100        # x é um inteiro
x = "Python"   # Agora x é uma string
```

Isso demonstra a tipagem dinâmica do Python, mas também destaca a importância de gerenciar tipos de dados com cuidado para evitar confusão ou erros em programas mais complexos.

**Escopo de Variáveis**

O escopo de uma variável determina onde ela é acessível dentro do código. Variáveis definidas em um bloco principal são globalmente acessíveis, enquanto variáveis definidas dentro de funções são locais a essas funções, a menos que sejam explicitamente declaradas como `global`.

Entender variáveis e tipos de dados é essencial para programação em Python, pois permite manipular dados de maneira eficaz e criar programas dinâmicos e flexíveis. A capacidade de Python de inferir tipos de dados torna a linguagem acessível para iniciantes, ao mesmo tempo em que oferece poderosas funcionalidades para programadores experientes.