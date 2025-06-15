# 📌 IMPORTAÇÕES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# 📌 CARREGAR DADOS
df_evasao = pd.read_csv('data/evasao_historica.csv')
df_renda = pd.read_csv('data/renda_media_regiao.csv')
df_ideb = pd.read_csv('data/indicadores_educacionais.csv')
df_infra = pd.read_csv('data/infraestrutura_escolar_simulada.csv')

# 📌 TRATAR RENDA (usar Brasil como referência)
df_renda_brasil = df_renda[df_renda['Regiao'] == 'brasil'].drop(columns='Regiao')
df_renda_brasil.rename(columns={'Renda_Media': 'Renda_Media'}, inplace=True)

# 📌 TRATAR IDEB (fazer média por rede pública e privada)
#   Limpar coluna IDEB: manter apenas linhas com números válidos
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

df_ideb = df_ideb[df_ideb['IDEB'].apply(is_number)]
df_ideb['IDEB'] = df_ideb['IDEB'].astype(float)

df_ideb['Dependencia_Administrativa'] = df_ideb['Rede'].apply(lambda x: 'pública' if x in ['estadual', 'pública', 'municipal'] else 'privada')
ideb_por_rede = df_ideb.groupby('Dependencia_Administrativa')['IDEB'].mean().reset_index()
ideb_por_rede.rename(columns={'IDEB': 'IDEB_Medio'}, inplace=True)

# 📌 UNIR BASES
df = df_evasao.merge(df_renda_brasil, on='Ano', how='left')
df = df.merge(ideb_por_rede, on='Dependencia_Administrativa', how='left')

# 📌 INFRAESTRUTURA - simulando repetição para tamanho da base
infra_mean = df_infra.mean()
infra_data = pd.DataFrame([infra_mean.values] * len(df), columns=infra_mean.index)
df = pd.concat([df.reset_index(drop=True), infra_data.reset_index(drop=True)], axis=1)

# 📌 TRATAR VARIÁVEIS CATEGÓRICAS
le = LabelEncoder()
df['Dependencia_Administrativa'] = le.fit_transform(df['Dependencia_Administrativa'])

# 📌 VARIÁVEIS DE ENTRADA E SAÍDA
X = df.drop(columns=['Taxa_Abandono'])
y = df['Taxa_Abandono']

# 📌 TREINAR MODELO
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# 📌 AVALIAÇÃO
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f'MSE: {mse}')
print(f'R²: {r2}')


# 📌 PREVISÃO MÉDIA
future_data = pd.DataFrame({
    'Ano': [2025],
    'Dependencia_Administrativa': [le.transform(['pública'])[0]],
    'Renda_Media': [df['Renda_Media'].mean()],
    'IDEB_Medio': [df['IDEB_Medio'].mean()],
    'Curricular units 1st sem (enrolled)': [infra_mean['Curricular units 1st sem (enrolled)']],
    'Tuition fees up to date': [infra_mean['Tuition fees up to date']],
    'Scholarship holder': [infra_mean['Scholarship holder']]
})
pred = model.predict(future_data)
print( f'\nPrevisão de taxa de evasão para uma escola pública média no futuro(2025): {round(pred[0],2)}%')

# 📌 PREVISÕES PARA 2026 e 2027
anos_futuros = [2026, 2027]
previsoes_futuras = []

# Crescimento estimado: +3% na renda e +0.2 no IDEB por ano
renda_atual = df['Renda_Media'].mean()
ideb_atual = df['IDEB_Medio'].mean()

for i, ano in enumerate(anos_futuros, start=1):
    renda_future = renda_atual * (1 + 0.03 * i)
    ideb_future = ideb_atual + (0.2 * i)
    input_data = pd.DataFrame({
        'Ano': [ano],
        'Dependencia_Administrativa': [le.transform(['pública'])[0]],
        'Renda_Media': [renda_future],
        'IDEB_Medio': [ideb_future],
        'Curricular units 1st sem (enrolled)': [infra_mean['Curricular units 1st sem (enrolled)']],
        'Tuition fees up to date': [infra_mean['Tuition fees up to date']],
        'Scholarship holder': [infra_mean['Scholarship holder']]
    })
    pred_fut = model.predict(input_data)[0]
    previsoes_futuras.append((ano, pred_fut))

print("\n📊 Previsões Futuras de Evasão Escolar:")
for ano, taxa in previsoes_futuras:
    print(f"{ano}: {round(taxa, 2)}%")


