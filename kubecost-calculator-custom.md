1.csv input based on kubecost file api version 1.99.

obg chatgpt e copilot pelas correções de bug e descrições xD

```python
import pandas as pd
import os
from datetime import datetime
import numpy as np

def file_exists(file_path):
    """
    Verifica se um arquivo existe no caminho especificado.
    
    Args:
        file_path (str): Caminho do arquivo a ser verificado.
    
    Returns:
        bool: True se o arquivo existe, False caso contrário.
    """
    return os.path.exists(file_path)

def split_container_column(df, column_name='Container'):
    """
    Divide a coluna especificada em duas novas colunas 'Namespace' e 'Pod'.
    
    Args:
        df (pd.DataFrame): DataFrame contendo a coluna a ser dividida.
        column_name (str): Nome da coluna a ser dividida. Default é 'Container'.
    
    Returns:
        pd.DataFrame: DataFrame com as novas colunas 'Namespace' e 'Pod'.
    """
    if column_name not in df.columns:
        print(f"A coluna {column_name} não existe no DataFrame.")
        return df
    
    # Dividir a coluna 'Container'
    split_columns = df[column_name].str.split('/', expand=True)
    
    # Verificar o número de colunas resultantes
    if split_columns.shape[1] != 2:
        print("A coluna 'Container' não está no formato esperado.")
        return df
    
    df['Namespace'] = split_columns[0]
    df['Pod'] = split_columns[1]
    
    return df

def calculate_recommends(df):
    """
    Cria as colunas 'CPU-Rec-Base', 'CPU-Rec-Agressiva', 'CPU-Rec-Conservadora', 'CPU-EmUso', 'quantity', 'CPU-savingagressive', 'CPU-savingconservative',
    'Mem-Rec-Base', 'Mem-Rec-Agressiva', 'Mem-Rec-Conservadora', 'Mem-EmUso', 'Mem-savingagressive', 'Mem-savingconservative'
    com base nas colunas correspondentes.
    
    Args:
        df (pd.DataFrame): DataFrame contendo as colunas 'CPU Cores Recommended', 'CPU Cores Used', 'RAM Usage Bytes', 'RAM Request Bytes' e 'RAM Recommended Bytes'.
    
    Returns:
        pd.DataFrame: DataFrame com as novas colunas calculadas.
    """
    if 'CPU Cores Recommended' not in df.columns or 'CPU Cores Used' not in df.columns:
        print("As colunas 'CPU Cores Recommended' ou 'CPU Cores Used' não existem no DataFrame.")
        return df

    if 'RAM Recommended Bytes' not in df.columns or 'RAM Usage Bytes' not in df.columns:
        print("As colunas 'RAM Recommended Bytes' ou 'RAM Usage Bytes' não existem no DataFrame.")
        return df
    
    def conservative_cpu(value):
        try:
            value = float(value)
            result = value * 1000 * 1.3
            return np.ceil(result / 10) * 10
        except ValueError:
            return np.nan

    def aggressive_cpu(value):
        try:
            value = float(value)
            result = value * 1000 * 1.1
            return np.ceil(result / 10) * 10
        except ValueError:
            return np.nan

    def kubebase_cpu(value):
        try:
            value = float(value)
            return value * 1000
        except ValueError:
            return np.nan

    def used_rounded_cpu(value):
        try:
            value = float(value)
            return round(value * 1000, 1)
        except ValueError:
            return np.nan

    def conservative_mem(value):
        try:
            value = float(value) / 1048576 
            result = value * 1.3
            return np.ceil(result / 10) * 10
        except ValueError:
            return np.nan

    def aggressive_mem(value):
        try:
            value = float(value) / 1048576 
            result = value * 1.1
            return np.ceil(result / 10) * 10
        except ValueError:
            return np.nan

    def kubebase_mem(value):
        try:
            return round(float(value) / 1048576, 1)  # esquema pra usar apenas 1 casa dps da virgula
        except ValueError:
            return np.nan

    def used_rounded_mem(value):
        try:
            value = float(value) / 1048576  
            return round(value, 1)
        except ValueError:
            return np.nan

    # Calcular as novas colunas para CPU
    df['CPU-EmUso'] = df['CPU Cores Used'].apply(used_rounded_cpu)
    df['CPU-Rec-Base'] = df['CPU Cores Recommended'].apply(kubebase_cpu)
    df['CPU-Rec-Agressiva'] = df['CPU Cores Recommended'].apply(aggressive_cpu)
    df['CPU-Rec-Conservadora'] = df['CPU Cores Recommended'].apply(conservative_cpu)
    df['quantity'] = 1
    df['CPU-savingagressive'] = (df['CPU-Rec-Agressiva'] - df['CPU-EmUso']) * df['quantity']
    df['CPU-savingconservative'] = (df['CPU-Rec-Conservadora'] - df['CPU-EmUso']) * df['quantity']
    
    # Calcular as novas colunas para Memória
    df['Mem-EmUso'] = df['RAM Usage Bytes'].apply(used_rounded_mem)
    df['Mem-Rec-Base'] = df['RAM Recommended Bytes'].apply(kubebase_mem)
    df['Mem-Rec-Agressiva'] = df['RAM Recommended Bytes'].apply(aggressive_mem)
    df['Mem-Rec-Conservadora'] = df['RAM Recommended Bytes'].apply(conservative_mem)
    df['Mem-savingagressive'] = (df['Mem-Rec-Agressiva'] - df['Mem-EmUso']) * df['quantity']
    df['Mem-savingconservative'] = (df['Mem-Rec-Conservadora'] - df['Mem-EmUso']) * df['quantity']
    
    return df

def process_csv(input_csv_path):
    """
    Processa o arquivo CSV, divide a coluna 'Container' em 'Namespace' e 'Pod',
    calcula as colunas 'CPU-Rec-Base', 'CPU-Rec-Agressiva', 'CPU-Rec-Conservadora', 'CPU-EmUso', 'quantity', 'CPU-savingagressive', 'CPU-savingconservative',
    'Mem-Rec-Base', 'Mem-Rec-Agressiva', 'Mem-Rec-Conservadora', 'Mem-EmUso', 'Mem-savingagressive' e 'Mem-savingconservative',
    e salva o DataFrame modificado em um novo arquivo CSV.
    
    Args:
        input_csv_path (str): Caminho do arquivo CSV de entrada.
    """
    if not file_exists(input_csv_path):
        print(f"O arquivo {input_csv_path} não foi encontrado.")
        return
    
    # Carregar o CSV em um DataFrame
    df = pd.read_csv(input_csv_path)

    # Separar a coluna 'Container' em 'Namespace' e 'Pod'
    df = split_container_column(df)

    # Calcular as novas colunas
    df = calculate_recommends(df)

    # Exibir o DataFrame modificado para verificação
    print(df.head())

    # Gerar um nome de arquivo de saída com timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_csv_path = f'output_{timestamp}.csv'

    # Salvar o DataFrame modificado em um novo CSV
    df.to_csv(output_csv_path, index=False)

    print(f"Novo CSV salvo em: {output_csv_path}")

# Nome do arquivo CSV a ser processado
input_csv_path = '1.csv'

# Processar o arquivo CSV
process_csv(input_csv_path)
```
