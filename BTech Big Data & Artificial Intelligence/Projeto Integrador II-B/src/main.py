import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import os

# 1. Carregar o dataset
try:
    df = pd.read_csv('fictitious_tca_diagnosis.csv')
    print("Dados carregados com sucesso!")
    print("\nPrimeiras 5 linhas do dataset:")
    print(df.head())
    print("\nInformações do dataset:")
    print(df.info())
except FileNotFoundError:
    print("Erro: O arquivo 'fictitious_tca_diagnosis.csv' não foi encontrado.")
    print("Certifique-se de que o arquivo CSV está na mesma pasta do script.")
    exit()

# 2. Preparar os dados para o modelo
# Desconsiderar as colunas 'patient_id' e 'tca_diagnosis' para as features (X)
# 'tca_diagnosis' será a variável alvo (y)
X = df.drop(columns=['patient_id', 'tca_diagnosis'])
y = df['tca_diagnosis']

# Mapeamento dos nomes das colunas para os nomes das perguntas do fluxograma para melhor visualização.
# A ordem aqui é apenas para as labels, não para forçar a ordem de split do algoritmo.
feature_names_mapping = {
    'question1': 'Q1: Ingestão excessiva de alimentos (SIM/NÃO)?',
    'question2': 'Q2: Angústia/Sofrimento (SIM/NÃO)?',
    'question3': 'Q3: Perda de controle sobre a ingestão (SIM/NÃO)?',
    'question4': 'Q4: Comportamentos compensatórios (SIM/NÃO)?',
    'question5': 'Q5: Come mais rapidamente (SIM/NÃO)?',
    'question6': 'Q6: Come até se sentir desconfortável (SIM/NÃO)?',
    'question7': 'Q7: Come grandes quantidades sem fome (SIM/NÃO)?',
    'question8': 'Q8: Come sozinho por vergonha (SIM/NÃO)?',
    'question9': 'Q9: Sente desgosto/culpa depois (SIM/NÃO)?'
}

# Criar a lista de nomes de features para a visualização, na ordem das colunas de X
feature_names = [feature_names_mapping.get(col, col) for col in X.columns]

# Nomes das classes para a variável alvo (0 para "Investigar outros transtornos", 1 para "Possível TCA")
class_names = ["Investigar outros transtornos", "Possível TCA"]

# 3. Inicializar e Treinar o Decision Tree Classifier
# Usamos um random_state para garantir a reprodutibilidade dos resultados.
# Sem definir max_depth inicialmente para ver a árvore completa.
dt_classifier = DecisionTreeClassifier(random_state=42)

# Treinar o modelo
dt_classifier.fit(X, y)

# 4. Visualizar a Árvore de Decisão
plt.figure(figsize=(28, 16)) # Ajuste o tamanho da figura para melhor visualização da árvore
plot_tree(dt_classifier,
          feature_names=feature_names,
          class_names=class_names,
          filled=True, # Preenche os nós com cores baseadas na classe
          rounded=True, # Arredonda as caixas dos nós
          fontsize=9) # Tamanho da fonte para maior clareza

# Adicionar um título à árvore
plt.title("Árvore de Decisão para Diagnóstico de TCA (Baseada em Dados Fictícios e Fluxograma)", fontsize=18)

# Definir o caminho para salvar a imagem
output_filename = 'decision_tree_tca_final.png'
plt.savefig(output_filename)
plt.close() # Fechar a figura para liberar memória

print(f"\nOperação concluída. A árvore de decisão foi gerada e salva como '{output_filename}'.")
print("\nNota Importante sobre a Ordem das Questões:")
print("O algoritmo DecisionTreeClassifier do scikit-learn otimiza a ordem das perguntas (features) em cada nó")
print("para obter a melhor separação dos dados. Portanto, a ordem exata das perguntas no fluxograma original")
print("não é rigidamente imposta, mas as perguntas mais relevantes (discriminativas) para seus dados tendem")
print("a aparecer nos níveis superiores da árvore gerada. As labels nas ramificações '0' e '1' indicam 'False' e 'True' (ou 'Não' e 'Sim') respectivamente.")