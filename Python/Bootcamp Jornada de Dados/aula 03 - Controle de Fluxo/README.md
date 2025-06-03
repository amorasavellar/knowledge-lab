# Aula 03: DEBUG, IF, FOR, While, Listas e Dicionários em Python

Vamos explorar estruturas de controle de fluxo como if, for, e while. 

Usamos estrutura de Controle de Fluxo para tomar decisões!

Databricks tem workflow
![imagem_06](./assets/image1.png)

Airflow principal ferramenta de workflow
![imagem_07](./assets/image2.png)

### Estruturas de Controle de Fluxo

Exploraremos como utilizar `if` para tomar decisões baseadas em condições, `for` para iterar sobre sequências de dados, e `while` para executar blocos de código enquanto uma condição for verdadeira.

Para saber mais:
[Doc](https://docs.python.org/pt-br/3/tutorial/controlflow.html)


## Estruturas de Controle de Fluxo

O if é uma estrutura condicional fundamental em Python que avalia se uma condição é verdadeira (True) e, se for, executa um bloco de código. Se a condição inicial não for verdadeira, você pode usar elif (else if) para verificar condições adicionais, e else para executar um bloco de código quando nenhuma das condições anteriores for verdadeira.

Provavelmente o mais conhecido comando de controle de fluxo é o if. Por exemplo:

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