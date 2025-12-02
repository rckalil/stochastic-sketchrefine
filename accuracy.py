import pandas as pd
import numpy as np

# Nomes dos arquivos
ARQUIVO_JULIA = 'results/julia_20_50.csv'
ARQUIVO_SPAQL = 'results/spaql_20_1000.csv'

try:
    # 1. Carregar DataFrame do Solver Julia (SamplingRB)
    df_julia = pd.read_csv(ARQUIVO_JULIA)
    
    # 2. Carregar DataFrame do Solver Python (SPaQL)
    df_spaql = pd.read_csv(ARQUIVO_SPAQL)
    
    print(f"✅ Dados carregados com sucesso!")
    print("-" * 40)
    
    print(f"## DataFrame Julia ({ARQUIVO_JULIA}) - Head:")
    print(df_julia.head())
    print("\n" + "=" * 40 + "\n")
    
    print(f"## DataFrame SPaQL ({ARQUIVO_SPAQL}) - Head:")
    print(df_spaql.head())
    print("-" * 40)
    
except FileNotFoundError as e:
    print(f"❌ ERRO: O arquivo '{e.filename}' não foi encontrado.")
    print("Certifique-se de que os arquivos 'julia.csv' e 'spaql.csv' estão no diretório de execução.")
    
# Os DataFrames (df_julia e df_spaql) estão agora prontos para manipulação.

# criar um índice único para cada tripla (m_time, ticker, sell_after) e adicioná-lo a ambos os DataFrames
cols = ['m_time', 'ticker', 'sell_after']

# verificar colunas
for df, name in ((df_julia, 'df_julia'), (df_spaql, 'df_spaql')):
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise KeyError(f"{name} missing columns: {missing}")

# normalizar tipos para evitar mismatch (usar str aqui é simples e robusto)
for df in (df_julia, df_spaql):
    for c in cols:
        df[c] = df[c].astype(str)

# construir conjunto único de triplas e gerar ids inteiros
combined = pd.concat([df_julia[cols], df_spaql[cols]]).drop_duplicates().reset_index(drop=True)
combined['_tuple'] = combined.apply(tuple, axis=1)
combined['triplet_id'] = pd.factorize(combined['_tuple'])[0]
mapping = dict(zip(combined['_tuple'], combined['triplet_id']))

# aplicar mapping a ambos os DataFrames
for df in (df_julia, df_spaql):
    df['triplet_id'] = df.apply(lambda r: mapping.get(tuple(r[cols]), -1), axis=1)

print(f"✅ Criados {len(mapping)} triplet_id únicos e adicionados como coluna 'triplet_id' em ambos os DataFrames.")

#__________________________________________________________________________________

# --- PARÂMETROS DE CLASSIFICAÇÃO ---

# Definir os thresholds para a coluna Objective_Value.
# O valor máximo na coluna é 50.
# T1: Limite inferior para considerar o peso significativo (Classe 1). 
#     (Ex: Qualquer coisa acima de 1 unidade de peso é relevante)
# THRESHOLD_SIGNIFICANTE = 0.5 

# T2: Não é necessário para classificação binária simples, mas poderia ser 
#     usado para uma classificação ternária (0, 1, 2) ou para desambiguação.
#     Vamos usar apenas um T1 para a classificação 0/1.

# --- FUNÇÃO DE CLASSIFICAÇÃO ---

def aplicar_classificacao_binaria(df: pd.DataFrame, tr) -> pd.DataFrame:
    """
    Cria a coluna 'class' nos DataFrames, classificando a linha como 1
    se o Objective_Value exceder o threshold, e 0 caso contrário.
    """
    
    # Valida se a coluna Objective_Value existe antes de processar
    if 'Objective_Value' not in df.columns:
        print(f"❌ ERRO: Coluna 'Objective_Value' não encontrada no DataFrame.")
        return df

    # Aplica a classificação: 1 se for >= THRESHOLD, 0 caso contrário.
    df['class'] = np.where(
        df['Objective_Value'] >= tr,
        1,  # Classe 1: Alocação Significativa
        0   # Classe 0: Alocação Desprezível/Ruído
    )
    
    return df

# --- APLICAÇÃO NOS DOIS DATAFRAMES ---

# Aplicar a classificação no DataFrame Julia
df_julia = aplicar_classificacao_binaria(df_julia, 0.5)

# Aplicar a classificação no DataFrame SPaQL
df_spaql = aplicar_classificacao_binaria(df_spaql, 0.5)

print("\n" + "="*60)
print(f"✅ Classificação Binária Concluída (Threshold={0.5})")
print("Nova coluna 'class' adicionada a df_julia e df_spaql.")
print("="*60)
print("Amostra do df_julia com a nova coluna 'class':")
print(df_julia[['Objective_Value', 'class']].head(15))



from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score
import pandas as pd
import numpy as np

# --- 1. PREPARAÇÃO DOS DADOS (Assumindo que df_julia e df_spaql já estão carregados) ---

# Reutilizando a lógica de carregamento e classificação (necessária para rodar o bloco)
# (Substitua por seus DataFrames ativos, se estiver no ambiente interativo)
# df_julia = aplicar_classificacao_binaria(df_julia)
# df_spaql = aplicar_classificacao_binaria(df_spaql)

# 2. MERGE DOS DATASETES PARA COMPARAÇÃO

# O merge deve ser feito usando o índice comum criado ('triplet_id').
# Usamos 'inner' para garantir que comparamos apenas as triplas que apareceram em ambos.
df_comparacao = pd.merge(
    df_julia[['triplet_id', 'class']].rename(columns={'class': 'gabarioto_julia'}),
    df_spaql[['triplet_id', 'class']].rename(columns={'class': 'spaql_previsao'}),
    on='triplet_id',
    how='inner'
)

# 3. EXTRAÇÃO DAS CLASSIFICAÇÕES

# Gabarito: As classes do solver Julia (Y_true)
y_true = df_comparacao['gabarioto_julia'].values

# Previsão: As classes do solver SPaQL (Y_pred)
y_pred = df_comparacao['spaql_previsao'].values

# --- 4. CÁLCULO DAS MÉTRICAS ---

# Acurácia (Taxa de acertos gerais)
acuracia = accuracy_score(y_true, y_pred)

# Precisão (Dos que o SPaQL disse que eram 1, quantos eram 1 de verdade?)
precisao = precision_score(y_true, y_pred)

# Recall/Sensibilidade (Dos que eram 1 de verdade, quantos o SPaQL acertou?)
recall_ = recall_score(y_true, y_pred)

# Matriz de Confusão
matriz_confusao = confusion_matrix(y_true, y_pred)


# --- 5. RESULTADOS ---

print("\n" + "="*60)
print("RESULTADOS DA ACURÁCIA (JULIA COMO GABARITO)")
print("="*60)

print(f"Número de Triplas Únicas Comparadas: {len(y_true)}")
print(f"1. Acurácia Geral (Overall Accuracy): {acuracia:.4f}")
print(f"2. Precisão (Precision - Class 1): {precisao:.4f}")
print(f"3. Recall (Sensibilidade - Class 1): {recall_:.4f}")
print("\nMatriz de Confusão:")
print(f"True Negatives (0 -> 0): {matriz_confusao[0, 0]}")
print(f"False Positives (0 -> 1): {matriz_confusao[0, 1]}")
print(f"False Negatives (1 -> 0): {matriz_confusao[1, 0]}")
print(f"True Positives (1 -> 1): {matriz_confusao[1, 1]}")
print("="*60)