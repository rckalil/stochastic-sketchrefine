import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os Dados
# Certifique-se de que o arquivo 'tabela_processamento.csv' está na mesma pasta
# do seu script Python, ou forneça o caminho completo do arquivo.

try:
    # O seu CSV usa vírgula (',') como separador decimal para os números,
    # então usamos 'decimal=',''. O separador de colunas parece ser espaço ou tab,
    # então usaremos 'sep='\s+' para tratar múltiplos espaços como um único separador.
    df = pd.read_csv(
        'tabela_processamento.csv',
        sep=r'\s+', # Regex para um ou mais espaços como separador
        decimal=',', # A vírgula é o separador decimal
        encoding='utf-8' # Tentativa de encoding comum
    )
except FileNotFoundError:
    print("Erro: O arquivo 'tabela_processamento.csv' não foi encontrado.")
    exit()
except Exception as e:
    print(f"Erro ao ler o arquivo CSV: {e}")
    # Tenta com o separador de ponto e vírgula, caso o 'sep=r'\s+' falhe
    try:
        df = pd.read_csv('tabela_processamento.csv', sep=';', decimal=',')
    except Exception as e:
        print(f"Tentativa com separador ';' também falhou: {e}")
        exit()


# 2. Limpeza de Dados (Remover espaços extras e converter para numérico, se necessário)
# O pandas com 'decimal=','' geralmente faz a conversão correta,
# mas vamos garantir que as colunas de interesse são numéricas.

# As colunas de interesse são 'Linhas', 'Total' e 'Consulta'
print("Colunas disponíveis no DataFrame:", df.columns.tolist())
df['Linhas'] = pd.to_numeric(df['Linhas'], errors='coerce')
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')
df['Consulta'] = pd.to_numeric(df['Consulta'], errors='coerce')

# Remover linhas com valores inválidos (NaN) após a conversão
df.dropna(subset=['Linhas', 'Total', 'Consulta'], inplace=True)


# 3. Geração do Gráfico 1: Linhas X Total
# ----------------------------------------------------------------------
plt.figure(figsize=(10, 6)) # Define o tamanho da figura

plt.plot(
    df['Linhas'], # Eixo X
    df['Total'], # Eixo Y
    marker='o', # Marcadores circulares em cada ponto
    linestyle='-', # Linha contínua
    color='blue'
)

# Configurações do gráfico
plt.title('Tempo Total de Execução vs. Número de Linhas', fontsize=16)
plt.xlabel('Número de Linhas', fontsize=12)
plt.ylabel('Tempo Total (segundos)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6) # Adiciona grade suave
plt.xticks(rotation=45) # Rotaciona os rótulos do eixo X para melhor leitura
plt.tight_layout() # Ajusta o layout para evitar cortes
plt.show()


# 4. Geração do Gráfico 2: Linhas X Consulta
# ----------------------------------------------------------------------
plt.figure(figsize=(10, 6)) # Define o tamanho da figura

plt.plot(
    df['Linhas'], # Eixo X
    df['Consulta'], # Eixo Y
    marker='s', # Marcadores quadrados
    linestyle='--', # Linha tracejada
    color='red'
)

# Configurações do gráfico
plt.title('Tempo de Consulta vs. Número de Linhas', fontsize=16)
plt.xlabel('Número de Linhas', fontsize=12)
plt.ylabel('Tempo de Consulta (segundos)', fontsize=12)
plt.grid(True, linestyle='-', alpha=0.5) # Adiciona grade
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nOs gráficos foram gerados e exibidos.")