import pandas as pd
import matplotlib.pyplot as plt

# Caminho do seu arquivo CSV
df = pd.read_csv('/Users/erikalima/Documents/all_tasks_developed_by_erika_lima.csv')

# Garante que a coluna de dias é numérica
df['Time to Develop (days)'] = pd.to_numeric(df['Time to Develop (days)'], errors='coerce')

# Agrupa por tipo de issue e calcula a média
media_tempo = df.groupby('Issue Type')['Time to Develop (days)'].mean().sort_values()

# Plota o gráfico
plt.figure(figsize=(10,6))
media_tempo.plot(kind='bar', color='skyblue')
plt.title('Tempo médio de desenvolvimento por tipo de task')
plt.ylabel('Tempo médio (dias)')
plt.xlabel('Tipo de Task')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
