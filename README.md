Claro! Aqui está o README atualizado incluindo a estrutura de pastas que você pediu:

---

# Previsão de Evasão Escolar com Random Forest

## Estrutura do Projeto

```
/projeto_evasao/
├── data/
│   ├── evasao_historica.csv
│   ├── renda_media_regiao.csv
│   ├── indicadores_socioeconomicos.csv
│   ├── indicadores_educacionais.csv
│   └── infraestrutura_escolar_simulada.csv
├── modelo_evasao.py
├── requirements.txt
└── README.md
```

---

## Descrição

Este projeto utiliza dados históricos de evasão escolar, renda média por região, indicadores socioeconômicos e educacionais (IDEB), além de infraestrutura escolar simulada para treinar um modelo de regressão (Random Forest) que prevê a taxa de evasão escolar em escolas públicas.

O modelo gera previsões para os anos futuros com base em cenários de crescimento da renda e melhoria do IDEB, fornecendo insights importantes para políticas públicas educacionais.

---

## Requisitos

* Python 3.6 ou superior
* Bibliotecas Python (listadas no `requirements.txt`):

  * pandas
  * numpy
  * scikit-learn
  * matplotlib
  * seaborn

Você pode instalar as dependências com:

```bash
pip install -r requirements.txt
```

---

## Arquivos de dados

Os arquivos CSV utilizados devem estar organizados na pasta `data/` conforme a estrutura acima.

---

## Uso

1. Clone o repositório ou copie o projeto para sua máquina local.
2. Coloque os arquivos CSV na pasta `data/`.
3. Instale as dependências.
4. Execute o script:

```bash
python modelo_evasao.py
```

O script irá:

* Carregar e tratar os dados.
* Treinar o modelo Random Forest para prever a taxa de evasão.
* Avaliar o modelo com métricas MSE e R².
* Fazer previsões para os anos 2025, 2026 e 2027.
* Imprimir as taxas previstas de evasão escolar para esses anos.

---

## Resultados esperados

* Métricas de avaliação do modelo indicando o desempenho (exemplo: MSE baixo e R² alto).
* Previsão numérica da taxa de evasão para os anos futuros simulados.

---

## Interpretação

O modelo indica que:

* A evasão escolar tende a diminuir com o aumento da renda média e melhoria dos indicadores educacionais.
* Pequenas variações nas previsões indicam que outros fatores além dos usados podem influenciar a evasão.
* A análise pode ajudar na formulação de políticas para combater a evasão escolar.


