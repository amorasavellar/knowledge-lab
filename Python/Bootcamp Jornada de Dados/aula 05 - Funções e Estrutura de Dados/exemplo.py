def soma(valor_1: float, valor_2: float) -> float:
    """Função simples que retorna a soma entre dois valores do tipo float

    Args:
        valor_1 (float): Primeiro valor
        valor_2 (float): Segundo valor

    Returns:
        float: Resultado da soma
    """
    resultado = valor_1 + valor_2
    return resultado

resultado_soma = soma(valor_1=1,valor_2=2)
print(resultado_soma)