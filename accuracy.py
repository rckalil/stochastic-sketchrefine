import pandas as pd
import numpy as np

# Nomes dos arquivos (Assumindo que os DataFrames ativos são df_julia e df_spaql)
# ... (Seu código de carregamento e preparacao de df_julia e df_spaql aqui) ...

# --- 1. PREPARAÇÃO DOS DADOS (Necessária para contexto e funcionalidade) ---

# Reutilizando as variáveis para garantir que o script seja executável
ARQUIVO_JULIA = 'results/julia_20_50.csv'
ARQUIVO_SPAQL = 'results/spaql_20_2000.csv'
THRESHOLD_SIGNIFICANTE = 0.5 

try:
    df_julia = pd.read_csv(ARQUIVO_JULIA)
    print(f"Arquivo Julia carregado com {len(df_julia)} linhas.")
    df_spaql = pd.read_csv(ARQUIVO_SPAQL)
    print(f"Arquivo SPaQL carregado com {len(df_spaql)} linhas.")
except FileNotFoundError as e:
    # Saída de erro se os arquivos nao existirem
    pass 
    
# --- Funções de Preparação (simplificadas para rodar) ---
def aplicar_classificacao_binaria(df: pd.DataFrame, tr) -> pd.DataFrame:
    df['class'] = np.where(
        df['Objective_Value'] >= tr, 1, 0
    )
    return df

cols = ['ticker', 'sell_after']
for df in (df_julia, df_spaql):
    for c in cols:
        df[c] = df[c].astype(str)

combined = pd.concat([df_julia[cols], df_spaql[cols]]).reset_index(drop=True)
combined['_tuple'] = combined.apply(tuple, axis=1)
combined['triplet_id'] = pd.factorize(combined['_tuple'])[0]
mapping = dict(zip(combined['_tuple'], combined['triplet_id']))

for df in (df_julia, df_spaql):
    df['triplet_id'] = df.apply(lambda r: mapping.get(tuple(r[cols]), -1), axis=1)

print(f"Número de triplas únicas: {len(mapping)}")
    
df_julia = aplicar_classificacao_binaria(df_julia, THRESHOLD_SIGNIFICANTE)
df_spaql = aplicar_classificacao_binaria(df_spaql, THRESHOLD_SIGNIFICANTE)

# MERGE DOS DATASETES PARA COMPARAÇÃO
df_comparacao = pd.merge(
    df_julia[['triplet_id', 'class']].rename(columns={'class': 'gabarioto_julia'}),
    df_spaql[['triplet_id', 'class']].rename(columns={'class': 'spaql_previsao'}),
    on='triplet_id',
    how='inner'
)

# --- INÍCIO DOS CÁLCULOS MANUAIS COM NUMPY ---

# Gabarito: Classes do solver Julia (Y_true)
y_true = df_comparacao['gabarioto_julia'].values

# Previsão: Classes do solver SPaQL (Y_pred)
y_pred = df_comparacao['spaql_previsao'].values

# 1. CÁLCULO DA MATRIZ DE CONFUSÃO (TP, TN, FP, FN)

# Condições booleanas:
TP = np.sum((y_true == 1) & (y_pred == 1)) # True Positives (1 no gabarito, 1 na previsao)
TN = np.sum((y_true == 0) & (y_pred == 0)) # True Negatives (0 no gabarito, 0 na previsao)
FP = np.sum((y_true == 0) & (y_pred == 1)) # False Positives (0 no gabarito, 1 na previsao)
FN = np.sum((y_true == 1) & (y_pred == 0)) # False Negatives (1 no gabarito, 0 na previsao)

total_amostras = len(y_true)

# Evitar divisão por zero se não houver casos positivos ou negativos
denominador_precisao = TP + FP
denominador_recall = TP + FN

# 2. CÁLCULO DAS MÉTRICAS PRINCIPAIS

# Acurácia: (Acertos totais) / (Total)
acuracia = (TP + TN) / total_amostras

# Precisão: TP / (TP + FP) -> Quão confiável é a Classe 1 do SPaQL
precisao = TP / denominador_precisao if denominador_precisao > 0 else 0.0

# Recall: TP / (TP + FN) -> Quão bem o SPaQL encontrou todas as Classes 1
recall_ = TP / denominador_recall if denominador_recall > 0 else 0.0

# --- 3. RESULTADOS ---

print("\n" + "="*60)
print("RESULTADOS DA ACURÁCIA (CALCULADOS COM NUMPY)")
print("="*60)

print(f"Número de Triplas Únicas Comparadas: {total_amostras}")
print("\nMatriz de Confusão (Contagem):")
print(f"  [TN] True Negatives (0 -> 0): {TN}")
print(f"  [FP] False Positives (0 -> 1): {FP}")
print(f"  [FN] False Negatives (1 -> 0): {FN}")
print(f"  [TP] True Positives (1 -> 1): {TP}")

print("\n--- Métricas de Desempenho ---")
print(f"1. Acurácia Geral (Overall Accuracy): {acuracia:.4f}")
print(f"2. Precisão (Precision - Classe 1): {precisao:.4f}")
print(f"3. Recall (Sensibilidade - Classe 1): {recall_:.4f}")
print("="*60)