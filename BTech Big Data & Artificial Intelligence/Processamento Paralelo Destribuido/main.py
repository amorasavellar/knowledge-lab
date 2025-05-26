# Necessário ter o python 3 instalado na máquina
# Necessário ter o gerenciador de pacotes do python 'pip' instalado
# Para instalar o pip usem o comando 'sudo apt install python3-pip'
# Será usado a biblioteca numpy para a criação das matrizes de forma aleatória

# Importa numpy e renomeia como np para utilização no código
import numpy as np
# Importa as classes Process e Array do módulo multiprocessing. 
# Este módulo permite a criação de processos paralelos nativos do Python
from multiprocessing import Process, Array

'''
Função criada para realizar a multiplicação de matrizes.
1) A_row: Linha da matriz A
2) B: Matriz B completa (multiplicada por cada linha A_row)
3) C_row_index: O índice da linha na matriz resultado C 
onde o resultado da multiplicação de A_row por B será armazenado.
4) C_shared: Array compartilhado do tipo 'multiprocessing.Array'.
Armazena o resultado da multiplicação. Acessível nos processos paralelos
'''
def multiply_row(A_row, B, C_row_index, C_shared):
    # Acessa o buffer de memória compartilhada entre processos e cria uma visão numpy dele
    # O buffer é redimensionado para as dimensões esperadas do resultado da multiplicação de matrizes
    C_row = np.frombuffer(C_shared.get_obj()).reshape(A.shape[0], B.shape[1])[C_row_index]

    # Calcula o produto da linha A_row por B e armazena diretamente na linha correspondente de C
    # Isso permite a atualização do array compartilhado em memória entre diferentes processos
    np.dot(A_row, B, out=C_row)

if __name__ == '__main__':
    # Matrizes A e B com valores arredondados para 2 casas decimais
    A = np.round(np.random.rand(4, 4), 2)
    B = np.round(np.random.rand(4, 4), 2)

    # Array para armazenar o resultado da multiplicação
    C_shared = Array('d', A.shape[0] * B.shape[1])


    # Lista para armazenar os processos
    processes = []

    # Cria e inicia um processo para cada linha de A
    for i in range(A.shape[0]):
        p = Process(target=multiply_row, args=(A[i], B, i, C_shared))
        processes.append(p)
        p.start()

    # Espera todos os processos terminarem
    for p in processes:
        p.join()
    

    # Converte o array compartilhado de volta para um formato numpy para fácil manipulação e visualização
    C_result = np.frombuffer(C_shared.get_obj()).reshape(A.shape[0], B.shape[1])

    print("Matriz A:\n", A)
    print("Matriz B:\n", B)
    print("Matriz C (resultado):\n", np.round(C_result, 2))  # Arredondando o resultado
