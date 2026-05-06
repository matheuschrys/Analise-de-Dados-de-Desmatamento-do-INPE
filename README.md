# Análise de Desmatamento no Brasil (PRODES/INPE)

Projeto de análise de dados sobre o desmatamento nos biomas e estados brasileiros entre 2000 e 2023, com dados do projeto PRODES/INPE e metadados municipais brasileiros.

O repositório foi organizado para separar dados, notebook e código reutilizável, facilitando a reprodução da análise e futuras evoluções.

## Estrutura do projeto

```text
.
├── data/
│   └── raw/
│       ├── br_bd_diretorios_brasil_municipio.csv
│       └── br_inpe_prodes_municipio_bioma.csv
├── notebooks/
│   └── Desmatamento_PRODES.ipynb
├── src/
│   └── desmatamento_inpe/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analysis.py
│       └── visualization.py
├── requirements.txt
└── README.md
```

## Objetivos de aprendizagem

Este projeto demonstra técnicas fundamentais de análise de dados com Python:

- leitura de arquivos CSV;
- integração de bases com `merge` por `id_municipio`;
- exploração inicial com `info`, `describe` e inspeção de amostras;
- agrupamentos e agregações por ano, bioma e UF;
- criação de colunas derivadas, como valores em milhões e percentuais;
- visualização com gráficos de linhas e barras.

## Bases de dados

Os arquivos usados pela análise estão versionados em `data/raw`:

1. `br_inpe_prodes_municipio_bioma.csv`: histórico de área total, área desmatada, vegetação natural, não vegetação natural e hidrografia por município e bioma.
2. `br_bd_diretorios_brasil_municipio.csv`: metadados dos municípios, incluindo UF, região e indicador de Amazônia Legal.

## Principais análises

O notebook `notebooks/Desmatamento_PRODES.ipynb` gera as seguintes visões:

- evolução do desmatamento total por bioma;
- área total monitorada por bioma;
- percentual de área desmatada por bioma;
- ranking absoluto de desmatamento por estado;
- ranking relativo de desmatamento por estado.

## Como reproduzir

1. Clone o repositório.
2. Crie e ative um ambiente virtual, se desejar:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o notebook:

   ```bash
   jupyter notebook notebooks/Desmatamento_PRODES.ipynb
   ```

Também é possível executar um resumo das tabelas agregadas pelo módulo Python:

```bash
PYTHONPATH=src python -m desmatamento_inpe
```

## Organização do código

- `src/desmatamento_inpe/analysis.py`: concentra carga dos dados e cálculos tabulares.
- `src/desmatamento_inpe/visualization.py`: concentra funções de visualização.
- `notebooks/Desmatamento_PRODES.ipynb`: mantém a narrativa da análise, chamando funções reutilizáveis em vez de repetir lógica.

## Tecnologias utilizadas

- Python 3.12+
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

Desenvolvido originalmente por Chrys — Bacharelando em Ciência da Computação (IFAM).
