"""Funções de visualização para a análise PRODES/INPE."""

import matplotlib.ticker as ticker
import seaborn as sns
from matplotlib import pyplot as plt


def configurar_tema() -> None:
    """Aplica um tema visual consistente aos gráficos."""
    sns.set_theme(style="whitegrid", context="notebook")


def plotar_evolucao_desmatamento(df_desmatamento):
    """Plota a evolução da área desmatada por bioma ao longo dos anos."""
    figura, eixo = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        data=df_desmatamento,
        x="ano",
        y="desmatado_milhoes",
        hue="bioma",
        marker="o",
        linewidth=2.5,
        ax=eixo,
    )
    eixo.set_title("Evolução do Desmatamento Total por Bioma (2000-2023)", pad=20)
    eixo.set_xlabel("Ano")
    eixo.set_ylabel("Área desmatada em milhões de km²")
    eixo.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
    eixo.legend(title="Bioma", bbox_to_anchor=(1.01, 1), loc="upper left")
    figura.tight_layout()
    return figura, eixo


def plotar_area_total_monitorada(df_area_total):
    """Plota a área total monitorada por bioma ao longo dos anos."""
    figura, eixo = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        data=df_area_total,
        x="ano",
        y="area_total_milhoes",
        hue="bioma",
        marker="o",
        ax=eixo,
    )
    eixo.set_title("Área Total Monitorada por Bioma")
    eixo.set_xlabel("Ano")
    eixo.set_ylabel("Área total em milhões de km²")
    eixo.yaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
    eixo.legend(title="Bioma", bbox_to_anchor=(1.01, 1), loc="upper left")
    figura.tight_layout()
    return figura, eixo


def plotar_percentual_desmatado(df_percentual):
    """Plota o percentual de área desmatada por bioma ao longo dos anos."""
    figura, eixo = plt.subplots(figsize=(12, 6))
    sns.lineplot(
        data=df_percentual,
        x="ano",
        y="porcentagem_desmatada",
        hue="bioma",
        marker="o",
        ax=eixo,
    )
    eixo.set_title("Percentual da Área do Bioma Perdida por Ano")
    eixo.set_xlabel("Ano")
    eixo.set_ylabel("Área desmatada (%)")
    eixo.legend(title="Bioma", bbox_to_anchor=(1.01, 1), loc="upper left")
    figura.tight_layout()
    return figura, eixo


def plotar_ranking_absoluto_estados(df_estados):
    """Plota o ranking absoluto de área desmatada por UF."""
    figura, eixo = plt.subplots(figsize=(10, 8))
    dados = df_estados.sort_values("desmatado_milhoes", ascending=False)
    sns.barplot(
        data=dados,
        x="desmatado_milhoes",
        y="sigla_uf",
        hue="desmatado_milhoes",
        legend=False,
        ax=eixo,
    )
    eixo.set_title("Ranking Absoluto: Área Total Desmatada")
    eixo.set_xlabel("Área desmatada em milhões de km²")
    eixo.set_ylabel("Estado")
    eixo.xaxis.set_major_formatter(ticker.FormatStrFormatter("%.2f"))
    figura.tight_layout()
    return figura, eixo


def plotar_ranking_relativo_estados(df_estados):
    """Plota o ranking relativo de área desmatada por UF."""
    figura, eixo = plt.subplots(figsize=(10, 8))
    dados = df_estados.sort_values("porcentagem_desmatada", ascending=False)
    sns.barplot(
        data=dados,
        x="porcentagem_desmatada",
        y="sigla_uf",
        hue="porcentagem_desmatada",
        legend=False,
        ax=eixo,
    )
    eixo.set_title("Ranking Relativo de Área Desmatada")
    eixo.set_xlabel("Área desmatada (%)")
    eixo.set_ylabel("Estado")
    figura.tight_layout()
    return figura, eixo
